# 💊 Drug Prediction System
---

# 🌐 Live Demo

🔗 https://drugpredictionprojectp19-kzwmcahwejtdmzptyrb5uy.streamlit.app/

---

# 🚀 Project Overview

The Drug Prediction System is a Machine Learning-based healthcare application that predicts the most suitable drug for a patient based on medical attributes such as age, gender, blood pressure, cholesterol level, and sodium-to-potassium ratio.

The project aims to assist in understanding how patient characteristics influence drug recommendations by using classification algorithms trained on historical healthcare data.

This application demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, deployment, and real-time prediction using Streamlit.

---

# 🎯 Problem Statement

Selecting the appropriate medication is an important aspect of healthcare. Different patients may require different drugs depending on their medical conditions and biological characteristics.

This project aims to develop a predictive system that can classify patients into appropriate drug categories based on their health-related information.

The system helps demonstrate how machine learning can support decision-making in healthcare analytics.

---

# 📊 Dataset Information

Dataset Name: Drug Prediction Dataset

Total Records: 200

Total Features: 5

Target Variable:

* Drug

Drug Categories:

* drugA
* drugB
* drugC
* drugX
* drugY

---

# 📋 Dataset Features

| Feature     | Description               |
| ----------- | ------------------------- |
| Age         | Patient Age               |
| Sex         | Male / Female             |
| BP          | Blood Pressure Level      |
| Cholesterol | Cholesterol Level         |
| Na_to_K     | Sodium to Potassium Ratio |
| Drug        | Target Variable           |

---

# ⚙️ How The System Works

```text
Patient Information
         │
         ▼
 Data Preprocessing
         │
         ▼
 Feature Encoding
         │
         ▼
 Trained ML Model
         │
         ▼
 Drug Prediction
         │
         ▼
 Final Result
```

---

# 🔍 Input Parameters

The user provides:

### 👤 Personal Information

* Age
* Gender

### 🩺 Health Information

* Blood Pressure

  * High
  * Normal
  * Low

* Cholesterol

  * High
  * Normal

* Sodium-to-Potassium Ratio

---

# 🎯 Prediction Output

The system predicts one of the following drug categories:

* Drug A
* Drug B
* Drug C
* Drug X
* Drug Y

Based on the patient's medical characteristics.

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-Learn

## Deployment

* Streamlit

---

# 🧠 Machine Learning Workflow

## Step 1: Data Collection

The healthcare dataset is loaded into Python using Pandas.

---

## Step 2: Data Preprocessing

Data preparation includes:

* Checking missing values
* Data validation
* Label Encoding
* Feature transformation

---

## Step 3: Exploratory Data Analysis (EDA)

The dataset is analyzed to understand:

* Age distribution
* Drug frequency
* Blood pressure trends
* Cholesterol impact
* Sodium-to-Potassium ratio influence

---

## Step 4: Feature Engineering

Relevant features are selected for training:

* Age
* Sex
* Blood Pressure
* Cholesterol
* Na_to_K Ratio

---

## Step 5: Model Training

The machine learning model learns patterns between patient attributes and drug categories.

The algorithm identifies relationships between medical conditions and appropriate medications.

---

## Step 6: Model Evaluation

Performance is evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Metrics

---

## Step 7: Prediction

The user enters patient details.

Example:

Age: 45

Sex: Male

BP: High

Cholesterol: High

Na_to_K: 25

Output:

Predicted Drug: drugY

---

# ✨ Features

✅ Drug Prediction

✅ Healthcare Dataset Analysis

✅ Data Preprocessing

✅ Feature Engineering

✅ Classification Model

✅ Real-Time Prediction

✅ Streamlit Web Application

✅ User-Friendly Interface

---

# 📂 Project Structure

```bash
Drug_Prediction_System/
│
├── drug200.csv
├── app.py
├── model.pkl
├── encoder.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

# 📈 Analysis Performed

### Drug Distribution Analysis

Study how different drug categories are distributed.

---

### Age-Based Analysis

Analyze drug recommendations across age groups.

---

### Blood Pressure Analysis

Understand how BP affects drug selection.

---

### Cholesterol Analysis

Study the relationship between cholesterol levels and medication categories.

---

### Na_to_K Analysis

Identify the importance of sodium-to-potassium ratio in drug prediction.

---

# 🎓 Learning Outcomes

Through this project, I learned:

* Data Cleaning
* Feature Encoding
* Exploratory Data Analysis
* Classification Models
* Healthcare Data Analytics
* Model Evaluation
* Streamlit Deployment
* End-to-End Machine Learning Workflow

---

# 🚀 Future Improvements

* Drug Recommendation Dashboard
* Explainable AI Integration
* Multiple Model Comparison
* Cloud Deployment
* API Development
* Patient History Tracking
* Advanced Healthcare Analytics

---

# 💡 Applications

This project can be useful for:

* Healthcare Analytics
* Educational Purposes
* Machine Learning Learning Projects
* Medical Data Analysis
* Clinical Decision Support Research

---

# 👨‍💻 Author

**Rishu Gurjar**

Python Developer | Machine Learning Enthusiast | Data Science Learner

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📜 Disclaimer

This project is developed for ml pratices & educational purpose only .

The predictions generated by the system should not be considered professional medical advice or used for actual medical treatment decisions.
