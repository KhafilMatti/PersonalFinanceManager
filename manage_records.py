# from backend.app import db, User, Transaction, Budget

# def get_user_id(username):
#     user = User.query.filter_by(username=username).first()
#     if user:
#         return user.id
#     else:
#         print("User not found.")
#         return None

# def edit_transaction(user_id):
#     transactions = Transaction.query.filter_by(user_id=user_id).all()
#     if not transactions:
#         print("No transactions found for this user.")
#         return

#     print("\nTransactions:")
#     for t in transactions:
#         print(f"{t.id}: {t.category} - {t.amount}")

#     tid = int(input("Enter the ID of the transaction to edit: "))
#     transaction = Transaction.query.get(tid)

#     if transaction and transaction.user_id == user_id:
#         new_category = input("Enter new category: ")
#         new_amount = float(input("Enter new amount: "))
#         transaction.category = new_category
#         transaction.amount = new_amount
#         db.session.commit()
#         print("Transaction updated successfully.")
#     else:
#         print("Invalid transaction ID.")

# def delete_transaction(user_id):
#     transactions = Transaction.query.filter_by(user_id=user_id).all()
#     if not transactions:
#         print("No transactions found for this user.")
#         return

#     print("\nTransactions:")
#     for t in transactions:
#         print(f"{t.id}: {t.category} - {t.amount}")

#     tid = int(input("Enter the ID of the transaction to delete: "))
#     transaction = Transaction.query.get(tid)

#     if transaction and transaction.user_id == user_id:
#         db.session.delete(transaction)
#         db.session.commit()
#         print("Transaction deleted successfully.")
#     else:
#         print("Invalid transaction ID.")

# def edit_budget(user_id):
#     budgets = Budget.query.filter_by(user_id=user_id).all()
#     if not budgets:
#         print("No budgets found for this user.")
#         return

#     print("\nBudgets:")
#     for b in budgets:
#         print(f"{b.id}: {b.category} - {b.limit}")

#     bid = int(input("Enter the ID of the budget to edit: "))
#     budget = Budget.query.get(bid)

#     if budget and budget.user_id == user_id:
#         new_category = input("Enter new category: ")
#         new_limit = float(input("Enter new limit: "))
#         budget.category = new_category
#         budget.limit = new_limit
#         db.session.commit()
#         print("Budget updated successfully.")
#     else:
#         print("Invalid budget ID.")

# def delete_budget(user_id):
#     budgets = Budget.query.filter_by(user_id=user_id).all()
#     if not budgets:
#         print("No budgets found for this user.")
#         return

#     print("\nBudgets:")
#     for b in budgets:
#         print(f"{b.id}: {b.category} - {b.limit}")

#     bid = int(input("Enter the ID of the budget to delete: "))
#     budget = Budget.query.get(bid)

#     if budget and budget.user_id == user_id:
#         db.session.delete(budget)
#         db.session.commit()
#         print("Budget deleted successfully.")
#     else:
#         print("Invalid budget ID.")

# # Main Menu
# if __name__ == "__main__":
#     from backend.app import app
#     with app.app_context():
#         username = input("Enter your username: ")
#         user_id = get_user_id(username)
#         if user_id:
#             print("\n1. Edit Transaction\n2. Delete Transaction\n3. Edit Budget\n4. Delete Budget")
#             choice = input("Choose an option: ")

#             if choice == "1":
#                 edit_transaction(user_id)
#             elif choice == "2":
#                 delete_transaction(user_id)
#             elif choice == "3":
#                 edit_budget(user_id)
#             elif choice == "4":
#                 delete_budget(user_id)
#             else:
#                 print("Invalid option.")
