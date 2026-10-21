# 🎓 Student Final Exam Score Prediction Using ANN

An Artificial Neural Network (ANN) based Machine Learning project that predicts a student's final exam score using academic performance, attendance, study habits, and other student-related information. The project uses **TensorFlow/Keras** for deep learning and **Streamlit** to provide an interactive web application.

## 📌 Project Overview

Student performance can be influenced by several factors, including study hours, attendance, previous examination results, and assignment completion.

This project uses a trained ANN regression model to estimate a student's final exam score based on these input features.

Users can enter student information through a simple Streamlit interface and receive an instant score prediction.

## 🎯 Objectives

- Predict final exam scores using an Artificial Neural Network.
- Analyze the relationship between student academic factors and exam performance.
- Apply data preprocessing and feature scaling.
- Build an interactive web application using Streamlit.
- Demonstrate the practical deployment of a deep learning regression model.

## ✨ Features

- **ANN-based prediction:** Uses a trained deep learning model to estimate final exam scores.
- **Interactive interface:** Enter student details without writing code.
- **Multiple input features:** Considers study hours, attendance, previous exam scores, and assignments.
- **Categorical feature encoding:** Handles gender and internet access categories.
- **Feature scaling:** Uses a previously fitted scaler to preprocess inputs consistently.
- **Instant predictions:** Displays the predicted final exam score in the web application.

## 🧠 Model Architecture

The project uses a feedforward Artificial Neural Network built with TensorFlow/Keras.

| Layer | Configuration |
|---|---|
| Input layer | 9 input features |
| Hidden layer 1 | 64 neurons, ReLU activation |
| Hidden layer 2 | 32 neurons, ReLU activation |
| Output layer | 1 neuron, Linear activation |
| Optimizer | Adam |
| Loss function | Mean Squared Error (MSE) |
| Evaluation metrics | Mean Absolute Error (MAE), R² score |

The model is configured as a **regression model** because the target variable, `final_exam_score`, is a continuous numerical value.

*Note: This architecture describes the intended model configuration. Verify it against the saved model and training notebook.*

## 📊 Dataset Features

The dataset contains student-related features used to predict final exam performance.

| Feature | Description |
|---|---|
| `age` | Student's age |
| `gender` | Encoded gender category |
| `study_hours_per_day` | Daily study hours |
| `attendance_percentage` | Student attendance percentage |
| `previous_exam_score` | Score in a previous examination |
| `assignments_completed` | Number of completed assignments |
| `internet_access_no` | Indicates no internet access |
| `internet_access_unknown` | Indicates unknown internet access status |
| `internet_access_yes` | Indicates internet access is available |
| `final_exam_score` | Target variable for prediction |

The three internet access columns are one-hot encoded representations of a single categorical feature.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **TensorFlow / Keras** — ANN model development and inference
- **Pandas** — Data manipulation and preprocessing
- **NumPy** — Numerical computations
- **Scikit-learn** — Feature scaling and model evaluation
- **Streamlit** — Interactive web application
- **Pickle** — Loading the saved scaler

## 📁 Project Structure

```text
student-score-prediction/
│
├── app.py
├── model.h5
├── scaler.pkl
├── requirements.txt
├── README.md
│
└── dataset/
    └── student_data.csv
```

**File descriptions:**

- `app.py` — Streamlit application for score prediction.
- `model.h5` — Saved, trained ANN model.
- `scaler.pkl` — Fitted feature scaler used during model training.
- `requirements.txt` — Python dependency list.
- `dataset/student_data.csv` — Optional location for the original dataset.

The dataset and training notebook are optional at inference time if the trained model and scaler are already available.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd student-score-prediction
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
streamlit
tensorflow
pandas
numpy
scikit-learn
```

Then install the packages:

```bash
pip install -r requirements.txt
```

### 4. Verify the required files

Make sure the project directory contains:

- `app.py`
- `model.h5`
- `scaler.pkl`

The saved scaler must be the same fitted scaler used to preprocess the model's training data.

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

## 🔄 How It Works

1. **Input collection:** The user enters student information through the Streamlit interface.
2. **Preprocessing:** Categorical inputs are encoded into the expected numerical representation.
3. **Feature alignment:** Input columns are arranged in the same order used during model training.
4. **Feature scaling:** The saved scaler transforms the input features.
5. **ANN inference:** The trained neural network generates a numerical prediction.
6. **Result display:** The predicted final exam score is displayed in the application.

## 📈 Model Evaluation

Regression models should be evaluated using appropriate regression metrics.

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted scores.
- **Mean Squared Error (MSE):** Measures the average squared prediction error.
- **R² Score:** Measures how well the model explains variation in the target variable.

A lower MAE and MSE generally indicate better predictions, while an R² closer to 1 indicates a stronger fit on the evaluated dataset.

Actual evaluation results should be reported only after testing the model on held-out data.

## 🚀 Future Improvements

- Add a dashboard showing student performance insights.
- Visualize the relationship between attendance, study hours, and exam scores.
- Compare ANN performance against Linear Regression, Random Forest, and other models.
- Add model evaluation charts and actual-versus-predicted plots.
- Improve input validation and error handling.
- Deploy the application to a cloud hosting platform.
- Add explainability features to help understand which factors influence predictions.

## ⚠️ Limitations

- Predictions depend on the quality and representativeness of the training dataset.
- The model estimates exam performance; it cannot guarantee actual examination results.
- Predictions may be unreliable for students whose characteristics differ substantially from the training data.
- Model performance must be verified using unseen test data.
- Student information should be handled responsibly and with appropriate privacy safeguards.

## 👨‍💻 Author

**Salman**

Student | Python | Machine Learning | Deep Learning | Artificial Intelligence

## 📄 License

This project is intended for educational and learning purposes. Add a suitable open-source license if you plan to distribute the source code publicly.
