# import os
# import sys


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from backend.app import db, Transaction, User, app

# def view_transactions():
#     with app.app_context():  #  FIX: wrap all DB logic here
#         username = input("Enter your username: ").strip()
#         user = User.query.filter_by(username=username).first()

#         if not user:
#             print(f"User '{username}' not found.")
#             return

#         transactions = Transaction.query.filter_by(user_id=user.id).all()

#         if not transactions:
#             print(f"No transactions found for '{username}'.")
#         else:
#             print(f"\nTransactions for '{username}':")
#             for t in transactions:
#                 print(f"{t.id}. {t.category} - {t.amount}")

# if __name__ == "__main__":
#     view_transactions()
