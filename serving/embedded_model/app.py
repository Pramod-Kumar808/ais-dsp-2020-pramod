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
import urllib.request

urllib.request.urlretrieve(
  'https://0901.static.prezi.com/preview/v2/rfpe76g53rtio7k4dui7yfhwex6jc3sachvcdoaizecfr3dnitcq_3_0.png',
   "gfg.png")

# from app import about
from PIL import Image
st.markdown("<h1 style='text-align: center; color: green;'>EARLY DIABETES DETECTION</h1>", unsafe_allow_html=True)
image = Image.open('gfg.png')
st.sidebar.title("Diabetes Detection")
st.sidebar.success("Dibetes Prediction with The power of **Artificial Intelligence**!")
st.sidebar.image(image, width=250)
st.sidebar.subheader('The diabetes dataset:')
st.sidebar.write("[https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)")
    
# app_add.add_app("About-Diabetes", about.app_add)


model = joblib.load('C:/Users/npram/Desktop/Github/ais-dsp-2020-pramod/models/diabetes_model.pkl')


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
st.warning("This is only for study purpose.....! The prediction are not accurate and not validated by any of them....! This prediction gives the score and For every prediction its says your safe...!")
host = "http://127.0.0.1:8000"

#User inputs
def run():
    st.title("User input diabetes prediction for single patient")
    age = st.text_input("Age in years", "59")
    if (float(age) < 0) or (float(age) > 100):
        st.warning("Your not immortal, Please re-enter")

    sex = st.text_input("Gender", "1")
    if (float(sex) < 0) or (float(sex) > 2):
        st.warning("Mention 2 for Women and 1 for Men")

    bmi = st.text_input("BMI value in (weight in kg/(height in m)^2)", "32.1")
    if (float(bmi) < 0) or (bmi == None):
        st.warning("Please enter correct values")

    bp = st.text_input("Blood pressure in (mm Hg)", "101")
    if (float(bp) < 0) or (bp == None):
        st.warning("Please enter correct values")

    s1 = st.slider("S1 value", 0, 200, 150, 1)
    s2 = st.slider("S2 value", 0, 200, 93, 1)
    s3 = st.slider("S3 value", 0, 200, 38, 1)
    s4 = st.slider("S4 value", 0, 200, 4, 1)
    s5 = st.slider("S5 value", 0, 200, 4, 1)
    s6 = st.slider("S6 value", 0, 200, 87, 1)
    Y = st.slider("Y value", 0, 200, 151, 1)
# '''#     data = {
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
     # Run code for the user input
    if st.button("Singe Predict"):
        st.info("Prediction for Single patient from the User input")
        # st.success(f"Result of Patient: {predictions}")
        connect = f"{host}/Prediction?age={age}&sex={sex}&bmi={bmi}&bp={bp}&s1={s1}&s2={s2}&s3={s3}&s4={s4}&s5={s5}&s6={s6}"
        predictions = requests.post(connect)
        st.info(f"Patient Prediction: {predictions.text}")
        st.success("""# Congratulations . 
            Based on your responses, we believe that you are not at a risk of being diabetic at present. Staying safe and engaging in a healthy lifestyle are proactive measures that keep diabetes at bay! """)
        st.balloons()
        st.markdown(
            """
            ## Prevention
            Simple lifestyle measures have been shown to be effective in preventing or delaying the onset of type 2 diabetes. To help prevent type 2 diabetes and its complications, people should:
            * achieve and maintain a healthy body weight;
            * be physically active – doing at least 30 minutes of regular, moderate-intensity activity on most days. More activity is required for weight control;
            * eat a healthy diet, avoiding sugar and saturated fats; and
            * avoid tobacco use – smoking increases the risk of diabetes and cardiovascular disease.
            """)
    else:
        print("Please fill the user inputs...!")


    #Uploading the csv file
    file = st.file_uploader("Upload the file")
    if file:
        st.subheader("Dataset View")
        dataframe = pd.read_csv(file, sep="\t")
        st.write(dataframe)

    # Run code thought request post for the csv file
  
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
                    st.success("""# Congratulations . 
            Based on your responses, we believe that you are not at a risk of being diabetic at present. Staying safe and engaging in a healthy lifestyle are proactive measures that keep diabetes at bay! """)
                    st.balloons()
        else:
            st.error("Please upload the data")

    

   

if __name__ == '__main__':
    run()