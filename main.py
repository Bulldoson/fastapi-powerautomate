from typing import Union

from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder


from file import router as FileRouter

app = FastAPI()


app.include_router(FileRouter, tags=["File"], prefix="/file")




@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


