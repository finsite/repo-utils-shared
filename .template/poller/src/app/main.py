"""Main application entry point.

Polls stock data from an external API and sends it to a message queue.
"""

import logging
import time
from typing import Any

from app import config_shared
from app.message_queue.queue_sender import QueueSender
from app.poller_factory import PollerFactory
from app.utils import validate_environment_variables
from app.utils.rate_limit import RateLimiter
from app.utils.setup_logger import setup_logger

# Mapping of log level strings to logging module constants
LOG_LEVEL_MAP = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


def _redact(value: str, show_last: int = 2) -> str:
    """Redact sensitive strings for secure logging."""
    if not value:
        return "[REDACTED]"
    return f"{'*' * (len(value) - show_last)}{value[-show_last:]}"


def main() -> None:
    """Run the main polling loop to collect and send stock data."""
    validate_environment_variables(["POLLER_TYPE", "SYMBOLS"])

    # Load configuration
    log_level = config_shared.get_config_value("LOG_LEVEL", "INFO")
    poll_interval = config_shared.get_polling_interval()
    poller_type = config_shared.get_poller_type()
    rate_limit = config_shared.get_rate_limit()
    retry_delay = config_shared.get_retry_delay()
    structured = config_shared.get_config_bool("STRUCTURED_LOGGING", False)

    # Set up logger
    logger = setup_logger(
        __name__, level=LOG_LEVEL_MAP.get(log_level.lower(), logging.INFO), structured=structured
    )

    # Initialize components
    rate_limiter = RateLimiter(max_requests=rate_limit, time_window=1)
    queue_sender = QueueSender()
    poller_factory = PollerFactory()
    poller = poller_factory.create_poller()

    try:
        logger.info("🚀 Starting poller: [REDACTED]")
        logger.info("📅 Polling interval: %s seconds", poll_interval)

        while True:
            try:
                symbols: list[str] = config_shared.get_symbols()
                logger.debug("🔍 Loaded %d symbols", len(symbols))
            except Exception:
                logger.warning("⚠️ Failed to load symbols (redacted) – skipping iteration")
                time.sleep(retry_delay)
                continue

            for symbol in symbols:
                redacted_symbol = _redact(symbol)
                context_key = _redact(f"{poller_type}-{symbol}")

                rate_limiter.acquire(context=context_key)

                try:
                    logger.debug("📡 Polling symbol: [REDACTED]")
                    data: Any = poller.poll([symbol])
                    queue_sender.send_message(data)
                except Exception:
                    logger.error("❌ Polling error for symbol: [REDACTED]")
                    logger.info("⏳ Retrying after %s seconds...", retry_delay)
                    time.sleep(retry_delay)

            time.sleep(poll_interval)

    except KeyboardInterrupt:
        logger.info("🛑 Polling interrupted by user.")
    except Exception:
        logger.exception("🚨 Unexpected poller error (details redacted)")
    finally:
        logger.info("📦 Shutting down poller...")
        queue_sender.close()


if __name__ == "__main__":
    main()
