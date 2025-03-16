import os
import sys
from getpass import getpass


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.app import app, db, User, Transaction, Budget
from werkzeug.security import generate_password_hash, check_password_hash

# Register a New User 
def register_user():
    with app.app_context():
        username = input("Enter a new username: ").strip()
        if User.query.filter_by(username=username).first():
            print(" User already exists.")
            return
        password = getpass("Enter a password: ").strip()
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        print(" User registered successfully.")


# Login Existing User
def login_user():
    with app.app_context():
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password: ").strip()
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            print(" Invalid credentials.")
            return None
        print(" Login successful.")
        return user


# Add Transaction 
def add_transaction(user):
    with app.app_context():
        category = input("Enter transaction category (e.g., groceries, rent): ").strip()
        try:
            amount = float(input("Enter transaction amount: "))
        except ValueError:
            print(" Invalid amount.")
            return
        new_txn = Transaction(user_id=user.id, category=category, amount=amount)
        db.session.add(new_txn)
        db.session.commit()
        print(" Transaction added.")


# View Transactions 
def view_transactions(user):
    with app.app_context():
        transactions = Transaction.query.filter_by(user_id=user.id).all()
        if not transactions:
            print(" No transactions found.")
            return
        print("\n Your Transactions:")
        for txn in transactions:
            print(f"{txn.id}. Category: {txn.category}, Amount: {txn.amount}")


# Edit Transaction
def edit_transaction(user):
    with app.app_context():
        transactions = Transaction.query.filter_by(user_id=user.id).all()
        if not transactions:
            print(" No transactions found.")
            return
        for txn in transactions:
            print(f"{txn.id}. Category: {txn.category}, Amount: {txn.amount}")
        try:
            txn_id = int(input("Enter ID of transaction to edit: "))
        except ValueError:
            print(" Invalid ID.")
            return
        txn = Transaction.query.filter_by(id=txn_id, user_id=user.id).first()
        if not txn:
            print(" Transaction not found.")
            return
        new_category = input(f"Enter new category (current: {txn.category}): ").strip()
        try:
            new_amount = float(input(f"Enter new amount (current: {txn.amount}): "))
        except ValueError:
            print(" Invalid amount.")
            return
        txn.category = new_category
        txn.amount = new_amount
        db.session.commit()
        print(" Transaction updated.")


# Budget Alerts 
def budget_alerts(user):
    with app.app_context():
        transactions = Transaction.query.filter_by(user_id=user.id).all()
        budgets = Budget.query.filter_by(user_id=user.id).all()
        category_totals = {}
        for t in transactions:
            category_totals[t.category] = category_totals.get(t.category, 0) + t.amount
        alerts = []
        for b in budgets:
            total = category_totals.get(b.category, 0)
            if total > b.limit:
                alerts.append(f"⚠️ Budget exceeded for {b.category}: {total} / {b.limit}")
        if alerts:
            print("\n Budget Alerts:")
            for alert in alerts:
                print(alert)
        else:
            print(" All budgets are within limits.")


# Add Budget 
def add_budget(user):
    with app.app_context():
        category = input("Enter budget category (e.g., groceries, rent): ").strip()
        try:
            limit = float(input("Enter budget limit amount: "))
        except ValueError:
            print(" Invalid amount.")
            return
        new_budget = Budget(user_id=user.id, category=category, limit=limit)
        db.session.add(new_budget)
        db.session.commit()
        print(" Budget added successfully.")


# Edit Budget 
def edit_budget(user):
    with app.app_context():
        budgets = Budget.query.filter_by(user_id=user.id).all()
        if not budgets:
            print(" No budgets found.")
            return
        print("\n Your Budgets:")
        for b in budgets:
            print(f"{b.id}. Category: {b.category}, Limit: {b.limit}")
        try:
            budget_id = int(input("Enter ID of budget to edit: "))
        except ValueError:
            print(" Invalid ID.")
            return
        budget = Budget.query.filter_by(id=budget_id, user_id=user.id).first()
        if not budget:
            print(" Budget not found.")
            return
        new_category = input(f"Enter new category (current: {budget.category}): ").strip()
        try:
            new_limit = float(input(f"Enter new limit amount (current: {budget.limit}): "))
        except ValueError:
            print(" Invalid amount.")
            return
        budget.category = new_category
        budget.limit = new_limit
        db.session.commit()
        print(" Budget updated.")


# Main Menu 
def main():
    while True:
        print("\n Finance Dashboard Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                while True:
                    print("\n User Options")
                    print("1. Add Transaction")
                    print("2. View Transactions")
                    print("3. Edit Transaction")
                    print("4. Add Budget")
                    print("5. Edit Budget")
                    print("6. Budget Alerts")
                    print("7. Logout")

                    user_choice = input("Select an action: ").strip()

                    if user_choice == '1':
                        add_transaction(user)
                    elif user_choice == '2':
                        view_transactions(user)
                    elif user_choice == '3':
                        edit_transaction(user)
                    elif user_choice == '4':
                        add_budget(user)
                    elif user_choice == '5':
                        edit_budget(user)
                    elif user_choice == '6':
                        budget_alerts(user)
                    elif user_choice == '7':
                        print("🚪 Logging out...")
                        break
                    else:
                        print(" Invalid option. Try again.")
        elif choice == '3':
            print("Goodbye, see you soon!")
            break
        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
