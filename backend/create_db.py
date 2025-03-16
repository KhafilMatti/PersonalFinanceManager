import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  
from backend.app import app, db

with app.app_context():
    db.create_all()
    print("Database created successfully!")
