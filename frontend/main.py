import streamlit as st


from crud_ui import (add_patient_ui,view_patients_ui,update_patient_ui,delete_patient_ui)


st.title(" Health Prediction Application")

#menu = st.sidebar.radio("Select Menu", ["Read (View)", "Create (Add)", "Update (Edit)", "Delete (Remove)"])

st.sidebar.title("Menu")

menu = st.sidebar.selectbox(
    "Select an Option",
    (
        "Dashboard",
        "Add Patient",
        "View Patients",
        "Update Patient",
        "Delete Patient"
    )
)

if menu == "Dashboard":
    st.subheader("Dashboard")
    st.info("""
        Welcome to the Health Prediction Application.

        Use the menu on the left to:

        • Add Patient Records
        • View Existing Patients
        • Update Patient Information
        • Delete Patient Records
        • Predict Health Risks
        """
    )
elif menu == "Add Patient":
    add_patient_ui()

elif menu == "View Patients":
    view_patients_ui()

elif menu == "Update Patient":

    update_patient_ui()

elif menu == "Delete Patient":

    delete_patient_ui()

