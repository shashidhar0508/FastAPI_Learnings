from typing import List, Set

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class User(BaseModel):
    user_name: str
    mail: str
    phone_no: str


class ItemImage(BaseModel):
    image_name: str
    url: HttpUrl


class Item(BaseModel):
    name: str = Field(None)
    description: str = Field(None, description="Add a description about item")
    cost: float = Field(None, ge=15000.0, le=300000.0)
    tax: float = Field(None, le=20000)
    available_locations: List[str] = Field(None)  # It is the List from typing which takes only specified data type
    used_by: Set[str] = Field(None)  # It is the Set from typing which takes only specified data type
    user: User = None  # Placing User class here, None means User class is optional
    images: List[ItemImage] = None  # Item_Image as list


@app.post("/nested_models")
def nested_models(items: Item = Body(..., embed=True)):
    """
    We can see the above example as Example value in docs
    """
    return {"items": items}
