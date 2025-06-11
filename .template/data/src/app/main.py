"""Entrypoint for data poller."""

from app.config import get_log_level
from app.poller_factory import get_poller
from app.utils.setup_logger import setup_logger

logger = setup_logger(__name__, level=get_log_level())


def main() -> None:
    logger.info("🚀 Starting data poller...")
    poller = get_poller()
    poller.run()


if __name__ == "__main__":
    main()
