import streamlit as st
import numpy as np
import joblib
import base64

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Diabetes Risk Prediction",
    page_icon="🩺",
    layout="centered"
)

# ===================== BACKGROUND IMAGE =====================
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# استخدم raw string لتجنب مشاكل backslash
set_background(r"D:\ANACONDA\my projects in data science\Diabetes Prediction App\background.png")

# ===================== LOAD MODEL =====================
try:
    model = joblib.load(r"D:\ANACONDA\my projects in data science\Diabetes Prediction App\models\diabetes_model.pkl")
except:
    st.error("❌ Model file not found. Please make sure 'diabetes_model.pkl' is in the project folder.")
    st.stop()

# ===================== MAIN CONTAINER =====================
st.markdown("""
<div style="
background-color: rgba(255, 255, 255, 0.88);
padding: 30px;
border-radius: 20px;
box-shadow: 0px 10px 30px rgba(0,0,0,0.25);
">
""", unsafe_allow_html=True)

# ===================== TITLE =====================
st.markdown(
    "<h1 style='text-align:center; color:#0B5394;'>🩺 Diabetes Risk Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "This application predicts the risk of diabetes using a Machine Learning model trained on medical data."
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ===================== INPUTS =====================
st.subheader("📋 Patient Medical Information")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose Level (mg/dL)", 0, 200, 120)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", 0, 150, 70)
    skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)

with col2:
    insulin = st.number_input("Insulin Level (μU/mL)", 0, 900, 80)
    bmi = st.number_input("BMI (Body Mass Index)", 0.0, 70.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.number_input("Age", 1, 120, 30)

st.divider()

# ===================== PREDICTION =====================
if st.button("🔍 Predict Diabetes Risk"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                             skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("""
⚠️ **High Risk of Diabetes**

The model indicates a high probability of diabetes.

🔹 Recommendations:
- Consult a medical specialist.
- Monitor blood glucose regularly.
- Maintain a healthy diet.
- Engage in regular physical activity.
""")
    else:
        st.success("""
✅ **Low Risk of Diabetes**

The model indicates a low probability of diabetes.

🔹 Health Tips:
- Maintain a balanced diet.
- Exercise regularly.
- Monitor your health periodically.
""")

st.markdown("</div>", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown(
    "<p style='text-align:center; font-size:12px; color:gray;'>"
    "⚠️ This application is for educational purposes only and does not replace professional medical advice."
    "</p>",
    unsafe_allow_html=True
)
