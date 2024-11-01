from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Flask
app = Flask(__name__)
app.config.from_object(Config)

# Sql
db = SQLAlchemy(app)

# models
from app import routes, models

# creat 
with app.app_context():
    db.create_all()