import os
import joblib

# get current script directory
BASE_DIR = os.path.dirname(__file__)

# model path
model_path = os.path.join(BASE_DIR, "diabetes_model.pkl")

# load model
model = joblib.load(model_path)

# example patient data
sample = [[2,120,70,20,79,25.0,0.5,30]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Person is likely Diabetic")
else:
    print("Person is Not Diabetic")