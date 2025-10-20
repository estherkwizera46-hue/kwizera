import streamlit as st
import pandas as pd
import pickle
import numpy as np
# Load the trained model
with open('Model_saving.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Streamlit App UI
st.title("🌟 Personal Weight Prediction")
st.write("Enter your details to predict your weight:")

# Input fields
gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x==0 else "Male")
age = st.number_input("Age", min_value=1, max_value=120, value=25)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
workout_type = st.selectbox("Workout Type", [0, 1, 2, 3], format_func=lambda x: f"Type {x}")

# Predict button
if st.button("Predict Weight"):
    Input=np.array([[gender,age,height,workout_type]])
    input_data = pd.DataFrame([{
        'Gender': gender,
        'Age': age,
        'Height (m)': height,
        'Workout_Type': workout_type
    }])
    
    predicted_weight = loaded_model.predict(Input)
    st.success(f"Predicted Weight: {predicted_weight[0]:.2f} kg")
