import streamlit as st
import pandas as pd

st.title("🌱 Crop Recommendation System")
st.write("Enter the environmental parameters to get the best crop recommendation.")

# Load the dataset directly
try:
    df = pd.read_csv('Crop_Recommender/Crop_recommendation.csv')
except Exception as e:
    st.error(f"Error loading data file: {e}")
    st.stop()

# Layout layout columns for input variables
col1, col2 = st.columns(2)

with col1:
    n = st.number_input("Nitrogen (N)", min_value=0, max_value=140, value=50)
    p = st.number_input("Phosphorus (P)", min_value=0, max_value=145, value=50)
    k = st.number_input("Potassium (K)", min_value=0, max_value=205, value=50)
    temp = st.number_input("Temperature (°C)", min_value=8.0, max_value=45.0, value=25.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=14.0, max_value=100.0, value=70.0)
    ph = st.number_input("pH level", min_value=3.5, max_value=10.0, value=6.5)
    rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0, value=100.0)

if st.button("Recommend Crop"):
    # Calculate difference between input values and data values to find the absolute closest matching rows
    df_metrics = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].copy()
    inputs = [n, p, k, temp, humidity, ph, rainfall]
    
    # Mathematical absolute distance calculation
    distance = ((df_metrics - inputs) ** 2).sum(axis=1)
    closest_index = distance.idxmin()
    recommended_crop = df.loc[closest_index, 'label']
    
    st.success(f"Best recommended crop for these conditions: **{recommended_crop.capitalize()}**")
