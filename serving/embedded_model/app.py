"""
You need to run the app from the root
To run the app
$ streamlit run serving/embedded_model/app.py
"""

import streamlit as st
import requests
import json
import joblib
import numpy as np

model = joblib.load('C:/Users/npram/Desktop/Github/machine-learning-deployment-diabetes/model/diabetes_model.pkl')

def run():
    st.title("Diabetes prediction")
    age = st.text_input("Age of patient", "59")
    if (float(age) <= 0):
        st.warning("Value must be range [1 to 100]")

    sex = st.text_input("Gender", "1")
    if (float(sex) < 0) or (float(sex) > 2):
        st.warning("Mention 2 for Women and 1 for Men")

    bmi = st.text_input("BMI value", "32.1")
    if (float(bmi) < 0):
        st.warning("Please enter the integer values")

    bp = st.text_input("Blood pressure", "101")
    if (float(bp) < 0):
        st.warning("Please enter the integer values")

    s1 = st.text_input("S1 value", "157")
    s2 = st.text_input("S2 value", "92.3")
    s3 = st.text_input("S3 value", "38")
    s4 = st.text_input("S4 value", "4")
    s5 = st.text_input("S5 value", "4.852")
    s6 = st.text_input("S6 value", "87")

    data = {
        "age" : age,
        "sex" : sex,
        "bmi" : bmi,
        "bp" : bp,
        "s1" : s1,
        "s2": s2,
        "s3": s3,
        "s4" : s4,
        "s5" : s5,
        "s6" : s6
    }


    if st.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/Predict", json = data)
        prediction = response.json()
        # model_input_data = np.array([age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]).reshape(1, -1)
        # progression = model.predict(model_input_data)
        # print(type(progression))
        # return progression[0]
        # prediction = model.predict(data)
        st.success(f"The prediction of the model: {prediction}")


if __name__ == '__main__':
    run()