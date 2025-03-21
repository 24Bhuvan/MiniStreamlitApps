import streamlit as st

# Title
st.title("BMI Calculator")

# Taking user input
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")

# Button to calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        
        # BMI Categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(f"Category: {category}")
    else:
        st.error("Height must be greater than 0!")
