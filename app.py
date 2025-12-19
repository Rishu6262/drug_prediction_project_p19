import streamlit as st
import numpy as np
import pickle

# ===============================
# Load trained model
# ===============================
with open('drug_model.pkl', 'rb') as file:
    model = pickle.load(file)

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Drug Prediction System",
    page_icon="💊",
    layout="centered"
)

st.title("💊 Drug Prediction System")
st.write("Predict the suitable drug based on patient details")

st.divider()

# ===============================
# User Inputs
# ===============================

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

bp = st.selectbox(
    "Blood Pressure",
    ["LOW", "NORMAL", "HIGH"]
)

cholesterol = st.selectbox(
    "Cholesterol",
    ["NORMAL", "HIGH"]
)

na_to_k = st.number_input(
    "Na to K Ratio",
    min_value=0.0,
    max_value=50.0,
    value=10.0
)

# ===============================
# Encoding (MUST match training)
# ===============================

# Manual encoding based on LabelEncoder order
sex_map = {"F": 0, "M": 1}
bp_map = {"HIGH": 0, "LOW": 1, "NORMAL": 2}
chol_map = {"HIGH": 0, "NORMAL": 1}

sex_encoded = sex_map[sex]
bp_encoded = bp_map[bp]
chol_encoded = chol_map[cholesterol]

# Input array
input_data = np.array([[age, sex_encoded, bp_encoded, chol_encoded, na_to_k]])

# ===============================
# Prediction
# ===============================
if st.button("🔍 Predict Drug"):
    prediction = model.predict(input_data)

    drug_map = {
        0: "Drug A",
        1: "Drug B",
        2: "Drug C",
        3: "Drug X",
        4: "Drug Y"
    }

    st.success(f"✅ Recommended Drug: **{drug_map[prediction[0]]}**")
