import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
with open('new_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Biriyani Price Predictor")

# Input fields for the user
st.header("Enter the values:")
input1 = st.number_input("Biriyani price")
input2 = st.number_input("Rice Price")
input3 = st.number_input("Spice Price")
input4 = st.number_input("Vegetable Price")
input5 = st.number_input("Chef Experience")

# Prediction button
if st.button("Predict"):
    inputs = np.array([[input1, input2, input3, input4, input5]])
    prediction = model.predict(inputs)
    st.write(f"The predicted biriyani price is: {prediction[0]}")
