from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_name():
    response = client.get("/api/v1/name", params={"name": "John"})
    assert response.status_code == 200
    assert response.json() == {"name": "John"}


def test_get_name_missing_param():
    response = client.get("/api/v1/name")
    assert response.status_code == 422


def test_get_name_empty_string():
    response = client.get("/api/v1/name", params={"name": ""})
    assert response.status_code == 422
