import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_convert_usd_to_eur():
    response = client.post(
        "/convert",
        json={"amount": 100, "from_currency": "USD", "to_currency": "EUR"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["converted_amount"] == 92.0


def test_rejects_invalid_amount():
    response = client.post(
        "/convert",
        json={"amount": 0, "from_currency": "USD", "to_currency": "EUR"},
    )
    assert response.status_code == 422


def test_rejects_unknown_currency():
    response = client.post(
        "/convert",
        json={"amount": 10, "from_currency": "USD", "to_currency": "XYZ"},
    )
    assert response.status_code == 400
