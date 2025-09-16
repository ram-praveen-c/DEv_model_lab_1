def add_expense(amount, description):
    expenses.append({'amount': amount, 'description': description})

def show_expenses():
    print("Expenses:")
    for exp in expenses:
        print(f"{exp['description']}: ${exp['amount']}")
    print(f"Total: ${sum(exp['amount'] for exp in expenses)}")

expenses = []

add_expense(50, "Groceries")
add_expense(20, "Transport")
show_expenses()