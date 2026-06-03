import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="health_prediction_db"
    )
#Create
def add_patient(full_name, dob, email, glucose, haemoglobin, cholesterol, remarks):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO patients
    (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )
    )

    conn.commit()
    cursor.close()
    conn.close()

# Read
def get_patients():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients

# Update
def update_patient(
    patient_id,
    full_name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE patients
    SET
        full_name=%s,
        dob=%s,
        email=%s,
        glucose=%s,
        haemoglobin=%s,
        cholesterol=%s,
        remarks=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks,
            patient_id
        )
    )

    conn.commit()
    cursor.close()
    conn.close()

# Delete
def delete_patient(patient_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=%s",
        (patient_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()