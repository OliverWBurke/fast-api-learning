from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_root_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_main_root_post():
    response = client.post("/")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
