# streamlit_app.py
import streamlit as st
import joblib
import os
import numpy as np

# Debug: Show current directory and files (helps troubleshoot)
st.write("Current working directory:", os.getcwd())
st.write("Files in directory:", os.listdir())

# Load model with enhanced error handling
try:
    model_path = "sales_model.pkl"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        st.success("✅ Model loaded successfully!")
    else:
        st.error(f"❌ Model file not found at: {os.path.abspath(model_path)}")
        st.stop()  # Halt the app if model is missing
except Exception as e:
    st.error(f"🔥 Error loading model: {str(e)}")
    st.stop()

# --- Only runs if model loaded successfully ---
st.title("📈 Advertising Budget → Sales Predictor")

# User inputs
tv_budget = st.slider("TV Ad Budget ($)", 0, 300, 100)
radio_budget = st.slider("Radio Ad Budget ($)", 0, 50, 25)
newspaper_budget = st.slider("Newspaper Ad Budget ($)", 0, 120, 30)

# Prediction
input_data = np.array([[tv_budget, radio_budget, newspaper_budget]])
predicted_sales = model.predict(input_data)[0]
st.write(f"### 🔮 Predicted Sales: {predicted_sales:.2f} units")
