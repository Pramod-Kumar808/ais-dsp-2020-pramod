from re import T
import pandas as pd
import joblib
import streamlit as st
from PIL import Image
from streamlit.proto.DataFrame_pb2 import DataFrame

st.title("My first machine learning application")

uploaded_file = st.file_uploader("choose an image")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="upload an image", use_column_width=True)

csv_file = st.file_uploader("Choose csv file")
if csv_file is not None:
    st.write("filename: ", csv_file.name)
    Dataframe = pd.read_csv(csv_file)
    st.write(Dataframe)

user_input = st.text_input("label goes here", "Type")
print(user_input)

def inference(data, model_path=None, model=None):
    # https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    # for caching data: https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html
    if model_path:
        model = joblib.load(model_path)
    return model.predict(data)


# Model prediction
if st.button('Predict diabetes progression'):
    if csv_file:
        # dataframe = pd.read_csv(csv_file)
        predictions = model.predict(dataframe)
        st.success(f'Predictions : {predictions}')
    else:
        st.warning('You need to upload a CSV file')