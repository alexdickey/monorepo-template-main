import pytest
from fastapi.testclient import TestClient
from ..src.main import app

client = TestClient(app)

# Test for the "first_api" endpoint
def test_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_worldXXX"}

# Test for the "first_apiV2" endpoint
def test_first_apiV2():
    path_param = "sample_path_param"
    response = client.get(f"/books/{path_param}")
    assert response.status_code == 200
    assert response.json() == {"msg": path_param}

# Test for the "first_apiV3" endpoint
def test_first_apiV3():
    title = "sample_title"
    response = client.get(f"/books/?title={title}")
    assert response.status_code == 200
    assert response.json() == {"msg": title}

# Test for the "first_apiV5" endpoint
def test_first_apiV5_param():
    path_param = "sample_path_param"
    # title = "sample_title"
    response = client.get(f"/books/{path_param}")
    assert response.status_code == 200
    assert response.json() == {"msg": path_param}

def test_first_apiV5_query():
    # path_param = "sample_path_param"
    title = "sample_title"
    response = client.get(f"/books/?title={title}")
    assert response.status_code == 200
    assert response.json() == {"msg": title}


# Test for the "first_apiV4" endpoint
def test_first_apiV4():
    new_book = {"title": "New Book", "author": "Author"}
    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"msg": new_book}

# Test for the "update_item" endpoint when  item is present
def test_update_item_item_exists():
    item_id = 1
    updated_item = "Updated Item"
    response = client.put(f"/items/{item_id}", json=updated_item)
    assert response.status_code == 200
    assert response.json() == {"message": "Item updated successfully"}

# Test for the "update_item" endpoint when not present
def test_update_item_not_present():
    item_id = 30
    updated_item = "Updated Item"
    response = client.put(f"/items/{item_id}", json=updated_item)
    assert response.status_code == 200
    assert response.json() == {"message": "Item not found"}

# Test for the "delete_item" endpoint
def test_delete_item():
    item_id = 1
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}

# Test for the "delete_item" endpoint with an item that doesn't exist
def test_delete_item_not_found():
    item_id = 40
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item not found"}

