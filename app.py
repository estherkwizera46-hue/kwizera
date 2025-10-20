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
gender = st.selectbox("Gender", ['Male', 'Female'])
age = st.number_input("Age", min_value=1, max_value=120, value=25)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
workout_type = st.selectbox("Workout Type", ['Cardio', 'HIIT', 'Strength','Yoga'])

gen=0
type=0
if gender=='Male':
    gen=0
else:
    gen=1
if workout_type == 'Cardio':
    type=0
elif workout_type == 'HIIT':
    type=1
elif workout_type== 'Strength':
    type=2
elif workout_type== 'Yoga':
    type=3

# Predict button
if st.button("Predict Weight"):
    Input=np.array([[gen,age,height,type]])
    input_data = pd.DataFrame([{
        'Gender': gender,
        'Age': age,
        'Height (m)': height,
        'Workout_Type': workout_type
    }])
    
    predicted_weight = loaded_model.predict(Input)
    st.success(f"Predicted Weight: {predicted_weight[0]:.2f} kg")

