from bson.objectid import ObjectId
from datetime import datetime

def insert_transaction(db, data):
    transaction_type = data["type"]
    category = "Salary" if transaction_type == "income" else data["category"]

    transaction = {
        "amount": float(data["amount"]),
        "type": transaction_type,
        "category": category,
        "description": data["description"],
        "date": datetime.now()
    }
    return db.transactions.insert_one(transaction)

def get_all_transactions(db):
    return list(db.transactions.find().sort("date", -1))

def delete_transaction(db, transaction_id):
    return db.transactions.delete_one({"_id": ObjectId(transaction_id)})

def calculate_summary(db):
    transactions = db.transactions.find()
    income = 0
    expenses = 0

    for t in transactions:
        if t["type"] == "income":
            income += t["amount"]
        else:
            expenses += t["amount"]

    return {
        "income": income,
        "expenses": expenses,
        "balance": income - expenses
    }
