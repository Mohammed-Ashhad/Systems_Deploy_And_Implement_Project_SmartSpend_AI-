from flask import Blueprint, current_app, redirect, url_for
from google import genai
from datetime import datetime
import os
from collections import defaultdict

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/generate-insights", methods=["POST"])
def generate_insights():
    db = current_app.config["DB"]

    transactions = list(db.transactions.find())

    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expenses

    # Category breakdown
    category_totals = defaultdict(float)
    for t in transactions:
        if t["type"] == "expense":
            category_totals[t["category"]] += t["amount"]

    category_text = "\n".join(
        [f"{cat}: {amt}" for cat, amt in category_totals.items()]
    )

    # Monthly trend analysis
    monthly_data = defaultdict(float)
    for t in transactions:
        if "date" in t:
            month = t["date"].strftime("%Y-%m")
            if t["type"] == "expense":
                monthly_data[month] += t["amount"]

    monthly_text = "\n".join(
        [f"{month}: {amt}" for month, amt in monthly_data.items()]
    )

    # Savings score (simple logic)
    if income == 0:
        savings_score = 0
    else:
        savings_score = round((balance / income) * 100)

    prompt = f"""
    Financial Summary:
    Income: {income}
    Expenses: {expenses}
    Balance: {balance}
    Savings Score: {savings_score}%

    Expense Breakdown by Category:
    {category_text}

    Monthly Expense Trend:
    {monthly_text}

    Provide short financial advice in 4-5 sentences.
    """

    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        ai_text = response.text
    except Exception as e:
        ai_text = f"AI Error: {str(e)}"

    db.ai_reports.insert_one({
        "income": income,
        "expenses": expenses,
        "balance": balance,
        "savings_score": savings_score,
        "report_text": ai_text,
        "created_at": datetime.utcnow()
    })

    return redirect(url_for("transactions.dashboard"))