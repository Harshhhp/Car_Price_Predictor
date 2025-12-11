# 🎬 Car Price Predictor Web App

A machine learning–powered web application built with Python, Flask, and Bootstrap.
It predicts the selling price of a used car based on key attributes such as company, model, year, fuel type, and kilometers driven.

🔗 **Live Demo:** (https://web-production-8bc84.up.railway.app/)

---

## 📘 Project Overview

This project uses a Linear Regression model trained on a cleaned dataset of used cars.
The web interface is built using Flask + Jinja Templates, with frontend styling done in Bootstrap.

The application provides an interactive UI that dynamically filters car models based on selected company and returns an accurate predicted price instantly.

---

## ⚙️ How It Works

1. Dataset: Cleaned dataset of used cars (company, model, year, fuel type, kms driven, selling price)

   
2. Preprocessing steps:
   
    -Handling missing values
   
    -Feature selection
   
    -One-hot encoding and label encoding
   
3. Machine Learning:
 
    -Model trained using Linear Regression
   
    -Model saved using Pickle
   
4. Prediction:

    -User fills form in Flask web UI
    
    -Backend processes input & returns predicted price
---

## 🧠 Tech Stack

-**Python 3.9+**

-**Flask**

-**Bootstrap 4**

-**Pandas**

-**NumPy**

-**Scikit-learn**

-**Pickle**

-**Gunicorn (for deployment)**

-**Railway (hosting)**

---
🧾 License

This project is open-source and available under the MIT License
.

✨ Author

Harsh Pandey
**Connect with me on LinkedIn:** [Harsh Pandey](https://www.linkedin.com/in/harsh-pandey-891261354/)

🖥️ Built with ❤️ using Python + Streamlit
