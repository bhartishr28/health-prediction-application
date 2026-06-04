# 🏥 Health Prediction Application

## Overview

The Health Prediction Application is a full-stack health Prediction system developed using **Streamlit**, **FastAPI**, **MySQL**, and **Machine Learning**. The application enables users to manage patient records through complete CRUD (Create, Read, Update, Delete) operations and predict potential health risks based on patient health details such as Glucose, Haemoglobin, and Cholesterol levels.

## Demo Video

🎥 Watch the Demo: https://drive.google.com/file/d/1P-IIxLecmGSZoT1-0TD_hnSrL2Ivu8-i/view?usp=drive_link

### Patient Information Required

To generate a health risk prediction, users must provide the following patient details:

* Full Name
* Date of Birth
* Email Address
* Glucose Level
* Haemoglobin Level
* Cholesterol Level

After validating the inputs, the application processes the health metrics through a Machine Learning model and generates a predicted health risk, which is automatically displayed and stored in the **Remarks** field.

The project demonstrates frontend-backend integration, REST API development, database management, data validation, and machine learning model deployment in a production-style architecture.

---

## Key Features

### Patient Record Management (CRUD)

The application supports complete patient data management:

* Create new patient records
* View all patient records
* Update existing patient information
* Delete patient records

All operations are performed through an intuitive Streamlit user interface and processed via FastAPI endpoints.

---

### Health Risk Prediction

Once valid patient information is submitted, the system:

1. Validates the input data
2. Sends the request to the FastAPI backend
3. Uses a Machine Learning model to predict potential health risks
4. Stores the prediction result in the database
5. Displays the prediction in the **Remarks** field

Example predictions include:

* Possible Diabetes Risk
* Healthy
* Other risk categories based on the trained model

---

### Input Validation

The application performs validation before data submission:

* Full Name cannot be empty
* Email must be in a valid format
* Date of Birth cannot be a future date
* Glucose must be numeric and positive
* Haemoglobin must be numeric and positive
* Cholesterol must be numeric and positive

This helps maintain data quality and consistency.

---

### Persistent Storage

Patient records are stored in a MySQL database, ensuring:

* Data persistence
* Reliable retrieval
* Update and deletion capabilities
* Scalability for future enhancements

---

## Technology Stack

### Frontend

* Streamlit
* Pandas
* Requests

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Database

* MySQL

### Machine Learning

* Scikit-Learn
* Joblib
* Pandas

---

## System Architecture

```text
┌─────────────────┐
│    Streamlit    │
│    Frontend     │
└────────┬────────┘
         │ HTTP Requests
         ▼
┌─────────────────┐
│     FastAPI     │
│     Backend     │
└────────┬────────┘
         │
 ┌───────┴────────┐
 ▼                ▼
MySQL       ML Prediction
Database        Model
```

---

## Project Structure

```text
health-prediction-app/
│
├── backend/
│   ├── server.py
│   ├── db_crud.py
│   └── prediction.py
│
├── frontend/
│   ├── main.py
│   └── crud_ui.py
│
├── artifacts/
│   └── model_data.joblib
│
├── requirements.txt
│
└── README.md
```

---

## Database Schema

### Patients Table

| Column      | Type              |
| ----------- | ----------------- |
| id          | INT (Primary Key) |
| full_name   | VARCHAR           |
| dob         | DATE              |
| email       | VARCHAR           |
| glucose     | FLOAT             |
| haemoglobin | FLOAT             |
| cholesterol | FLOAT             |
| remarks     | VARCHAR           |

---

## API Endpoints

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /patients      | Create Patient         |
| GET    | /patients      | Retrieve All Patients  |
| GET    | /patients/{id} | Retrieve Patient by ID |
| PUT    | /patients/{id} | Update Patient         |
| DELETE | /patients/{id} | Delete Patient         |

FastAPI automatically generates API documentation through Swagger UI.

```text
http://127.0.0.1:8000/docs
```

---

## Running the Application

### 1. Start FastAPI Backend

```bash
cd backend

uvicorn server:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### 2. Start Streamlit Frontend

```bash
cd frontend

streamlit run main.py
```

---

## Machine Learning Workflow

Input Features:

* Glucose
* Haemoglobin
* Cholesterol

Prediction Flow:

1. User enters patient details
2. Frontend sends request to FastAPI
3. FastAPI invokes prediction service
4. Machine Learning model generates risk prediction
5. Prediction is stored in database
6. Result is displayed in the UI

---

## Requirements Fulfilled

### CRUD Operations

✔ Create patient records

✔ Read patient records

✔ Update patient records

✔ Delete patient records

---

### User Interface

✔ Clean Streamlit-based interface

✔ Sidebar navigation

✔ Easy-to-use forms

✔ Responsive data tables

---

### Data Validation

✔ Email validation

✔ Date validation

✔ Numeric value validation

✔ Mandatory field checks

---

### Persistent Storage

✔ MySQL database integration

✔ Data persistence across sessions

---

### AI/ML Integration

✔ Machine Learning model integration

✔ Automated health risk prediction

✔ Prediction results stored as remarks

---

## Skills Demonstrated

* Full Stack Development
* REST API Development
* Machine Learning Deployment
* Data Validation
* Database Design
* CRUD Operations
* Frontend-Backend Integration
* Software Architecture
* Python Development
* Healthcare Data Processing

---

## Future Enhancements

* User Authentication & Authorization
* Duplicate Email Prevention
* Search and Filter Functionality
* Dashboard Analytics
* Docker Deployment
* Cloud Deployment (AWS/Azure/GCP)
* Role-Based Access Control
* Model Monitoring and Retraining

---

## Note
The dataset used in this project is synthetic and was generated for demonstration and learning purposes only. No real patient data was used.

## Author

**Bharti Kumari**

Aspiring Data Scientist | Machine Learning & Generative AI Enthusiast

### Areas of Interest

* Data Science
* Machine Learning
* Generative AI
* Predictive Analytics
* Healthcare Analytics
* Credit Risk Analytics
