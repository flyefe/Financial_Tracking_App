from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


 
class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_type = db.Column(db.String(50))
    amount = db.Column(db.Float)
    transaction_date = db.Column(db.DateTime(timezone=True), default=func.now())
    description = db.Column(db.String(255))



# Define the Users Model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime(timezone=True), default=func.now())
    balance = db.Column(db.Float)
    transactions = db.relationship('Transactions', backref='users', lazy=True)
