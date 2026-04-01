# ❤️ Heart Disease Prediction ML Project

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts the risk of heart disease based on clinical parameters. It includes data preprocessing, model training with cross-validation, and deployment using a Streamlit web app for real-time predictions.

---

## 🚀 Features

* 🔍 Data cleaning (duplicate removal)
* 📊 Exploratory Data Analysis (EDA)
* 🔁 Stratified Cross-Validation for reliable performance
* 🤖 Machine Learning model (Random Forest)
* 🌐 Interactive Streamlit web app
* ⚡ Real-time prediction system

---

## 🧠 Problem Statement

Heart disease is one of the leading causes of death worldwide. Early detection can significantly reduce risks. This project aims to predict whether a patient is at risk based on medical attributes.

---

## 📊 Dataset

* Source: UCI Heart Disease Dataset
* Total Features: 13 input features
* Target:

  * 0 → No Heart Disease
  * 1 → Presence of Heart Disease

---

## ⚙️ Tech Stack

* Python 🐍
* Scikit-learn 🤖
* Pandas & NumPy 📊
* Streamlit 🌐
* Joblib 💾

---

## 🔁 Machine Learning Pipeline

1. Data Loading
2. Data Cleaning (Removed duplicates)
3. Feature-Target Split
4. Model Pipeline (StandardScaler + RandomForest)
5. Stratified Cross-Validation
6. Model Training
7. Model Saving

---

## 📈 Model Performance

* Cross-Validation Accuracy: **~82%**
* Model Used: Random Forest Classifier
* Validation Technique: Stratified K-Fold (k=5)

---

## 🌐 Live Demo

👉 (Add your Streamlit app link here after deployment)

---

## 💻 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Pratik-Haladkar/heart-disease-prediction-ml.git
cd heart-disease-prediction-ml
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train Model

```bash
python -m src.train
```

### 5️⃣ Run App

```bash
streamlit run app.py
```

---

## 📸 Screenshots

(Add screenshots of your app UI here)

---

## 🔮 Future Improvements

* 📊 Add model comparison (Logistic Regression, SVM)
* 🧠 Add SHAP explainability
* 🎯 Add risk probability levels (Low/Medium/High)
* 🌍 Deploy with custom domain

---

## 🙌 Author

**Pratik Haladkar**

---

## ⭐ If you found this useful

Give this repo a ⭐ on GitHub!
