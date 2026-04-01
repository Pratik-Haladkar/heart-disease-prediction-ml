import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("models/model.pkl")

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Prediction System")
st.write("Enter patient details to predict risk")

# --- INPUTS ---
age = st.slider("Age", 20, 80, 40)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox("Chest Pain Type", [
    "Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"
])
cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)

trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 400, 200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs = 1 if fbs == "Yes" else 0

restecg = st.selectbox("Rest ECG", [
    "Normal", "ST-T abnormality", "Left ventricular hypertrophy"
])
restecg = ["Normal", "ST-T abnormality", "Left ventricular hypertrophy"].index(restecg)

thalach = st.number_input("Max Heart Rate", 70, 210, 150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang = 1 if exang == "Yes" else 0

oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0)

slope = st.selectbox("Slope of Peak Exercise", [
    "Upsloping", "Flat", "Downsloping"
])
slope = ["Upsloping", "Flat", "Downsloping"].index(slope)

ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])

thal = st.selectbox("Thalassemia", [
    "Normal", "Fixed Defect", "Reversible Defect"
])
thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

# --- PREDICTION ---
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    result = model.predict(input_data)

    st.subheader("Result:")

    if result[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
        st.write("👉 Please consult a doctor and maintain a healthy lifestyle.")
    else:
        st.success("✅ Low Risk of Heart Disease")
        st.write("👉 Keep maintaining a healthy lifestyle!")