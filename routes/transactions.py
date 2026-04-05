from flask import Blueprint, render_template, request, redirect, url_for, current_app
from models.transaction import insert_transaction, get_all_transactions, delete_transaction, calculate_summary

transactions_bp = Blueprint("transactions", __name__)

from datetime import timezone
import pytz

@transactions_bp.route("/")
def dashboard():
    db = current_app.config["DB"]

    transactions = get_all_transactions(db)
    summary = calculate_summary(db)

    ai_reports = list(
        db.ai_reports.find().sort("created_at", -1).limit(5)
    )

    # Convert UTC to Qatar time
    qatar_tz = pytz.timezone("Asia/Qatar")

    for report in ai_reports:
        if report.get("created_at"):
            report["created_at"] = report["created_at"].replace(tzinfo=timezone.utc).astimezone(qatar_tz)

    return render_template(
        "dashboard.html",
        transactions=transactions,
        summary=summary,
        ai_reports=ai_reports
    )

@transactions_bp.route("/add", methods=["GET", "POST"])
def add_transaction():
    db = current_app.config["DB"]

    if request.method == "POST":
        insert_transaction(db, request.form)
        return redirect(url_for("transactions.dashboard"))

    return render_template("add_transaction.html")

@transactions_bp.route("/delete/<id>", methods=["POST"])
def delete(id):
    db = current_app.config["DB"]
    delete_transaction(db, id)
    return redirect(url_for("transactions.dashboard"))