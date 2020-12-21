from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = Field(description="Add a description about item")
    cost: float = Field(...,ge=15000.0, le=300000.0)
    tax: float = Field(...,le=15000)
    # By adding Field for above values we can show the above validations in schema of docs


@app.post("/pydantic_fields")
def pydantic_field(items: Item = Body(..., embed=True, example={
      "items": {
        "name": "sony 7s III pro",
        "description": "Full-frame movie performance including high sensitivity",
        "cost": 296990,
        "tax": 13000
      }
    }, )):
    """
    We can see the above example as Example value in docs
    """
    return {"items": items}
