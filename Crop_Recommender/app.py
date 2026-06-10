import streamlit as st
import pickle
import numpy as np

# 1. Load the trained model
with open('Crop_Recommender/crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. App Styling & Header
st.set_page_config(page_title="Crop Recommendor", page_icon="🌱", layout="centered")
st.title("🌱 Smart Crop Recommendation System")
st.write("Enter the soil and weather metrics below to find the most optimal crop to grow.")

st.markdown("---")

# 3. Input Fields organized into columns
col1, col2 = st.columns(2)

with col1:
    n = st.number_input("Nitrogen (N) content", min_value=0, max_value=150, value=50)
    p = st.number_input("Phosphorus (P) content", min_value=0, max_value=150, value=50)
    k = st.number_input("Potassium (K) content", min_value=0, max_value=150, value=50)
    ph = st.number_input("Soil pH level", min_value=0.0, max_value=14.0, value=6.5, step=0.1)

with col2:
    temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0, step=0.1)
    humidity = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0, step=0.1)

st.markdown("---")

# 4. Prediction Logic
if st.button("Recommend Best Crop", use_container_width=True):
    # Format inputs for the model
    features = np.array([[n, p, k, temp, humidity, ph, rainfall]])
    prediction = model.predict(features)
    
    # Display Result
    st.balloons()
    st.success(f"🎉 The best crop to cultivate here is: **{prediction[0].upper()}**")
