import pandas as pd
import pickle

data = pd.read_csv('Credit_data.csv')
print(data.head())
data = data.dropna()

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
data['Employment_Status'] = label_encoder.fit_transform(data['Employment_Status'])
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
features = ['Age','Income','Credit_Score','Loan_Amount','Debt-to-Income_Ratio']

from sklearn.model_selection import train_test_split

X = data.drop("Employment_Status", axis=1)
y = data['Employment_Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

filename = 'creditcard-eligibility-predictor-rfc-model.pkl'
pickle.dump(model, open(filename,'wb'))