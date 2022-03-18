from fastapi.testclient import TestClient

from dbasik.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
