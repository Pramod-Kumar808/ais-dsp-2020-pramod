"""
Note: you need to run the app from the root folder otherwise the models folder will not be found
- To run the app
$ uvicorn serving.model_as_a_service.main:app --reload

- To make a prediction from terminal
$ curl -X 'POST' 'http://127.0.0.1:8000/predict_obj' \
  -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "age": 0, "sex": 0, "bmi": 0, "bp": 0, "s1": 0, "s2": 0, "s3": 0, "s4": 0, "s5": 0, "s6": 0 }'
"""


from textwrap import indent
import uvicorn
import joblib
import json
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from typing import List

app = FastAPI()

import joblib

patient = []


model = joblib.load('C:/Users/npram/Desktop/EPITA/CLASS and NOTES/SEM2/Data_science_production/dsp-correction/models/diabetes_model.pkl')

class DiabetesInfo(BaseModel):
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


@app.post("/Prediction")
async def predict_diabetes_progresss(age: float, sex: float, bmi: float,bp: float, s1: float, s2: float, s3:float, s4: float, s5: float, s6: float):
    print(age, sex, bmi, bp, s1, s2, s3, s4, s5, s6)
    model_input_data = np.array(
        [age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]).reshape(1, -1)
    progression = model.predict(model_input_data)
    # print(type(progression))
    print(f"model input {model_input_data}")
    return progression[0]

@app.post("/Prediction_file")
async def predict_diabetes_progresss(patients: List[DiabetesInfo]):
    result_list = {}
    for i, self in  enumerate(patients):
        input_in_list = np.array([self.age, self.sex, self.bmi, self.bp, self.s1, self.s2, self.s3, self.s4, self.s5, self.s6])
        input_in_list_reshape = input_in_list.reshape(1, -1)
        result_list[str(i)] = float(model.predict(input_in_list_reshape))
        output = json.dumps(result_list)
        return output
# def predict(data : Data):
#     data_dict = data.dict()
#     data_df = pd.DataFrame.from_dict([data_dict])
#     # print(data_df)
#     prediction = model.predict(data_df)
#     prediction_label = ["Patient is healthy" if result == 0 else "Patient need dialysis" for result in prediction]
#     return prediction_label

# if __name__ == '__main__':
#     uvicorn.run("main:api", host="127.0.0.1", port=5000, reload=True)

