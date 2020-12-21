from typing import List

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


class Items(BaseModel):
    item_name: str
    item_desc: str
    item_cost: float


@app.post("/items_list/{item_id}")
def items_list(
        *,
        item_id: str = Path(..., max_length=10, min_length=4,
                            regex="^[a-z]+$"),
        item_name: str = Query(..., max_length=20, description="Name of the Item"),
        item: Items,
        locations: List[str],
        cost: float = Path(..., ge=200, le=500)):
    """
    ... => Tells the required field as required.

    Query : item_id is query parameter(If a parameter is singular type(int,str,bool,float ex) and is not defined in
     @app.get()  then it is said to be query parameter.item_name in our function items_list() is query parameter)

    Path : item_name is path parameter(If a parameter is declared in path and also in url calling then it is
    said to be Path Parameter. In our function items_list(), item_id is in get() method and also in items_list()
    function parameters so item_id is said to path parameter.)

    request body: If a parameter is declared and its of Pydantic models type then it is said to request body.
    Example is Items.
    """
    return {"path_parameter": item_id, "query_parameter  ": item_name,
            "request body ": item, "list_type ": locations, "cost": cost}
