import streamlit as st
import numpy as np
import pickle
from streamlit_option_menu import option_menu
diabetes_model=pickle.load(open('diabetic_disease.sav','rb'))
heart_model=pickle.load(open('heart_disease.sav','rb'))
with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',['Diabetic prediction','Heart Disease prediction'],icons=['activity','balloon-heart'],default_index=0)
if (selected=='Diabetic prediction'):
    st.title('Diabetic Disease Prediction')
    col1,col2=st.columns(2)
    with col1:
        pregnancies = st.number_input('Pregnancies', min_value=0)
        blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0)
        insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0)
        dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")

    with col2:
        glucose = st.number_input('Glucose Level (mg/dL)', min_value=0)
        skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0)
        bmi = st.number_input('BMI (Body Mass Index)', min_value=0.0, format="%.2f")
        age = st.number_input('Age', min_value=0)

# Predict button
    if st.button("Predict Diabetes"):
        input_data = [pregnancies, glucose, blood_pressure, skin_thickness,
                    insulin, bmi, dpf, age]

        input_np = np.asarray(input_data).reshape(1, -1)
        result = diabetes_model.predict(input_np)

        if result[0] == 1:
            st.error("⚠️ Person is Diabetic")
        else:
            st.success("✅ Person is Not Diabetic")
if (selected=='Heart Disease prediction'):
    st.title('Heart Disease Prediction')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1)
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0)
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)
        slope = st.number_input('Slope of the Peak Exercise ST Segment (0-2)', min_value=0, max_value=2)

    with col2:
        sex = st.selectbox('Sex (0 = female, 1 = male)', [0, 1])
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=0)
        exang = st.selectbox('Exercise Induced Angina (0 = No, 1 = Yes)', [0, 1])
        restecg = st.selectbox('Resting ECG Results (0–2)', [0, 1, 2])  # ✅ Added
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy (0–3)', min_value=0, max_value=3)

    with col3:
        cp = st.selectbox('Chest Pain Type (0–3)', [0, 1, 2, 3])
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL (1 = True, 0 = False)', [0, 1])
        oldpeak = st.number_input('ST Depression Induced by Exercise', format="%.1f")
        thal = st.selectbox('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)', [0, 1, 2, 3])

    # Predict button
    if st.button("Predict Heart Disease"):
        input_data = [age, sex, cp, trestbps, chol, fbs, thalach,
                    exang, oldpeak, slope,restecg, ca, thal]

        input_np = np.asarray(input_data).reshape(1, -1)
        result = heart_model.predict(input_np)

        if result[0] == 1:
            st.error("⚠️ Person is Likely to Have Heart Disease")
        else:
            st.success("✅ Person is Not Likely to Have Heart Disease")
