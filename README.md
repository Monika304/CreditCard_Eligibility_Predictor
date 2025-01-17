# CreditCard_Eligibility_Predictor

**Requirements**

Flask==2.2.5
numpy==1.24.5
pandas==1.5.3
scikit-learn==1.2.2
Werkzeug==2.2.5
gunicorn==20.1.0  # If deploying to a server

**Key Findings for the Credit Eligibility Predictor**

Purpose: Predicts credit card eligibility using a RandomForestClassifier based on user inputs like age, income, loan amount, credit score, and employment status.

Data Insights: Features like employment status, credit score, and income significantly affect predictions. Proper preprocessing (handling missing values, scaling) is essential.

Model Performance: Can be improved with feature engineering, hyperparameter tuning, and balancing the dataset.

User Interface: Flask-based app with:
  *Input form on index.html.
  *Results (eligible or not) displayed on result.html with appropriate images.
  
Scalability: Expandable with APIs, cloud deployment, and more data for better accuracy.

Challenges: Addressing bias, ensuring secure data handling, and debugging prediction consistency.

Applications: Useful for banks to automate and streamline credit eligibility assessments.


**Table of Contents**

Introduction
  *Overview of the Project
  *Objectives
  
Dataset
  *Description of Credit_data.csv
  *Key Features and Labels
  *Data Preprocessing Steps
  
Machine Learning Model
  *Model Used: RandomForestClassifier
  *Model Training and Evaluation
  *Saving the Model: credit-eligibility-predictor-rfc-model.pkl
  
Project Structure

  *Explanation of Files and Folders
  *Static Assets (Images)
  *Templates (HTML Files)
  
Web Application Development

  *Flask Setup
  *app.py Code Explanation
  *Frontend Design (HTML Files)
  
Functionality

  *User Input Form (index.html)
  *Prediction Logic in Flask
  *Displaying Results (result.html)
  
Deployment

  *Local Setup Instructions
  *Requirements (requirements.txt)
  *Future Scope for Cloud Deployment
  
Key Findings

  *Insights from the Dataset
  *Challenges Faced
  *Improvements and Recommendations

**Tech Stack of the Project**

1.Programming Languages :
   *Python
   
2.Libraries and Frameworks :
   *Flask
   *Pandas
   *NumPy
   *scikit-learn
   *joblib
   *matplotlib/seaborn
   
3.Web Technologies :
   *HTML 
   *CSS 
   *JavaScript 
   
4.Machine Learning :
   *Random Forest Classifier
   *Model Evaluation Metrics
   
5.Version Control :
   *Git
   *GitHub
   
6.Deployment :
   *Localhost

7.Data :
   *CSV(Credit_data.csv)
   
8.Miscellaneou :
   *.gitignore
   *requirements.txt
   
**This stack ensures efficient data processing, machine learning, web development, and deployment**

**Run Locally**

python.app.py
  http://127.0.0.1:5000/

**Repository structure**

project/Credit Card Eligibility Predictor
│
├── static/
│   └── images/
│       ├── eligible.webp              # Image for eligible result
│       └── not_eligible.webp          # Image for not eligible result
│
├── templates/
│   ├── index.html                     # Form for user input
│   ├── result.html                    # Displays prediction result and respective image
│
├── app.py                             # Main Flask application
├── credit_card_deployment.py          # Script for training and saving the model
├── Credit_data.csv                    # Dataset for training the model
├── credit-eligibility-predictor-rfc-model.pkl # Pre-trained RandomForestClassifier model
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Ignore unnecessary files in Git
└── README.md                          # Project documentation

**Conclusion**

The project successfully predicts credit eligibility based on user-provided financial data using a machine learning model (Random Forest Classifier). The model was trained with a dataset, tested, and deployed via a Flask application. It efficiently classifies individuals as eligible or not eligible for credit, demonstrating the potential of machine learning in real-world applications like financial services.
  

