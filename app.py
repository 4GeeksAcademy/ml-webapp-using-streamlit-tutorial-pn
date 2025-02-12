from pickle import load
import streamlit as st

st.write("Hello World!")


model = load(open("Breast_Cancer_Classifier.pkl", "rb"))
class_dict = {
    "0": "Remission",
    "1": "Non-remission",
}

value_key = {
    "30-39": 0,
    "40-49": 1,
    "50-59": 2,
    "60-69": 3,
    "Pre-menopause": 0,
    "Menopause": 1,
    "0-10": 3,
    "10-20": 2,
    "20-30": 1, 
    "30-40": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "Left": 0,
    "Right":1,
    "Left-Low": 0,
    "Left-Up": 2,
    "Right-Low": 3,
    "Right-Up": 1,
    "Yes": 1,
    "No": 0
}

st.title("Will the Breast Cancer Stay in Remission")

val1 = value_key[st.selectbox("Choose your age:", ["30-39", "40-49", "50-59", "60-69"])]
val2 = value_key[st.selectbox("Menopause:", ["Pre-menopause", "Menopause"])]
val3 = value_key[st.selectbox("Tumor Size:", ["0-10", "10-20", "20-30", "30-40"])]
val4 = value_key[st.selectbox("Degree Malign:", ["1", "2", "3"])]
val5 = value_key[st.selectbox("Breast:", ["Left", "Right"])]
val6 = value_key[st.selectbox("Breast Quadrant:", ["Left-Low", "Left-Up", "Right-Low", "Right-Up"])]
val7 = 0
val8 = 0
val9 = value_key[st.selectbox("Irradiated:", ["Yes", "No"])]

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)