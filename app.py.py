

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('C:/Users/druvi/OneDrive/Desktop/ML/heart_disease_model.sav','rb'))

# Prediction function
def heartdisease_prediction(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_array)
    if prediction[0] == 0:
        return 'The Person does not have Heart Disease'
    else:
        return 'The Person does have Heart Disease'

# Main function for Streamlit app
def main():

    
    # Title and description
    st.markdown("""
    # ❤️ Heart Disease Prediction Web App
    This app predicts whether a person has **heart disease** based on health parameters.
    Fill in the details below and click the button to get the prediction.
    """)
    
    # Sidebar inputs
    st.sidebar.header("Patient Details")
    age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=25)
    sex = st.sidebar.selectbox("Gender", ["Male", "Female"])
    sex_val = 1 if sex == "Male" else 0
    cp = st.sidebar.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
    trestbps = st.sidebar.number_input("Resting BP", min_value=80, max_value=250, value=120)
    chol = st.sidebar.number_input("Cholesterol", min_value=100, max_value=600, value=200)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    fbs_val = 1 if fbs == "Yes" else 0
    restecg = st.sidebar.number_input("Resting ECG (0-2)", min_value=0, max_value=2, value=0)
    thalach = st.sidebar.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.sidebar.selectbox("Exercise Induced Angina", ["Yes", "No"])
    exang_val = 1 if exang == "Yes" else 0
    oldpeak = st.sidebar.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.sidebar.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2, value=0)
    ca = st.sidebar.number_input("Number of Major Vessels Colored (0-3)", min_value=0, max_value=3, value=0)
    thal = st.sidebar.number_input("Thalassemia (1=Normal, 2=Fixed Defect, 3=Reversible Defect)", min_value=1, max_value=3, value=1)
    
    # Button to predict
    if st.button("💓 Predict Heart Disease"):
        try:
            input_data = [
                age, sex_val, cp, trestbps, chol, fbs_val, restecg,
                thalach, exang_val, oldpeak, slope, ca, thal
            ]
            result = heartdisease_prediction(input_data)
            
            # Display result with simple images
            if "does not have" in result:
                st.success(result)
                
            else:
                st.error(result)
                
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")

# Run the app
if __name__ == '__main__':
    main()
