import uvicorn
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


@app.get("/items/")
def items(item_id: str = Query(None, max_length=10, min_length=2, regex="^[a-z]+$")):
    """
    Query is used to add validations for parameters.
    """
    return {"id": item_id}


@app.get("/items_list/")
def items_list(item_id: List[str] = Query(["abc", "def", "ghi"])):
    """
    Giving parameter as List allows only List values.
    """
    return {"id": item_id}
