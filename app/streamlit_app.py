import streamlit as st
import joblib

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Diabetes Prediction AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------
# LOAD MODEL
# ---------------------------
model = joblib.load("src/diabetes_model.pkl")

# ---------------------------
# HEADER
# ---------------------------
st.title("🧠 Diabetes Prediction")
st.caption("Predict diabetes risk using machine learning based on patient health metrics.")

st.divider()

# ---------------------------
# LAYOUT
# ---------------------------
col1, col2 = st.columns([2,1])

# ===========================
# INPUT SECTION
# ===========================
with col1:

    st.subheader("Patient Health Metrics")
    st.info("Enter patient medical measurements to estimate diabetes risk.")

    c1, c2 = st.columns(2)

    with c1:

        preg = st.number_input(
            "Pregnancies (count)",
            min_value=0,
            step=1,
            help="Total number of pregnancies"
        )

        glucose = st.number_input(
            "Glucose (mg/dL)",
            min_value=0,
            step=1,
            help="Normal fasting glucose: 70–99 mg/dL"
        )

        bp = st.number_input(
            "Blood Pressure (mmHg)",
            min_value=0,
            step=1,
            help="Normal systolic BP: 90–120 mmHg"
        )

        skin = st.number_input(
            "Skin Thickness (mm)",
            min_value=0,
            step=1,
            help="Typical range: 10–50 mm"
        )

    with c2:

        insulin = st.number_input(
            "Insulin (μU/mL)",
            min_value=0,
            step=1,
            help="Typical fasting insulin: 16–166 μU/mL"
        )

        bmi = st.number_input(
            "BMI (kg/m²)",
            min_value=0.0,
            step=0.1,
            help="Healthy BMI: 18.5 – 24.9"
        )

        dpf = st.number_input(
            "Diabetes Pedigree Function (index)",
            min_value=0.0,
            step=0.01,
            help="Genetic diabetes likelihood indicator"
        )

        age = st.number_input(
            "Age (years)",
            min_value=0,
            step=1
        )

    st.write("")
    
    # ===========================
    # PREDICTION BUTTON
    # ===========================
    if st.button("Predict Diabetes Risk"):

        data = [[preg, glucose, bp, skin, insulin, bmi, dpf, age]]

        probability = model.predict_proba(data)[0][1] * 100

        confidence = max(model.predict_proba(data)[0]) * 100

        st.divider()
        st.subheader("Prediction Result")

        if probability < 30:
            st.success(f"🟢 Low Diabetes Risk\n\nProbability: {probability:.2f}%")

        elif probability < 60:
            st.warning(f"🟡 Moderate Diabetes Risk\n\nProbability: {probability:.2f}%")

        elif probability < 80:
            st.error(f"🟠 High Diabetes Risk\n\nProbability: {probability:.2f}%")

        else:
            st.error(f"🔴 Very High Diabetes Risk\n\nProbability: {probability:.2f}%")

        st.progress(probability / 100)
        st.write(f"### Risk Score: {probability:.2f}%")
        st.write(f"Model Confidence: {confidence:.2f}%")

# ===========================
# MODEL INFORMATION
# ===========================
with col2:

    st.subheader("Model Information")

    st.metric("Model Used", "Random Forest")
    st.metric("Accuracy", "74%")
    st.metric("AUC Score", "0.82")

    st.divider()

    st.subheader("About the AI Model")

    st.write("""
    This application uses a **Random Forest Machine Learning model**
    to predict diabetes risk based on patient medical measurements.

    The model was trained using supervised learning on historical
    health data to identify patterns associated with diabetes.
    """)

    st.divider()

    st.subheader("About Model")

    st.write(
        """
        This AI model predicts diabetes risk using important health indicators such as:

        • Glucose level  
        • BMI (Body Mass Index)  
        • Insulin level  
        • Age  
        • Diabetes Pedigree Function  

        The model was trained using **Random Forest Classification**
        on the Kaggle Indians Diabetes Dataset**.
        """
    )

    st.divider()

    st.subheader("Dataset Information")

    st.write("""
Dataset: Kaggle Indians Diabetes Dataset**

Number of Samples: **768**

Features Used:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
""")