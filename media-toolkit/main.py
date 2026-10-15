class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        expense = {
            "name": name,
            "amount": amount
        }

        self.expenses.append(expense)
        print(f"Added {name}: ₹{amount}")

    def show_expenses(self):
        print("\n--- Your Expenses ---")

        for expense in self.expenses:
            print(f"{expense['name']}: ₹{expense['amount']}")

    def total_expenses(self):
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"\nTotal expenses: ₹{total}")


tracker = ExpenseTracker()

tracker.add_expense("Food", 200)
tracker.add_expense("Travel", 100)
tracker.add_expense("Shopping", 500)

tracker.show_expenses()
tracker.total_expenses()