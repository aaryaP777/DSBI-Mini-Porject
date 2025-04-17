import pandas as pd

# Define sample input data
# Format: [Age, MonthlyIncome, OverTime (1 for Yes, 0 for No), YearsAtCompany]
sample_inputs = [
    [30, 5000, 1, 5],  # Example 1: Age=30, Income=5000, OverTime=Yes, Years=5
    [45, 8000, 0, 10], # Example 2: Age=45, Income=8000, OverTime=No, Years=10
    [25, 3000, 1, 2],  # Example 3: Age=25, Income=3000, OverTime=Yes, Years=2
]

# Feature names used during training
feature_names = ["Age", "MonthlyIncome", "OverTime", "YearsAtCompany"]

# Prediction logic
def simple_prediction_logic(age, monthly_income, overtime, years_at_company):
    if (age < 30 and years_at_company < 3) or overtime == 1 or monthly_income < 4000:
        return "High Risk"
    else:
        return "Low Risk"

# Test the logic with each input
for i, X_input in enumerate(sample_inputs, start=1):
    # Convert input to DataFrame
    X_df = pd.DataFrame([X_input], columns=feature_names)
    # Extract individual features
    age = X_df["Age"][0]
    monthly_income = X_df["MonthlyIncome"][0]
    overtime = X_df["OverTime"][0]
    years_at_company = X_df["YearsAtCompany"][0]
    # Apply the prediction logic
    prediction = simple_prediction_logic(age, monthly_income, overtime, years_at_company)
    print(f"Test Case {i}: Input={X_input}, Prediction={prediction}")