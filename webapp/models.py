from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


# Define the Income Model

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime(timezone=True), default=func.now())
    # accounts = db.relationship('Account', backref='user', lazy=True)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255))
    expense = db.Column(db.Float)
    income = db.Column(db.Float)
    total_income = db.Column(db.Float, default=0.00)
    total_expenses = db.Column(db.Float, default=0.00)
    balance = db.Column(db.Float, default=0.00)
    date_recorded = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
