"""Pytest configuration file."""

import pytest

from finance_project.main import app
# from finance_project.models.stocks import Stock
from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
    return TestClient(app)

@pytest.fixture
def mock_expected_stocks_list():
    return [
        {
            "name": "Apple Company",
            "price": 102,
            "code": "AAPL.US"
        },
        {
            "name": "Google Company",
            "price": 78,
            "code": "GOOG.US"
        },
        {
            "name": "Microsoft Company",
            "price": 92,
            "code": "MSFT.US"
        }
    ]
    