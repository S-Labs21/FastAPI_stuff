from fastapi import FastAPI
import asyncio


app = FastAPI()


@app.get('/')
async def home():
    await asyncio.sleep(4)
    return {"message":"NA1SS"}

@app.get('/calculate/{data}')
def calc(data : int):
    return {"results": data ** 2}


    