import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Diabetes Progression Predictor", layout="centered")

st.title("Diabetes Progression Predictor")
st.write("Enter the 10 baseline physiological features to predict diabetes progression.")

model = joblib.load("best_diabetes_model.joblib")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", value=0.0, format="%.4f")
    sex = st.number_input("Sex", value=0.0, format="%.4f")
    bmi = st.number_input("BMI", value=0.0, format="%.4f")
    bp = st.number_input("BP", value=0.0, format="%.4f")
    s1 = st.number_input("S1", value=0.0, format="%.4f")

with col2:
    s2 = st.number_input("S2", value=0.0, format="%.4f")
    s3 = st.number_input("S3", value=0.0, format="%.4f")
    s4 = st.number_input("S4", value=0.0, format="%.4f")
    s5 = st.number_input("S5", value=0.0, format="%.4f")
    s6 = st.number_input("S6", value=0.0, format="%.4f")

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]],
        columns=["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"]
    )
    prediction = model.predict(input_data)
    st.success(f"Predicted Diabetes Progression: {float(prediction[0]):.2f}")

