import streamlit as st
import joblib
import os

# Load model
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "../src/diabetes_model.pkl")
model = joblib.load(model_path)

st.set_page_config(page_title="Diabetes Prediction", page_icon="🧠")

st.title("🧠 Diabetes Prediction System")
st.write("Enter patient health information to predict diabetes risk.")

st.divider()

# Input layout
col1, col2 = st.columns(2)

with col1:
    preg = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose", min_value=0)
    bp = st.number_input("Blood Pressure", min_value=0)
    skin = st.number_input("Skin Thickness", min_value=0)

with col2:
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0)

st.divider()

if st.button("Predict Diabetes Risk"):

    data = [[preg, glucose, bp, skin, insulin, bmi, dpf, age]]

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠ High Diabetes Risk ({probability:.2f})")
    else:
        st.success(f"✅ Low Diabetes Risk ({probability:.2f})")