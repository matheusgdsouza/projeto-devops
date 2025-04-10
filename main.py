from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def root():
    return {"teste": True, "Numero aleatorioo": random.randint(1, 100)}