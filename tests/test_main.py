from fastapi.testclient import TestClient

from dbasik_api.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
