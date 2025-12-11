🚗 Car Price Predictor Web Application

A machine learning–powered Flask web app that predicts the price of a used car based on its specifications.
The model analyzes features like company, model, year, fuel type, and kilometers driven to estimate a fair market value.

🔗 Live Demo: https://web-production-8bc84.up.railway.app/

📘 Project Overview

This project uses Machine Learning and a Linear Regression model trained on a cleaned dataset of used cars.
The web interface is built using Flask, making the app lightweight, fast, and easy to deploy.

The app also includes:
-Dynamic car model filtering based on selected company
-Clean UI form to enter car details
-Real-time prediction via the trained ML model
-Deployment-ready structure for Railway 

⚙️ How It Works

Dataset Trained on a preprocessed car dataset containing:
Company

Model

Year

Fuel Type

Kilometers Driven

Selling Price

ML Pipeline
The model performs:
-Data cleaning and feature selection

-Label encoding + one-hot encoding

-Linear Regression training

-Model serialization using Pickle

-Web App

-Flask backend

-HTML + CSS for frontend

-Auto-updating model list based on car company

-Prediction result delivered instantly

🧠 Tech Stack

Python 3.9+

Flask

Scikit-learn

Pandas

NumPy

Pickle

Gunicorn (for deployment)

Railway (hosting the live app)

✨ Author

Harsh Pandey
