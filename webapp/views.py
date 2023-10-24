from flask import Blueprint, render_template, url_for, redirect, request

import werkzeug
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "Hello World"

@views.route('/dashboard')
def dashboard():
    # Sample user information
    user_info = {
        'username': 'JohnDoe',
        'total_expenses': 1000,  # Total expenses for JohnDoe
        'total_income': 2500,    # Total income for JohnDoe
    }

    # Sample expenses list
    expenses = [
        {'id': 1, 'description': 'Rent', 'amount': 500},
        {'id': 2, 'description': 'Groceries', 'amount': 200},
        # Add more expenses as needed
    ]

    # Sample income list
    income = [
        {'id': 1, 'description': 'Salary', 'amount': 2000},
        {'id': 2, 'description': 'Freelance', 'amount': 500},
        # Add more income entries as needed
    ]

    return render_template('dashboard.html', user=user_info, expenses=expenses, income=income)



@views.route('/profile')
def profile():
    return "profile page" 

@views.route('/history')
def history():
    return "history page"

@views.route('/goals')
def goals():
    return "goals page"

@views.route('/error')
def error():
    return "error page"