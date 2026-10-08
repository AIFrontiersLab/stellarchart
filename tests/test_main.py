import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_startup():
    res = client.get("/openapi.json")
    assert res.status_code == 200

def test_happy_path():
    res = client.post("/analyze", json={"text": "Hello World", "language": "en"})
    assert res.status_code == 200
    data = res.json()
    assert data["word_count"] == 2
    assert data["language"] == "en"

def test_invalid_payload():
    res = client.post("/analyze", json={})
    assert res.status_code == 422

def test_empty_text():
    res = client.post("/analyze", json={"text": "   "})
    assert res.status_code == 422

def test_missing_text_field():
    res = client.post("/analyze", json={"language": "en"})
    assert res.status_code == 422
