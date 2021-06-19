"""
Note: you need to run the app from the root folder otherwise the models folder will not be found
- To run the app
$ uvicorn serving.model_as_a_service.main:app --reload

- To make a prediction from terminal
$ curl -X 'POST' 'http://127.0.0.1:8000/predict_obj' \
  -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "age": 0, "sex": 0, "bmi": 0, "bp": 0, "s1": 0, "s2": 0, "s3": 0, "s4": 0, "s5": 0, "s6": 0 }'
"""


import uvicorn
import joblib
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

import joblib

patient = []


model = joblib.load('C:/Users/npram/Desktop/Github/machine-learning-deployment-diabetes/model/diabetes_model.pkl')

class Data(BaseModel):
    age : int
    sex : float
    bmi : float
    bp : float
    s1 : float
    s2 : float
    s3 : float
    s4 : float
    s5 : float
    s6 : float


@app.get("/")
@app.get("/home")
def read_home():
    return {"message" : "Welcome to website"}


@app.post("/Predict")
def predict(data : Data):
    data_dict = data.dict()
    data_df = pd.DataFrame.from_dict([data_dict])
    # print(data_df)
    prediction = model.predict(data_df)
    prediction_label = ["Patient is healthy" if result == 0 else "Patient need dialysis" for result in prediction]
    return prediction_label

if __name__ == '__main__':
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)

