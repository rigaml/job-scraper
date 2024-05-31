from typing import List, Union
from typing_extensions import Annotated
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from enum import Enum

from api.job_response import JobResponse
from services.job_dto import JobDTO
from services.jobs_service import JobsService

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})


@app.get("/")
def health():
    return {"health_check": "OK"}


@app.get("/jobs/", response_model=List[JobResponse])
# def get_jobs(jobs_service=Depends(JobsService), skip: int = 0, limit: int = 10):
# jobs = jobs_service.get_jobs(skip, limit)
def get_jobs(skip: int = 0, limit: int = 10):
    jobs = [JobDTO()]
    return [JobResponse.create_from_dto(job) for job in jobs]


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


class Item(BaseModel):
    name: str
    price: float


@app.post("/models/{model_name}")
async def create_item(model_name: ModelName, item: Item):
    return {(model_name, item.name, item.price)}


@app.get("/items/")
async def read_items(q: Annotated[Union[List[str], None], Query(title="Query string", max_length=30)] = None):
    query_items = {"q": q}
    return query_items
