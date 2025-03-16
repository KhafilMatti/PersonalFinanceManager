# import os
# import sys


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from backend.app import db, User, app
# from werkzeug.security import generate_password_hash

# username = input("Enter your username: ").strip()
# user = User.query.filter_by(username=username).first()
# if not user:
#     print("User not found.")
# else:
#     transactions = Transaction.query.filter_by(user_id=user.id).all()
#     budgets = Budget.query.filter_by(user_id=user.id).all()

#     category_totals = {}
#     for t in transactions:
#         category_totals[t.category] = category_totals.get(t.category, 0) + t.amount

#     for b in budgets:
#         if category_totals.get(b.category, 0) > b.limit:
#             print(f"⚠️ ALERT: You exceeded your {b.category} budget!")
