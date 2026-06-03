import pandas as pd
import mysql.connector

df = pd.read_csv("health_dataset.csv")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="health_prediction_db"
)

cursor = connection.cursor()

# 2. ADD THIS LINE: Convert your date string column to MySQL's YYYY-MM-DD format
df["Date of Birth"] = pd.to_datetime(df["Date of Birth"], dayfirst=True).dt.strftime('%Y-%m-%d')

create_table_query = """ CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        dob DATE NULL,
        email VARCHAR(255) NULL,
        glucose INT NULL,
        haemoglobin DECIMAL(5,2) NULL,
        cholesterol INT NULL,
        remarks TEXT NULL
    );
    """
cursor.execute(create_table_query)
print(" Table 'patients' verified or successfully created.")


# Iterate through the DataFrame and insert records into the MySQL table
for index, row in df.iterrows():
    cursor.execute(
        """INSERT INTO patients (full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        (row["Full Name"],
        row["Date of Birth"],
        row["Email Address"],
        row["Glucose"],
        row["Haemoglobin"],
        row["Cholesterol"],
        row["Remarks"])
    )

# Commit the transaction
connection.commit()

print("Data imported successfully!")

# Close the connection
cursor.close()
connection.close()