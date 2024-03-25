#Api para llamar el modelo y generar predicciones
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyQuery, APIKey
from starlette.status import HTTP_403_FORBIDDEN
import uvicorn
import pickle
from pydantic import BaseModel

#Body parameter estructura
class FeaturesModel(BaseModel):
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender_Female: bool
    gender_Male: bool
    Partner_No: bool
    Partner_Yes: bool
    Dependents_No: bool
    Dependents_Yes: bool
    PhoneService_No: bool
    PhoneService_Yes: bool
    MultipleLines_No: bool
    MultipleLines_No_phone: bool
    service: bool
    MultipleLines_Yes: bool
    InternetService_DSL: bool
    InternetService_Fiber_optic: bool
    InternetService_No: bool
    OnlineSecurity_No: bool
    OnlineSecurity_No_internet_service: bool
    OnlineSecurity_Yes: bool
    OnlineBackup_No: bool
    OnlineBackup_No_internet_service: bool
    OnlineBackup_Yes: bool
    DeviceProtection_No: bool
    DeviceProtection_No_internet_service: bool
    DeviceProtection_Yes: bool
    TechSupport_No: bool
    TechSupport_No_internet_service: bool
    TechSupport_Yes: bool
    StreamingTV_No: bool
    StreamingTV_No_internet_service: bool
    StreamingTV_Yes: bool
    StreamingMovies_No: bool
    StreamingMovies_No_internet_service: bool
    StreamingMovies_Yes: bool
    Contract_Month_to_month: bool
    Contract_One_year: bool
    Contract_Two_year: bool
    PaperlessBilling_No: bool
    PaperlessBilling_Yes: bool
    PaymentMethod_Bank_transfer: bool
    PaymentMethod_Credit_card: bool
    PaymentMethod_Electronic_check: bool
    PaymentMethod_Mailed_check: bool


app= FastAPI()

API_KEY = "ChurnModel-2024$*"
API_KEY_NAME = "api_keys"

#Funcion que valida la key
api_key_query = APIKeyQuery(name =API_KEY_NAME, auto_error=False)

#Validar que coincida con el mismo nombre
def get_api_key(api_key_query: str = Security(api_key_query)):
    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

#Al iniciar la API carga el modelo
@app.on_event("startup")
def load_model():
    global model1
    with open("../../model/model.pickle", "rb") as openfile: #te sales 2 niveles
        model1 = pickle.load(openfile)

#Endpoint
@app.get("/api/v1/classify")
def classify(features_model: FeaturesModel, api_key : APIKey=Depends(get_api_key)):
    #Lista de valores que estamos trayendo den bodyrequest
    features = [val for val in features_model.__dict__.values()][:-1]

    prediction = model1.predict([features])

    label_dict= {
        0: "Not churn",
        1: "Churn"
    }

    return {'prediction': label_dict[int(prediction[0])]}


@app.get("/home")
def home(api_key : APIKey=Depends(get_api_key)):
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run('api:app', host='0.0.0.0', port=5050, log_level='info', reload=True)

