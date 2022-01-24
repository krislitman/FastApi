from fastapi import FastAPI
from models import RandomObject

app = FastAPI()

@app.get("/")
def index():
    object1 = RandomObject("Kris", 1)
    return {
            "Name": object1.name,
            "Number": object1.number
            }
