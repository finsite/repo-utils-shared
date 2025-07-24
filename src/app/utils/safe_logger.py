"""
Wrapper around the standard logger that applies redaction and structured logging.

This ensures that sensitive fields are redacted and logs follow consistent formatting.
"""

import os
import logging
from typing import Optional, Any, Dict

from app.utils.redactor import redact_dict
from app.utils.setup_logger import setup_logger

# Controls whether to log full payloads (only in dev/test)
SAFE_LOG_FULL: bool = os.getenv("SAFE_LOG_FULL", "false").lower() == "true"
SAFE_LOG_STRUCTURED: bool = os.getenv("SAFE_LOG_STRUCTURED", "false").lower() == "true"

# Base logger instance
logger: logging.Logger = setup_logger(__name__, structured=SAFE_LOG_STRUCTURED)


def safe_info(message: str, data: Optional[Dict[str, Any]] = None) -> None:
    """
    Logs a sanitized info-level message.

    Args:
        message (str): The log message or context.
        data (Optional[Dict[str, Any]]): Optional dictionary payload to log (will be redacted if needed).
    """
    if data is None:
        logger.info(message)
        return

    payload = data if SAFE_LOG_FULL else redact_dict(data)
    logger.info("%s | keys=%s", message, list(payload.keys()))


def safe_warning(message: str, data: Optional[Dict[str, Any]] = None) -> None:
    """
    Logs a sanitized warning-level message.

    Args:
        message (str): The log message or context.
        data (Optional[Dict[str, Any]]): Optional dictionary payload to log (will be redacted if needed).
    """
    if data is None:
        logger.warning(message)
        return

    payload = data if SAFE_LOG_FULL else redact_dict(data)
    logger.warning("%s | keys=%s", message, list(payload.keys()))


def safe_error(message: str, data: Optional[Dict[str, Any]] = None) -> None:
    """
    Logs a sanitized error-level message.

    Args:
        message (str): The log message or context.
        data (Optional[Dict[str, Any]]): Optional dictionary payload to log (will be redacted if needed).
    """
    if data is None:
        logger.error(message)
        return

    payload = data if SAFE_LOG_FULL else redact_dict(data)
    logger.error("%s | keys=%s", message, list(payload.keys()))


def safe_debug(message: str, data: Optional[Dict[str, Any]] = None) -> None:
    """
    Logs a sanitized debug-level message.

    Args:
        message (str): The log message or context.
        data (Optional[Dict[str, Any]]): Optional dictionary payload to log (will be redacted if needed).
    """
    if data is None:
        logger.debug(message)
        return

    payload = data if SAFE_LOG_FULL else redact_dict(data)
    logger.debug("%s | keys=%s", message, list(payload.keys()))
