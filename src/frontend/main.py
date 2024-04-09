import streamlit as st
import pandas as pd
import requests
import json

st.markdown("""
# Telecom Customer Churn Prediction

Enter customer details to predict churn probability
""")

st.sidebar.header("Customer Details:")
SeniorCitizen = st.sidebar.number_input("Senior Citizen (0 or 1)", min_value=0, max_value=1, value=0)
tenure = st.sidebar.number_input("Tenure (months)", min_value=0, value=0)
MonthlyCharges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=0.0)
TotalCharges = st.sidebar.number_input("Total Charges", min_value=0.0, value=0.0)
gender_Female = st.sidebar.checkbox("Gender: Female")
gender_Male = st.sidebar.checkbox("Gender: Male")
Partner_No = st.sidebar.checkbox("No Partner")
Partner_Yes = st.sidebar.checkbox("Has Partner")
Dependents_No = st.sidebar.checkbox("No Dependents")
Dependents_Yes = st.sidebar.checkbox("Has Dependents")
PhoneService_No = st.sidebar.checkbox("No Phone Service")
PhoneService_Yes = st.sidebar.checkbox("Has Phone Service")
MultipleLines_No = st.sidebar.checkbox("No Multiple Lines")
MultipleLines_No_phone = st.sidebar.checkbox("No Phone Service for Multiple Lines")
MultipleLines_Yes = st.sidebar.checkbox("Has Multiple Lines")
InternetService_DSL = st.sidebar.checkbox("Internet Service: DSL")
InternetService_Fiber_optic = st.sidebar.checkbox("Internet Service: Fiber Optic")
InternetService_No = st.sidebar.checkbox("No Internet Service")
OnlineSecurity_No = st.sidebar.checkbox("No Online Security")
OnlineSecurity_No_internet_service = st.sidebar.checkbox("No Internet Service for Online Security")
OnlineSecurity_Yes = st.sidebar.checkbox("Has Online Security")
# Add other parameters as needed

dict_input = {
    "SeniorCitizen": SeniorCitizen,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "gender_Female": gender_Female,
    "gender_Male": gender_Male,
    "Partner_No": Partner_No,
    "Partner_Yes": Partner_Yes,
    "Dependents_No": Dependents_No,
    "Dependents_Yes": Dependents_Yes,
    "PhoneService_No": PhoneService_No,
    "PhoneService_Yes": PhoneService_Yes,
    "MultipleLines_No": MultipleLines_No,
    "MultipleLines_No_phone": MultipleLines_No_phone,
    "MultipleLines_Yes": MultipleLines_Yes,
    "InternetService_DSL": InternetService_DSL,
    "InternetService_Fiber_optic": InternetService_Fiber_optic,
    "InternetService_No": InternetService_No,
    "OnlineSecurity_No": OnlineSecurity_No,
    "OnlineSecurity_No_internet_service": OnlineSecurity_No_internet_service,
    "OnlineSecurity_Yes": OnlineSecurity_Yes,
}

df_input = pd.DataFrame(dict_input, index=[0])
st.subheader("Customer Details")
st.write(df_input)


if st.button("predict"):
    url = "http://0.0.0.0:5050/api/v1/classify?api_keys=ChurnModel-2024$*"
    payload = json.dumps(dict_input)

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    st.write("Prediction: ",response.json())

    print(response.text)