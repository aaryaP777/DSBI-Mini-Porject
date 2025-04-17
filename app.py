from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
import pickle
import joblib

app = Flask(__name__)
app.secret_key = "secure-key"

DB_PATH = os.path.join("database", "employee_attrition.db")

# Validate login from DB
def validate_login(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Routes
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if validate_login(username, password):
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("dashboard_extended.html", active_section="report")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/model_comparison")
def model_comparison():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("model_comparison.html")

@app.post("/attrition")
def predict_attrition():
    age = int(request.form["age"])
    monthly_income = float(request.form["monthly_income"])
    overtime = 1 if request.form["overtime"].strip().lower() == "yes" else 0
    years_at_company = int(request.form["years_at_company"])

    # Apply the simple prediction logic
    def simple_prediction_logic(age, monthly_income, overtime, years_at_company):
        if (age < 30 and years_at_company < 3) or overtime == 1 or monthly_income < 4000:
            return "High Risk"
        else:
            return "Low Risk"

    prediction = simple_prediction_logic(age, monthly_income, overtime, years_at_company)

    return render_template(
        "dashboard_extended.html",
        attrition_result=prediction,
        active_section="attrition"
    )
    
@app.route("/attrition", methods=["GET"])
def attrition_form():
    return render_template("dashboard_extended.html")

if __name__ == "__main__":
    app.run(debug=True)
