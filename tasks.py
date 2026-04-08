from fastapi import FastAPI
import asyncio

app = FastAPI()

async def task1():
    print("Task 1 starts")
    await asyncio.sleep(3)
    print("Task 1 ends")
    return "Task1 done"

async def task2():
    print("Task 2 starts")
    await asyncio.sleep(1)
    print("Task 2 ends")
    return "Task2 done"

@app.get('/')
async def run_tasks():
    results = await asyncio.gather(task1(), task2())
    return {"Results" : results}