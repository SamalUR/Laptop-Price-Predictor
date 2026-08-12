# 💻 Laptop Price Predictor App

An End-to-End Machine Learning Web Application that predicts laptop prices based on hardware specifications using Machine Learning.

## 🚀 Features
* Predicts Laptop Prices in **INR (₹)** and converts to **LKR**.
* Handles various specifications including **RAM, ROM (Storage in GB/TB), CPU, GPU, OS, and Screen Resolution**.
* Built with **Random Forest Regressor** achieving an **R² Score of ~0.91**.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing & ML:** Pandas, NumPy, Scikit-Learn
* **Model Pipeline:** Random Forest Regressor, One-Hot Encoding
* **Web Framework:** Streamlit

## 📂 Project Structure
```text
Laptop-Price-Predictor/
├── dataset/
│   └── laptop_data.csv
├── data_processing.py      # Data cleaning and feature engineering
├── train_model.py          # Model training & pipeline export
├── app.py                  # Streamlit Web Interface
├── pipe.pkl                # Trained ML Pipeline
├── df.pkl                  # Processed DataFrame
├── requirements.txt        # Python Dependencies
└── README.md               # Project documentations
