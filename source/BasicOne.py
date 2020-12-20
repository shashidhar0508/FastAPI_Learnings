import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def indexes():
    return {"id": "hello"}


if __name__ == "--main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
