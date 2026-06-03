import pandas as pd
from joblib import load

model_data = load("../artifacts/model_data.joblib")
model = model_data["model"]
label_encoder = model_data["label_encoder"]
features = model_data["features"]

def predict_health(glucose, haemoglobin, cholesterol):
    if glucose >= 126:
        return "Possible Diabetes Risk"
    input_data = pd.DataFrame([[glucose, haemoglobin, cholesterol]],
        columns=features
    )

    prediction = model.predict(input_data)

    result = label_encoder.inverse_transform(prediction)[0]

    return result
