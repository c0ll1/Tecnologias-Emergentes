from socket import timeout
from typing import Union
import requests
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
url = 'https://6303b75f0de3cd918b3cc649.mockapi.io/item'

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    headers = {'Content-type': 'application/json','Accept':'application/json'}
    response = requests.put(url+"/"+str(item_id),item.json(), headers=headers)
    return response.json()

@app.post("/items")
def add_item(item: Item):
    headers = {'Content-type': 'application/json','Accept':'application/json'}
    response = requests.post(url,item.json(), headers=headers)
    return response.json()

@app.delete("/items/{item_id}")
def erase_item(item_id: int):
    headers = {'Content-type': 'application/json','Accept':'application/json'}
    response = requests.delete(url+"/"+str(item_id), headers=headers)
    return response.json()
