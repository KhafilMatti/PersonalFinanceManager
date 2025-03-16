# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from backend.app import db, Transaction, User, app

# def add_transaction(user):
#     category = input("Enter transaction category: ").strip()
#     amount = float(input("Enter transaction amount: "))

#     new_txn = Transaction(user_id=user.id, category=category, amount=amount)
#     db.session.add(new_txn)
#     db.session.commit()
#     print(" Transaction added successfully!")

# def edit_transaction(user):
#     transactions = Transaction.query.filter_by(user_id=user.id).all()
#     if not transactions:
#         print("No transactions found.")
#         return

#     print("\nYour Transactions:")
#     for txn in transactions:
#         print(f"{txn.id}. Category: {txn.category}, Amount: {txn.amount}")

#     txn_id = int(input("\nEnter ID of transaction to edit: "))
#     txn = Transaction.query.filter_by(id=txn_id, user_id=user.id).first()

#     if not txn:
#         print(" Transaction not found.")
#         return

#     new_category = input("Enter new category (leave blank to keep current): ").strip()
#     new_amount_input = input("Enter new amount (leave blank to keep current): ").strip()

#     if new_category:
#         txn.category = new_category
#     if new_amount_input:
#         txn.amount = float(new_amount_input)

#     db.session.commit()
#     print(" Transaction updated successfully!")

# def main():
#     with app.app_context():  #  Ensure proper Flask context
#         username = input("Enter username: ").strip()
#         user = User.query.filter_by(username=username).first()

#         if not user:
#             print(" User not found.")
#             return

#         action = input("Do you want to [a]dd or [e]dit a transaction? ").strip().lower()
#         if action == 'a':
#             add_transaction(user)
#         elif action == 'e':
#             edit_transaction(user)
#         else:
#             print("Invalid option selected.")

# if __name__ == "__main__":
#     main()
