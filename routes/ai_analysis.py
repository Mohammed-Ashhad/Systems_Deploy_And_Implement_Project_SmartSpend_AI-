from flask import Blueprint, current_app, redirect, url_for
from google import genai
from datetime import datetime
from collections import defaultdict

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/generate-insights", methods=["POST"])
def generate_insights():
    db = current_app.config["DB"]
    transactions = list(db.transactions.find())

    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expenses

    category_totals = defaultdict(float)
    for t in transactions:
        if t["type"] == "expense":
            category_totals[t["category"]] += t["amount"]

    prompt = f"Income: {income}
Expenses: {expenses}
Balance: {balance}
Give 4 short financial tips."

    try:
        client = genai.Client()
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        ai_text = response.text
    except Exception as exc:
        ai_text = f"AI Error: {exc}"

    db.ai_reports.insert_one({"report_text": ai_text, "savings_score": 0, "created_at": datetime.utcnow()})
    return redirect(url_for("transactions.dashboard"))
