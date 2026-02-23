import joblib

# Load saved model
model = joblib.load("diabetes_model.pkl")

# Example patient data
sample = [[2,120,70,20,79,25.0,0.5,30]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Person is likely Diabetic")
else:
    print("Person is Not Diabetic")