
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_model_and_scaler():
    model = tf.keras.models.load_model(
        BASE_DIR / "model.h5",
        compile=False
    )

    with open(BASE_DIR / "scaler.pkl", "rb") as file:
        scaler = pickle.load(file)

    return model, scaler


model, scaler = load_model_and_scaler()

st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Final Exam Score Prediction")
st.write(
    "Enter the student's academic details to predict "
    "their final exam score using an ANN model."
)

st.divider()

st.subheader("Student Information")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=20
)

# Assumes Female=0 and Male=1 from LabelEncoder
gender_option = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

gender = 0 if gender_option == "Female" else 1

study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=0.0,
    max_value=24.0,
    value=2.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)

previous_score = st.number_input(
    "Previous Exam Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0,
    step=1.0
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    value=10,
    step=1
)

internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No", "Unknown"]
)

if st.button("Predict Final Exam Score", type="primary"):

    internet_no = int(internet_access == "No")
    internet_unknown = int(internet_access == "Unknown")
    internet_yes = int(internet_access == "Yes")

    # Keep EXACTLY the feature order used during training
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "study_hours_per_day": study_hours,
        "attendance_percentage": attendance,
        "previous_exam_score": previous_score,
        "assignments_completed": assignments,
        "internet_access_no": internet_no,
        "internet_access_unknown": internet_unknown,
        "internet_access_yes": internet_yes
    }])

    try:
        # Apply the same scaler used during training
        input_scaled = scaler.transform(input_data)

        # ANN prediction
        prediction = model.predict(
            input_scaled,
            verbose=0
        )

        predicted_score = float(
            np.asarray(prediction).reshape(-1)[0]
        )

        st.divider()
        st.subheader("Prediction Result")

        st.metric(
            label="Predicted Final Exam Score",
            value=f"{predicted_score:.2f}"
        )

        if 0 <= predicted_score <= 100:
            st.progress(predicted_score / 100)

        st.caption(
            "This is an ANN-based estimate, not a guaranteed exam result."
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.info(
            "Check that scaler.pkl and model.h5 were created "
            "using the same training features and feature order."
        )
