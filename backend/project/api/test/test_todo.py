from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_get_all_todo():
    response = client.get("/todo/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_todo():
    responce = client.get("/todo/5")
    assert responce.status_code == 200
    assert responce.json()

    responce = client.get("/todo/9999")
    assert responce.status_code == 404

def test_get_user_todo():
    responce = client.get("/todo/users/string")
    assert responce.status_code == 200
    assert responce.json()

    responce = client.get("/todo/users/notfound")
    assert responce.status_code == 404

def test_post_todo():
    response = client.post(
        "/todo/",
        json={"title": "test", 
        "description": "test", 
        "status": "test", 
        "user_name": "test_user"})

    assert response.status_code == 200
    assert response.json()["title"] == "test"

    response = client.post(
        "/todo/",
        json={"title": "test", 
        "description": 2, 
        "status": "test", 
        "user_name": "test_user"})

    assert response.status_code == 200
    
    response = client.post(
        "/todo/",
        json={"title": "test", 
        "description": [2], 
        "status": "test", 
        "user_name": "test_user"})

    assert response.status_code == 422

    response = client.post(
        "/todo/",
        json={"title": "test", 
        "status": "test", 
        "user_name": "test_user"})

    assert response.status_code == 422

def test_update():
    responce = client.put(
        "/todo/5",
        json={
            "title": "string",
            "description": "string",
            "status": "string",
            "user_name": "string"
        })

    assert responce.status_code == 200
    assert responce.json() == "Updated"

    responce = client.put(
        "/todo/999",
        json={
            "title": "string",
            "description": "string",
            "status": "string",
            "user_name": "string"
        })
    
    assert responce.status_code == 404

    responce = client.put(
        "/todo/5",
        json={
            "title": [28382],
            "description": "string",
            "status": "string",
            "user_name": "string"
        })
    
    assert responce.status_code == 422

def test_delete():
#     responce = client.delete("/todo/5")

#     assert responce.status_code == 200

    responce = client.delete("/todo/999")

    assert responce.status_code == 404
