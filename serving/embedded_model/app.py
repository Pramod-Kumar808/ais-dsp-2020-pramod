"""
You need to run the app from the root
To run the app
$ streamlit run serving/embedded_model/app.py
"""

import streamlit as st
import requests
from requests.api import request
import json
import joblib
import pandas as pd
from PIL import Image

model = joblib.load('C:/Users/npram/Desktop/EPITA/CLASS and NOTES/SEM2/Data_science_production/dsp-correction/models/diabetes_model.pkl')

st.header("Diabetes Prediction for multiple patient")
st.subheader("Please entre the inputs for Prediction....!")
# st.set_page_config(page_icon= "https://image.shutterstock.com/image-photo/overt-diabetes-you-yes-no-260nw-1187847934.jpg",)

st.text("Upload your Patient data for the prediction......:)")

#Uploading the csv file
file = st.file_uploader("Upload the file")
if file:
    st.write("Filename ", file.name)
    dataframe = pd.read_csv(file, sep="\t")
    st.write(dataframe)

#User inputs
def run():
    st.sidebar.title("Diabetes prediction for a single Patient")
    age = st.sidebar.text_input("Age in years", "59")
    if (float(age) < 0) or (float(age) > 100):
        st.sidebar.warning("Your not immortal, Please re-enter")

    sex = st.sidebar.text_input("Gender", "1")
    if (float(sex) < 0) or (float(sex) > 2):
        st.sidebar.warning("Mention 2 for Women and 1 for Men")

    bmi = st.sidebar.text_input("BMI value", "32.1")
    if (float(bmi) < 0):
        st.sidebar.warning("Please enter correct values")

    bp = st.sidebar.text_input("Blood pressure", "101")
    if (float(bp) < 0):
        st.sidebar.warning("Please enter correct values")

    s1 = st.sidebar.text_input("S1 value", "157")
    s2 = st.sidebar.text_input("S2 value", "92.3")
    s3 = st.sidebar.text_input("S3 value", "38")
    s4 = st.sidebar.text_input("S4 value", "4")
    s5 = st.sidebar.text_input("S5 value", "4.852")
    s6 = st.sidebar.text_input("S6 value", "87")
    Y = st.sidebar.text_input("Y", "52")
# '''
#     data = {
#         "age" : age,
#         "sex" : sex,
#         "bmi" : bmi,
#         "bp" : bp,
#         "s1" : s1,
#         "s2": s2,
#         "s3": s3,
#         "s4" : s4,
#         "s5" : s5,
#         "s6" : s6
#     }
# '''
    host = "http://127.0.0.1:8000"
    if st.button("Predict"):
        # response = requests.post("http://127.0.0.1:8000/Predict", json = data)
        # prediction = response.json()
        if file:
            data = dataframe.to_json(orient = "records")
            connect = f"{host}/Prediction_file"
            data = data.lower()
            predictions = requests.post(connect, data = data, headers={'Content-Type': 'application/json'}) 
            print(predictions.text)
            predictions = json.loads(json.loads(predictions.text))
            print(type(predictions))
            for i in range(5):
                for j in predictions:
                    st.info(f"Patient {i} results: {predictions[j]}" )
        else:
            "Please upload the data"

    
    if st.sidebar.button("Prediction"):
        st.info("Prediction from the database")
        # st.sidebar.success(f"Result of Patient: {predictions}")
        connect = f"{host}/Prediction?age={age}&sex={sex}&bmi={bmi}&bp={bp}&s1={s1}&s2={s2}&s3={s3}&s4={s4}&s5={s5}&s6={s6}"
        predictions = requests.post(connect)
        st.info(f"Patient Prediction: {predictions.text}")
    else:
        print("Please fill the user inputs...!")

if __name__ == '__main__':
    run()