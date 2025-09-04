import pickle
import pandas as pd
from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()
with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
cols=['gender','SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

@app.get('/')
def extract():
    return "welcome to my project"

@app.post('/predict')
def model(info:list):
    clas = ['no_churn', 'churn']
    test_df = pd.DataFrame(info, columns=cols)
    result = loaded_model.predict(test_df)
    return clas[result]
#python -m uvicorn fast:app --reload