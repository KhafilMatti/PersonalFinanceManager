# import os
# import sys


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from backend.app import db, Transaction, User, app

# def edit_transaction():
#     with app.app_context():
#         username = input("Enter your username: ").strip()
#         user = User.query.filter_by(username=username).first()

#         if not user:
#             print(" User not found.")
#             return

#         transactions = Transaction.query.filter_by(user_id=user.id).all()
#         if not transactions:
#             print("No transactions to edit.")
#             return

#         print("\n Existing Transactions:")
#         for t in transactions:
#             print(f"{t.id}: {t.category} - ${t.amount}")

#         try:
#             transaction_id = int(input("Enter ID of transaction to edit: "))
#             transaction = Transaction.query.filter_by(id=transaction_id, user_id=user.id).first()
#             if not transaction:
#                 print("Transaction not found.")
#                 return

#             category = input("Enter new category (leave blank to keep same): ").strip()
#             amount = input("Enter new amount (leave blank to keep same): ").strip()

#             if category:
#                 transaction.category = category
#             if amount:
#                 transaction.amount = float(amount)

#             db.session.commit()
#             print(" Transaction updated successfully.")
#         except Exception as e:
#             print(" Error updating transaction:", str(e))

# if __name__ == "__main__":
#     edit_transaction()
