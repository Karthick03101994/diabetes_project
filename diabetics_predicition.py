import pandas as pd
import numpy as np
import streamlit as st
import joblib 


with open('diabetics_predicition.pkl', 'rb') as f:
    model = joblib.load(f)

st.header("Welcome to diabetes predcitaion app")


Pregnancies=st.sidebar.text_input('Pregnancies count')
Glucose=st.sidebar.text_input('Glucose value')
BloodPressure=st.sidebar.text_input('BloodPressure value')
SkinThickness=st.sidebar.text_input('SkinThickness value')
Insulin=st.sidebar.text_input('Insulin value')
BMI=st.sidebar.text_input('BMI value')
DiabetesPedigreeFunction=st.sidebar.text_input('Diabetes PedigreeFunction value')
Age=st.sidebar.text_input('Age')

button=st.sidebar.button('Enter')

if button:
    input_data = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.write('You are predicted to not have diabetes.')
        st.write('Happy to hear that you dont have diabets but please take care of your foods and do exercies.')
    else:
        st.write('You are predicted to have diabetes.')
        st.write( '''Don't worry!!!!!
                 
                 A doctor or diabetes nurse can recommend the best type of medicine for type 2 diabetes. Some common medications include:
                Sulfonylureas
                These medications increase insulin production in the pancreas and are often prescribed with metformin. Examples include glipizide (Glucotrol XL), glyburide (DiaBeta, Glynase), and glimepiride (Amaryl).
                Metformin
                Also known as a biguanide, this is a common type 2 diabetes tablet.
                Insulin
                A hormone that helps regulate blood sugar, insulin is needed when other medications aren't effective enough. There are different types of insulin that work at different speeds and last for different lengths of time.
                Tablets that lower blood sugar and help the heart pump blood
                These include dapagliflozin, empagliflozin, ertugliflozin, and canagliflozin. '''
)


else:
    st.write('Please enter values and press the button to make a prediction.')