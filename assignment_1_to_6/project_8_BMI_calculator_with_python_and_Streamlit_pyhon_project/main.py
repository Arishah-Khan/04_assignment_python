import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter Your Height (in cm):", 100, 200, 165)
weight = st.slider("Enter Your Weight (in kg):", 30, 200, 50)

bmi = weight / (height / 100) ** 2

st.write(f"## Your Body Mass Index (BMI) is:  **{bmi:.2f}**")

if bmi < 18.5:
    category = "Underweight"
    color = "🔵"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
    color = "🟢"
elif 25 <= bmi < 29.9:
    category = "Overweight"
    color = "🟡"
else:
    category = "Obesity"
    color = "🔴"

st.markdown(f"### **Category: {color} {category}**")

st.markdown("""
### **BMI Categories:**
- 🔵 **Underweight:** BMI less than 18.5  
- 🟢 **Normal weight:** BMI between 18.5 and 24.9  
- 🟡 **Overweight:** BMI between 25 and 29.9  
- 🔴 **Obesity:** BMI 30 or greater  
""")
