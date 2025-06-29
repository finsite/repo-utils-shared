from app.utils.types import (
    is_valid_batch,
    is_valid_payload,
    is_valid_trade_event,
    validate_dict,
    validate_list_of_dicts,
)


def test_validate_dict():
    assert validate_dict({"a": 1, "b": 2}, ["a", "b"]) is True
    assert validate_dict({"a": 1}, ["a", "b"]) is False


def test_validate_list_of_dicts():
    valid = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    invalid = [{"a": 1}, "not a dict"]
    assert validate_list_of_dicts(valid, ["a", "b"]) is True
    assert validate_list_of_dicts(invalid, ["a"]) is False


def test_is_valid_payload():
    assert is_valid_payload({"symbol": "AAPL", "timestamp": "2023-01-01T00:00:00Z"}) is True
    assert is_valid_payload({"symbol": "AAPL"}) is False


def test_is_valid_batch():
    valid = [{"symbol": "AAPL", "timestamp": "2023-01-01T00:00:00Z"}]
    assert is_valid_batch(valid) is True
    assert is_valid_batch([{"symbol": "AAPL"}]) is False


def test_is_valid_trade_event():
    valid = {
        "symbol": "AAPL",
        "action": "BUY",
        "quantity": 10,
        "price": 150.0,
        "timestamp": "2023-01-01T00:00:00Z",
    }
    invalid = {"symbol": "AAPL", "action": "HOLD"}
    assert is_valid_trade_event(valid) is True
    assert is_valid_trade_event(invalid) is False
