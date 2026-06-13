# 📈 Sales Prediction App

A machine learning web app that predicts product sales based on advertising spend, built with Python, Scikit-learn, and Streamlit.

## 🔗 Demo
> Add a screenshot or GIF of the app here after running it locally.
> Example: `![App Screenshot](screenshot.png)`

## 📌 Problem Statement
Businesses need to forecast sales based on how much they spend on advertising across different channels (TV, Radio, Newspaper). This project builds a regression model to predict sales from advertising budgets.

## 🛠 Tech Stack
- Python
- Pandas (data handling)
- Scikit-learn (machine learning)
- Streamlit (web app)

## 📊 Dataset
`Advertising.csv` — 200 rows with columns:
`TV, Radio, Newspaper, Sales`

## 🧠 Approach
1. **Preprocessing**: Dropped the unnamed index column.
2. **Model**: Trained a `Linear Regression` model using TV, Radio, and Newspaper advertising budgets as features to predict Sales.
3. **Evaluation**: Split data 80/20 (train/test) and evaluated using R² score.

## ✅ Result
**R² Score: 0.90** on the test set — meaning the model explains 90% of the variation in sales based on advertising spend alone.

## 📥 Sample Prediction
| TV Budget | Radio Budget | Newspaper Budget | → Predicted Sales |
|---|---|---|---|
| $230.1K | $37.8K | $69.2K | ~21.5K units |

## 🚀 How to Run
```bash
pip install streamlit pandas scikit-learn
streamlit run app.py
```
The app opens in your browser. The model (`sales_model.pkl`) is already trained, so it works immediately.

To retrain the model from scratch:
```bash
python train_model.py
```

## 📂 Project Structure
```
Sales_Prediction_Project/
├── app.py              # Streamlit app
├── train_model.py       # Model training script
├── Advertising.csv       # Dataset
└── sales_model.pkl       # Trained model
```

## 💡 What I Learned
- Building and evaluating a simple linear regression model
- Understanding how R² score measures model performance
- Deploying a trained regression model into an interactive Streamlit app
