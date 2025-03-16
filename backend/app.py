from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance_manager.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "amount": self.amount
        }

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    limit = db.Column(db.Float, nullable=False)

# Routes
@app.route("/")
def home():
    return jsonify({"message": "Welcome to Personal Finance Manager API"})

# Register
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 409

    hashed_pw = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify(access_token=access_token), 200

# Simulated Logout
@app.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    return jsonify({"message": "Logout successful (client should delete token)"}), 200

# View All Transactions
@app.route("/transactions", methods=["GET"])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return jsonify([t.to_dict() for t in transactions]), 200

# Add Transaction
@app.route("/transaction", methods=["POST"])
@jwt_required()
def add_transaction():
    data = request.get_json()
    user_id = get_jwt_identity()

    new_transaction = Transaction(
        user_id=user_id,
        category=data["category"],
        amount=data["amount"]
    )
    db.session.add(new_transaction)
    db.session.commit()

    return jsonify({"message": "Transaction added successfully"}), 201

# Edit Transaction
@app.route("/transaction/<int:transaction_id>", methods=["PUT"])
@jwt_required()
def update_transaction(transaction_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    transaction = Transaction.query.filter_by(id=transaction_id, user_id=user_id).first()
    if not transaction:
        return jsonify({"message": "Transaction not found"}), 404

    transaction.category = data.get("category", transaction.category)
    transaction.amount = data.get("amount", transaction.amount)
    db.session.commit()

    return jsonify({"message": "Transaction updated successfully"}), 200

# Delete Transaction
@app.route("/transaction/<int:transaction_id>", methods=["DELETE"])
@jwt_required()
def delete_transaction(transaction_id):
    user_id = get_jwt_identity()
    transaction = Transaction.query.filter_by(id=transaction_id, user_id=user_id).first()
    if not transaction:
        return jsonify({"message": "Transaction not found"}), 404

    db.session.delete(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction deleted successfully"}), 200

# Add Budget
@app.route("/budget", methods=["POST"])
@jwt_required()
def add_budget():
    data = request.get_json()
    user_id = get_jwt_identity()

    new_budget = Budget(
        user_id=user_id,
        category=data["category"],
        limit=data["limit"]
    )
    db.session.add(new_budget)
    db.session.commit()

    return jsonify({"message": "Budget added successfully"}), 201

# View Budgets
@app.route("/budgets", methods=["GET"])
@jwt_required()
def view_budgets():
    user_id = get_jwt_identity()
    budgets = Budget.query.filter_by(user_id=user_id).all()
    return jsonify([
        {"id": b.id, "category": b.category, "limit": b.limit}
        for b in budgets
    ]), 200

# Edit Budget
@app.route("/budget/<int:budget_id>", methods=["PUT"])
@jwt_required()
def update_budget(budget_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    budget = Budget.query.filter_by(id=budget_id, user_id=user_id).first()
    if not budget:
        return jsonify({"message": "Budget not found"}), 404

    budget.category = data.get("category", budget.category)
    budget.limit = data.get("limit", budget.limit)
    db.session.commit()

    return jsonify({"message": "Budget updated successfully"}), 200

# Budget Alert
@app.route("/budget_alert", methods=["GET"])
@jwt_required()
def budget_alert():
    user_id = get_jwt_identity()
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    budgets = Budget.query.filter_by(user_id=user_id).all()

    category_totals = {}
    for t in transactions:
        category_totals[t.category] = category_totals.get(t.category, 0) + t.amount

    alerts = []
    for b in budgets:
        if category_totals.get(b.category, 0) > b.limit:
            alerts.append(f" You exceeded your {b.category} budget!")

    return jsonify({"alerts": alerts})

# Run app
if __name__ == "__main__":
    app.run(debug=True)

