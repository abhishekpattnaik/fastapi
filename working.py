from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    item: Optional[str] = None

app = FastAPI()

@app.get(path="/sample")
def home():
    return {"Data": "Test"}

inventory = {
    1:{
        "name":"Milk",
        "price":3.99,
        "item":"regular"
    }
}

@app.get(path="/get-item/{item_id}")
def get_info(item_id:int):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(*, name:Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"data": "not_found"}

@app.post("/create_item/{item_id}")
def create_item(item_id: int, item:Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = {
        "name": item.name,
        "price": item.price,
        "item": item.item
    }
    return {"data":None}