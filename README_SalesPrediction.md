# 📈 Sales Prediction App

## What it does
A web app where you enter advertising budgets for TV, Radio, and Newspaper,
and it predicts the expected sales (in thousand units).

## How it works
- **Dataset**: Advertising.csv (200 rows)
- **Model**: Linear Regression (Scikit-learn)
- **Accuracy**: R² score = 0.90 on test data
- **Frontend**: Streamlit

## How to run
```
cd Sales_Prediction_Project
streamlit run app.py
```
This opens automatically in your browser. The model is already trained
(sales_model.pkl) so it works immediately — no need to retrain.

To retrain from scratch (optional, prints accuracy score):
```
python train_model.py
```
