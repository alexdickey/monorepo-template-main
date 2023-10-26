from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/api")
def first_api():
    return{"msg": "hello_worldXXX"}

# takes input in the path
@app.get("/books/{path_param}")
def first_apitV2(path_param: str):
    return{"msg": path_param}

# query param (?title=)
@app.get("/books/")
def first_apiV3(title: str):
    return{"msg": title}

# path parameter AND query parameter
@app.get("/books/{path_param}")
def first_apiV5(path_param: str, title: str = None):
    return{"path_param": path_param, "query_param": title}

# post
@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    print(new_book)
    return {"msg": new_book}

fake_db = {1: "This is item1",
           2: "This is item2"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: str = Body(...)):
    print(f"Received item_id: {item_id}, item: {item}")
    if item_id in fake_db:
        fake_db[item_id] = item
        return {"message": "Item updated successfully"}
    else:
        return {"message": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"message": "Item deleted successfully"}
    else:
        return {"message": "Item not found"}