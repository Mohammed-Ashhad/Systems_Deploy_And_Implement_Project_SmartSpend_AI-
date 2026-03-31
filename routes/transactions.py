from flask import Blueprint, current_app, redirect, render_template, request, url_for
from models.transaction import calculate_summary, delete_transaction, get_all_transactions, insert_transaction

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/")
def dashboard():
    db = current_app.config["DB"]
    return render_template(
        "dashboard.html",
        transactions=get_all_transactions(db),
        summary=calculate_summary(db),
        ai_reports=[],
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
