from datetime import date
import streamlit as st
import pandas as pd
import requests
import re

# from backend.prediction import predict_health

API_URL = "http://127.0.0.1:8000"


def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(re.match(pattern, email))


# Create operation

def add_patient_ui():
    st.subheader("Add Patient")
    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        dob = st.date_input("Date of Birth", max_value=date.today())
        email = st.text_input("Email Address")

    with col2:
        glucose = st.number_input("Glucose", min_value=0.0)
        haemoglobin = st.number_input("Haemoglobin", min_value=0.0)
        cholesterol = st.number_input("Cholesterol", min_value=0.0)

    if st.button("Save Patient"):

        if not full_name:
            st.error("Full Name is required")
            return

        if not validate_email(email):
            st.error("Invalid Email")
            return

        # remarks = predict_health(
        #     glucose,
        #     haemoglobin,
        #     cholesterol
        # )

        payload = {
            "full_name": full_name,
            "dob": str(dob),
            "email": email,
            "glucose": glucose,
            "haemoglobin": haemoglobin,
            "cholesterol": cholesterol,
        }
        try:

            response = requests.post(
                f"{API_URL}/patients",
                json=payload
            )

            if response.status_code == 200:

                result = response.json()
                st.success( result["message"] )

                st.text_area( "Predicted Risk", value=result["remarks"], disabled=True )

            else:

                st.error(response.text)

        except Exception as e:
            st.error(f"Connection Error: {e}")

# Read

def view_patients_ui():
    st.subheader("Patient Records")

    try:
        response = requests.get(f"{API_URL}/patients")

        if response.status_code == 200:
            patients = response.json()
            if patients:
                df = pd.DataFrame(patients)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No patient records found.")
        else:
            st.error("Unable to fetch records.")

    except Exception as e:
        st.error(f"Connection Error: {e}")


# Update

def update_patient_ui():
    st.subheader("Update Patient")

    try:
        response = requests.get(
            f"{API_URL}/patients"
        )

        if response.status_code != 200:
            st.error("Unable to fetch patients.")
            return

        patients = response.json()

        if not patients:
            st.info("No patient records found.")
            return

        patient = st.selectbox(
            "Select Patient",
            options=patients,
            format_func=lambda p: f"{p['id']} - {p['full_name']}"
        )

        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input(
                "Full Name",
                value=patient["full_name"]
            )

            dob = st.date_input(
                "Date of Birth",
                value=pd.to_datetime(
                    patient["dob"]
                ).date()
            )

            email = st.text_input(
                "Email Address",
                value=patient["email"]
            )

        with col2:
            glucose = st.number_input(
                "Glucose",
                value=float(patient["glucose"])
            )

            haemoglobin = st.number_input(
                "Haemoglobin",
                value=float(patient["haemoglobin"])
            )

            cholesterol = st.number_input(
                "Cholesterol",
                value=float(patient["cholesterol"])
            )

        if st.button("Update Patient"):
            payload = {
                "full_name": full_name,
                "dob": str(dob),
                "email": email,
                "glucose": glucose,
                "haemoglobin": haemoglobin,
                "cholesterol": cholesterol
            }

            response = requests.put(
                f"{API_URL}/patients/{patient['id']}",
                json=payload
            )

            if response.status_code == 200:
                result = response.json()
                st.success(result["message"])
                st.text_area(
                    "Updated Risk",
                    value=result["remarks"],
                    disabled=True
                )
            else:
                st.error(
                    f"Update Failed: {response.text}"
                )

    except Exception as e:
        st.error(f"Connection Error: {e}")


# Delete

def delete_patient_ui():

    st.subheader("Delete Patient")

    response = requests.get(
        f"{API_URL}/patients"
    )

    if response.status_code != 200:

        st.error(
            "Unable to fetch patients"
        )

        return

    patients = response.json()

    if not patients:

        st.warning(
            "No patient records found"
        )

        return

    patient = st.selectbox(
        "Select Patient to Delete",
        options=patients,
        format_func=lambda p:
        f"{p['id']} - {p['full_name']}"
    )

    st.warning(
        "This action cannot be undone."
    )

    confirm = st.checkbox(
        "I confirm deletion"
    )

    if st.button("Delete Patient") and confirm:

        response = requests.delete(
            f"{API_URL}/patients/{patient['id']}"
        )

        if response.status_code == 200:

            st.success(
                "Patient deleted successfully"
            )

        else:

            st.error(
                "Failed to delete patient"
            )