from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get('/')
def home():
    return {"message":"ML API is running"}

@app.get('/predict')
def predict(hours : float):
    input_data = np.array([[hours]])

    prediction = model.predict(input_data)

    return {
        "hours" : hours,
        "predicted_marks": float(prediction[0])
    }
