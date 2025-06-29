import pytest

from app.output_handler import OutputDispatcher
from app.utils.types import OutputMode


def test_output_dispatcher_init():
    dispatcher = OutputDispatcher()
    assert isinstance(dispatcher.output_modes, list)


def test_get_dispatch_method():
    dispatcher = OutputDispatcher()
    method = dispatcher._get_dispatch_method(OutputMode.LOG)
    assert callable(method)
