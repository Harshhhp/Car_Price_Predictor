from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load dataset
car = pd.read_csv('Cleaned Car.csv')

# Load ML Model using absolute path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "LinearRegression.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].unique())

    # Create company → models mapping
    car_company_mapping = {}
    for company in companies:
        models = sorted(car[car['company'] == company]['name'].unique())
        car_company_mapping[company] = models

    return render_template('index.html',
                           companies=companies,
                           years=years,
                           fuel_types=fuel_types,
                           car_company_mapping=car_company_mapping)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form['company']
    car_model = request.form['car_model']
    year = int(request.form['year'])
    fuel_type = request.form['fuel_type']
    driven = int(request.form['kms'])

    input_df = pd.DataFrame([[car_model, company, year, driven, fuel_type]],
                             columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model.predict(input_df)[0]

    return render_template('result.html', prediction=round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True)
