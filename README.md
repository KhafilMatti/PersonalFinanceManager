PERSONAL FINANCE MANAGER

A Flask-based personal finance management system that helps users track expenses, manage budgets, and receive budget alerts. Access it via a REST API (Postman) or an interactive command-line dashboard (VS Code terminal).

---

FEATURES 

User Registration & Login with secure JWT Authentication  
Add, Edit & View Transactions  
Set & Update Budgets per Category  
Get Budget Alerts when limits are exceeded  
 Dual Access:
  REST API via Postman
  CLI-based interactive dashboard via terminal
  SQLite Database (SQLAlchemy ORM)

---

TECH STACK

Backend: Flask (Python)
Database: SQLite (via SQLAlchemy)
Auth: Flask-JWT-Extended
CLI Input: Python `input()` + `getpass`
API Testing Tool: Postman

---

USING POSTMAN

POST/register – Register a new user
POST/login – Log in and get a JWT access token
POST/transaction – Add a new transaction (JWT required)
GET/transactions – View all transactions (JWT required)
GET/budget_alert – See budget warnings (JWT required)
Include Authorization: Bearer (Token from postman) in headers for protected routes.

---

USING VSCODE TERMINAL

py backend/utils/finance_dashboard.py


