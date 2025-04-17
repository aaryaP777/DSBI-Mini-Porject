import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib  # For saving and loading models

# Loading dataset
data = pd.read_csv("HR-Employee-Attrition.csv")

# Preprocess the 'OverTime' column: Convert 'Yes' to 1 and 'No' to 0
data["OverTime"] = data["OverTime"].map({"Yes": 1, "No": 0})

# Define features (X) and target (y)
X = data[["Age", "MonthlyIncome", "OverTime", "YearsAtCompany"]] 
y = data["Attrition"]  

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Train a Logistic Regression model
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)

# Evaluate the models
rf_predictions = rf_model.predict(X_test)
lr_predictions = lr_model.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, rf_predictions))
print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_predictions))

# Save the Random Forest model 
joblib.dump(rf_model, "random_forest_model.pkl")

# Save the Logistic Regression model 
joblib.dump(lr_model, "logistic_regression_model.pkl")