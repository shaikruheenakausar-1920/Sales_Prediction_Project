import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Sales Predictor", page_icon="📈", layout="centered")

# Load model
model = pickle.load(open("sales_model.pkl", "rb"))

st.title("📈 Sales Prediction App")
st.write("Enter your advertising budget below to predict sales.")

tv = st.number_input("TV Advertising Budget ($ thousands)", min_value=0.0, max_value=500.0, value=100.0, step=1.0)
radio = st.number_input("Radio Advertising Budget ($ thousands)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
newspaper = st.number_input("Newspaper Advertising Budget ($ thousands)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)

if st.button("Predict Sales"):
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=["TV", "Radio", "Newspaper"])
    prediction = model.predict(input_data)[0]
    prediction = max(0, round(prediction, 2))

    st.success(f"📊 Predicted Sales: {prediction} (thousand units)")
