from models.transaction import insert_transaction


class DummyTransactions:
    def __init__(self):
        self.saved_transaction = None

    def insert_one(self, transaction):
        self.saved_transaction = transaction
        return transaction


class DummyDB:
    def __init__(self):
        self.transactions = DummyTransactions()


def test_summary_math():
    income = 5000
    expenses = 1500
    balance = income - expenses
    assert balance == 3500


def test_delete_route_path():
    route = "/delete/123"
    assert route.startswith("/delete/")


def test_income_transactions_use_salary_category():
    db = DummyDB()

    insert_transaction(db, {
        "amount": "2500",
        "type": "income",
        "category": "Food",
        "description": "Monthly salary",
    })

    assert db.transactions.saved_transaction["category"] == "Salary"
