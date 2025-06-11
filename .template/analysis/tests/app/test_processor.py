"""
Unit test for processor.py in analysis repositories.
"""


def test_analyze_data():
    from app.processor import analyze_data

    result = analyze_data({"symbol": "AAPL", "price": 150.00})
    assert isinstance(result, dict)
