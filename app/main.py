from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class TextIn(BaseModel):
    text: str

class TextOut(BaseModel):
    out: str

@app.get("/")
def health():
    return {"health_check": "OK"}

@app.post("/predict", response_model=TextOut)
def predict(payload: TextIn):
    return {"out": "Is out"}