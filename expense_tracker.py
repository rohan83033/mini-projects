import json
import os
EXPENSE_FILE = 'expenses.json'
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    return []
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport): ").strip()
        description = input("Enter description (optional): ").strip()
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added!")
    except ValueError:
        print("Invalid amount entered. Please enter a number.")
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")
def get_total(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Expense: ${total:.2f}")
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            get_total(expenses)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu options.")
if __name__ == "__main__":
    main()