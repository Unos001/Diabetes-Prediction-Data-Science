# Diabetes Prediction using Machine Learning

## 📌 Project Overview
This project predicts whether a person is diabetic using medical data such as Glucose level, BMI, Age, Blood Pressure, etc.  
The goal is early detection of diabetes using Machine Learning (ML – Machine Learning).

---

## 📊 Dataset
Dataset used: **Kaggle Indians Diabetes Datasetset**

Features:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI (Body Mass Index)
- DiabetesPedigreeFunction
- Age

Target:
- Outcome (0 = Non-diabetic, 1 = Diabetic)

---

## 🛠️ Tools & Libraries
- Python
- Pandas (Python Data Analysis Library)
- NumPy (Numerical Python Library)
- Matplotlib & Seaborn
- Scikit-learn (Machine Learning Library)
- Joblib

---

## ⚙️ Steps Performed
1. Data Cleaning
2. Exploratory Data Analysis (EDA – Exploratory Data Analysis)
3. Train-Test Split
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Feature Importance Analysis
8. Model Saving

---

## 🤖 Models Used
- Logistic Regression
- Decision Tree
- Random Forest

---

## 📈 Final Result
Random Forest achieved **75.3% accuracy** and was selected as final model.

Feature importance showed **Glucose, BMI, and Age** as most important factors.

---

## ▶️ How to Run

1. Install requirements:

Run -
python src/predict.py