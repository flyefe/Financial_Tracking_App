from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
# from sqlalchemy.orm import relationship


# Define the Expense Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_recorded = db.Column(db.DateTime(timezone=True), default=func.now())

# Define the Income Model
class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_recorded = db.Column(db.DateTime(timezone=True), default=func.now())


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    total_income = db.Column(db.Float, default=0.00)
    total_expenses = db.Column(db.Float, default=0.00)
    date_joined = db.Column(db.DateTime(timezone=True), default=func.now())
    current_balance = db.Column(db.Float)
    expenses = db.relationship('Expense', backref='user', lazy=True)
    income = db.relationship('Income', backref='user', lazy=True)
    