# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load the Random Forest Classifier model
filename = 'creditcard-eligibility-predictor-rfc-model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
            # Retrieve form data and ensure the values are valid
            age = request.form.get('age', type=float)
            income = request.form.get('income', type=float)
            credit_score = request.form.get('credit_score', type=float)
            loan_amount = request.form.get('loan_amount', type=float)
            debt_to_income_ratio = request.form.get('debt-to-income_ratio', type=float)
            employment_status = request.form.get('employment_status', type=int)
            eligibility = request.form.get('eligibility', type=int)


            data = pd.DataFrame([[age, income, credit_score, loan_amount, debt_to_income_ratio, employment_status,eligibility ]]
                                , columns=['Age', 'Income', 'Credit_Score', 'Loan_Amount', 'Debt-to-Income_Ratio','Employment_Status','Outcome'])
            
            my_prediction = model.predict(data)
        
            return render_template('result.html', prediction=my_prediction[0])
            
if __name__ == '__main__':
    app.run(debug=True)
