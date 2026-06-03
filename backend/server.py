from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI, HTTPException

from db_crud import (
    add_patient,
    get_patients,
    update_patient,
    delete_patient
)

app = FastAPI()

from prediction import predict_health

class Patient(BaseModel):
    full_name: str
    dob: date
    email: str
    glucose: float
    haemoglobin: float
    cholesterol: float

@app.get("/")
def home():
    return {
        "message": "Health Prediction API is running"
    }

# Create
@app.post("/patients")
def create_patient(patient: Patient):

    remarks = predict_health(patient.glucose, patient.haemoglobin, patient.cholesterol)
    add_patient(patient.full_name, patient.dob, patient.email, patient.glucose, patient.haemoglobin, patient.cholesterol,remarks)
    return {
        "message": "Patient added successfully",
        "remarks": remarks
    }
# Retrieve
@app.get("/patients")
def read_patients():
    patients = get_patients()
    return patients

@app.get("/patients/{patient_id}")
def read_patient(patient_id: int):
    patients = get_patients()
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )
# Update
@app.put("/patients/{patient_id}")
def update_patient_record(
    patient_id: int,
    patient: Patient
):

    remarks = predict_health(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )
    update_patient(patient_id, patient.full_name,
        patient.dob,
        patient.email,
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol,
        remarks)
    return {
        "message": "Patient updated successfully",
        "remarks": remarks
    }

# Delete
@app.delete("/patients/{patient_id}")
def delete_patient_record(patient_id: int):
    delete_patient(patient_id)

    return {
        "message": "Patient deleted successfully"
    }
