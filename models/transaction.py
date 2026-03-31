from bson.objectid import ObjectId
from datetime import datetime

def insert_transaction(db, data):
    transaction = {
        "amount": float(data["amount"]),
        "type": data["type"],
        "category": data["category"],
        "description": data.get("description", ""),
        "date": datetime.now(),
    }
    return db.transactions.insert_one(transaction)

def get_all_transactions(db):
    return list(db.transactions.find().sort("date", -1))

def delete_transaction(db, transaction_id):
    return db.transactions.delete_one({"_id": ObjectId(transaction_id)})

def calculate_summary(db):
    income = 0
    expenses = 0
    for item in db.transactions.find():
        if item["type"] == "income":
            income += item["amount"]
        else:
            expenses += item["amount"]
    return {"income": income, "expenses": expenses, "balance": income - expenses}
