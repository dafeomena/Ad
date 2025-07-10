# streamlit_app.py
import streamlit as st
import joblib
import os
import numpy as np


# Correct model path - points to the Advert folder
model_path = os.path.join("Advert", "sales_model.pkl")

# Load model with enhanced error handling
try:
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        st.success("✅ Model loaded successfully from Advert folder!")
    else:
        st.error(f"❌ Model file not found at: {os.path.abspath(model_path)}")
        st.stop()  # Halt the app if model is missing
except Exception as e:
    st.error(f"🔥 Error loading model: {str(e)}")
    st.stop()

# --- App UI ---
st.title("📈 Advertising Budget → Sales Predictor")

# User inputs in a form
with st.form("prediction_form"):
    tv_budget = st.slider("TV Ad Budget ($)", 0, 300, 100)
    radio_budget = st.slider("Radio Ad Budget ($)", 0, 50, 25)
    newspaper_budget = st.slider("Newspaper Ad Budget ($)", 0, 120, 30)
    
    predict_button = st.form_submit_button("🚀 Predict Sales")

# Only predict when button is clicked
if predict_button:
    input_data = np.array([[tv_budget, radio_budget, newspaper_budget]])
    predicted_sales = model.predict(input_data)[0]
    
    # Display prediction with nice formatting
    st.success(f"""
    ### Prediction Results
    - TV Budget: ${tv_budget}
    - Radio Budget: ${radio_budget}
    - Newspaper Budget: ${newspaper_budget}
    
    **🎯 Predicted Sales:** {predicted_sales:.2f} units
    """)
    
    # Optional: Add a visual indicator
    st.progress(min(100, int(predicted_sales/2)))  # Scale for visualization
