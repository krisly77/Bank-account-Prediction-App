import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.linear_model import LogisticRegression

# Loading the Model
with open('/Users/MY LAPTOP/Desktop/Vs Code Intro/SL/Streamlit Checkpoint 1.pkl', 'rb') as file:
    LRmodel = pickle.load(file)

st.title("Telecom Client Churn Predictor")
st.write("Enter client information below:")

# Form container
with st.form("churn_form"):
    
    # Numeric input fields
    TENURE = st.number_input("TENURE (Duration in the Network)", min_value=0.0)
    MONTANT = st.number_input("MONTANT (Top-up Amount)", min_value=0.0)
    REVENUE = st.number_input("REVENUE (Monthly Income)", min_value=0.0)
    ARPU_SEGMENT = st.number_input("ARPU_SEGMENT (90-day avg income / 3)", min_value=0.0)
    FREQUENCE_RECH = st.number_input("FREQUENCE_RECH (Number of Recharges)", min_value=0)
    DATA_VOLUME = st.number_input("DATA_VOLUME (Data Usage)", min_value=0.0)
    REGULARITY = st.number_input("REGULARITY (Active Days in 90 days)", min_value=0)
    FREQ_TOP_PACK = st.number_input("FREQ_TOP_PACK (Times Activated Top Pack)", min_value=0)


    # Validation button
    submit = st.form_submit_button("Validate")

if submit:

    # Put all inputs into an array
    features = np.array([[TENURE, MONTANT, REVENUE, ARPU_SEGMENT, FREQUENCE_RECH, DATA_VOLUME, REGULARITY, FREQ_TOP_PACK]])

    # Make prediction
    prediction = LRmodel.predict(features)[0]

    if prediction == 1:
        st.error("The customer is likely to CHURN.")
    else:
        st.success("The customer is NOT likely to CHURN.")
    