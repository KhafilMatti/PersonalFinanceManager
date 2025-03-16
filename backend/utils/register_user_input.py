# import os
# import sys


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# from backend.app import db, User, app
# from werkzeug.security import generate_password_hash

# def register_user_cli():
#     with app.app_context():
#         try:
#             username = input("Enter a username: ").strip()
#             password = input("Enter a password: ").strip()

#             existing_user = User.query.filter_by(username=username).first()
#             if existing_user:
#                 print(f" User '{username}' already exists. Try another username.")
#                 return

#             hashed_pw = generate_password_hash(password)
#             new_user = User(username=username, password_hash=hashed_pw)
#             db.session.add(new_user)
#             db.session.commit()

#             print(f" User '{username}' registered successfully.")
#         except Exception as e:
#             print("Something went wrong:", str(e))

# if __name__ == "__main__":
#     register_user_cli()
