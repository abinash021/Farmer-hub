import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('crop_rec.pickle', 'rb'))

# Page Config
st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="centered")

# Title
st.title("🌾 Crop Recommendation System")
st.markdown("### Enter soil and climate data below:")

# Input Form
with st.form("crop_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=50)
        temperature = st.number_input("Temperature (°C)", value=25.0)

    with col2:
        P = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=50)
        humidity = st.number_input("Humidity (%)", value=80.0)

    with col3:
        K = st.number_input("Potassium (K)", min_value=0, max_value=150, value=50)
        ph = st.number_input("pH Level", value=6.5)

    rainfall = st.slider("Rainfall (mm)", min_value=0, max_value=400, value=100)

    submit = st.form_submit_button("Predict Crop")

# Prediction
if submit:
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]

    st.success(f"✅ Recommended Crop: **{prediction.capitalize()}**")
    st.balloons()
