from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/", json={"name": "Teste", "email": "teste@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário criado com sucesso"}


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert "users" in response.json()
