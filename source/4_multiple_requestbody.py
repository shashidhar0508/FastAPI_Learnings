from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Items(BaseModel):
    item_name: str
    item_desc: str
    item_cost: float


class User(BaseModel):
    user_name: str
    user_skill: list
    user_salary: float


@app.post("/user_items/{item_id}")
def user_items(item_id: int, items: Items, user: User, age: int):
    """
    For handling multiple request bodies
    :param item_id: path parameter
    :param items: request body
    :param user: request body
    :param age: query parameter
    """
    return {"item id": item_id, "items": items, "users": user, "age": age}


@app.post("/user_items1/{item_id}")
def user_items1(item_id: int, items: Items, user: User, age: int = Body(...)):
    """
    In this function age will be added in request body instead of individual parameter
    :param item_id: path parameter
    :param items: request body
    :param user: request body
    :param age: request body
    Example:
        {
          "items": {
            "item_name": "string",
            "item_desc": "string",
            "item_cost": 0
          },
          "user": {
            "user_name": "string",
            "user_skill": [
              "abc","deg","gsd"
            ],
            "user_salary": 0
          },
          "age": 0
        }
    """
    return {"item id": item_id, "items": items, "users": user, "age": age}


@app.post("/single_item")
def single_item(items: Items = Body(..., embed=True)):
    """
    Here the complete items body will be a value for Items key
    Like one key items having complete Items as one value, where Items also has key value pairs
    Example :
        {
          "items": {
            "item_name": "sony camera",
            "item_desc": "sony 7",
            "item_cost": 160000
          }
        }
    """
    return {"items": items}
