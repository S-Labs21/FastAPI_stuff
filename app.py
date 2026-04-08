from fastapi import FastAPI

app = FastAPI()


@app.get('/') #this is a route decorater, it modifies the function below it
def hello_world():
    return {'Hello':'World'}
