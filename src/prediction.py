import os
import joblib

# Load the trained model

try:
    model_path = os.path.join(os.path.dirname(__file__), "diabetes_model.pkl")
    model = joblib.load(model_path)
except FileNotFoundError:
    print("Model file not found. Make sure diabetes_model.pkl is in the src folder.")
    exit()

# Example patient data
# Order: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
sample = [[2, 120, 70, 20, 79, 25.0, 0.5, 30]]

# Make prediction
prediction = model.predict(sample)

# Display result
if prediction[0] == 1:
    print("Person is likely Diabetic")
else:
    print("Person is Not Diabetic")