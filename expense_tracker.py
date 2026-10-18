
# ==========================================
# Expense Tracker
# Beginner Python Project
# ==========================================

expenses = []


# Function to add a new expense
def add_expense():
    print("\n--- Add New Expense ---")

    category = input("Enter category (Food, Travel, etc.): ").strip()
    description = input("Enter expense description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense = {
        "category": category.title(),
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


# Function to display all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"\nExpense {number}")
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print(f"Amount: Rs. {expense['amount']:.2f}")


# Function to calculate total expenses
def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: Rs. {total:.2f}")


# Function to show expenses by category
def show_category_summary():
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    for category, total in category_totals.items():
        print(f"{category}: Rs. {total:.2f}")


# Main program
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        show_category_summary()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")