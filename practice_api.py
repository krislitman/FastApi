from typing import Optional
from fastapi import FastAPI
from models import RandomObject
from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    description: Optional[str] = None
    age: int
    cute: Optional[bool] = True

app = FastAPI()

@app.get("/")
def root():
    object1 = RandomObject("Kris", 1)
    return {
            "Name": object1.name,
            "Number": object1.number
    }

@app.get("/dogs/{dog_id}")
def read_dog(dog_id: int, q: Optional[str] = None):
    return {
        "dog_id": dog_id,
        "q": q
    }

@app.post("/dogs/")
async def create_dog(dog_id: int, dog: Dog, q: Optional[str] = None):
    result = {
        "dog_id": dog_id,
        **dog.dict()
    }
    if q:
        result.update({"q": q})
    return result
