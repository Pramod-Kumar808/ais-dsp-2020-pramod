# End to End Machine learning.
## This is an college repo and all the practice work is guided by alaa-bakhti (DSP professor)


This tree explain the main files
C:.
├───app
│   ├───inference.py
│   ├───make_submission.py
│   ├───preprocess.py
│   └───train.py
│
├───data
│   ├───Diabetes
│   │   └───diabetes.csv
│   ├───house-prices
│   │   └───test.csv
│   │   └───train.csv
│   └───power-plant
│       └───power_plant.csv
├───models
│   ├───RandomForestRegressor.joblib
│   ├───RandomizedSearchCV.joblib
│   ├───on_hot_encoder.joblib
│   ├───svm.joblib
│   └───diabetes_model.pkl  
├───notebook
│   ├───house-price.ipynb
│   ├───mlfow.ipynb
│   └───power_plant.ipynb   
└───serving
    ├───embedded_model
    │   └───app.py
    └───model_as_a_service
        └───main.py

In this repo i worked in End to End machine learning staring from importing the data to model deployment

# Files and their purpose 

1. app ---- dataset preprocessing
2. data ----- import all required dataset 
3. model ------ selected models training data and deployed for prediction 
4. notebook ------ python files (Codes)
5. serving ------- deployment setup using streamlit and fastapi
