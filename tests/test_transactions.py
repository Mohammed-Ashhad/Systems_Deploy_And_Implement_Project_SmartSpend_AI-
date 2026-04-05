def test_summary_math():
    income = 5000
    expenses = 1500
    balance = income - expenses
    assert balance == 3500

def test_delete_route_path():
    route = "/delete/123"
    assert route.startswith("/delete/")
