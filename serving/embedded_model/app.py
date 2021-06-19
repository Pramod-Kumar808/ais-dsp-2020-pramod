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
import base64

model = joblib.load('C:/Users/npram/Desktop/EPITA/CLASS and NOTES/SEM2/Data_science_production/dsp-correction/models/diabetes_model.pkl')


# Adding an Image 
import streamlit as st
import cv2
import urllib
import urllib.request

# METHOD #1: OpenCV, NumPy, and urllib
from PIL import Image
import urllib.request

URL = 'https://storage.googleapis.com/kaggle-competitions/kaggle/17222/logos/header.png?t=2019-11-10-16-51-29'

with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')
# my_png = cv2.waitKey(0)
st.image(img)

st.header("Diabetes Prediction")
st.subheader("This website will predict the diabetes for Single Patient from the user input and Multiple Patient from the dataset uploaded from the user....!")
# st.set_page_config(page_icon= "https://image.shutterstock.com/image-photo/overt-diabetes-you-yes-no-260nw-1187847934.jpg",)


#Uploading the csv file
file = st.file_uploader("Upload the file")
if file:
    st.subheader("Dataset View")
    dataframe = pd.read_csv(file, sep="\t")
    st.write(dataframe)

#User inputs
def run():
    st.sidebar.title("User input diabetes prediction for single patient")
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

    # Run code thought request post for the csv file
    host = "http://127.0.0.1:8000"
    if st.button("Multiple Prediction"):
        # response = requests.post("http://127.0.0.1:8000/Predict", json = data)
        # prediction = response.json()
        if file:
            data = dataframe.to_json(orient = "records")
            connect = f"{host}/Prediction_file"
            data = data.lower()
            predictions = requests.post(connect, data = data, headers={'Content-Type': 'application/json'}) 
            predictions = json.loads(json.loads(predictions.text))
            for i in range(5):
                for j in predictions:
                    st.info(f"Patient {i} results: {predictions[j]}" )
        else:
            st.error("Please upload the data")

    # Run code for the user input
    if st.sidebar.button("Singe Predict"):
        st.info("Prediction for Single patient from the User input")
        # st.sidebar.success(f"Result of Patient: {predictions}")
        connect = f"{host}/Prediction?age={age}&sex={sex}&bmi={bmi}&bp={bp}&s1={s1}&s2={s2}&s3={s3}&s4={s4}&s5={s5}&s6={s6}"
        predictions = requests.post(connect)
        st.info(f"Patient Prediction: {predictions.text}")
    else:
        print("Please fill the user inputs...!")

if __name__ == '__main__':
    run()