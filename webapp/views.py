from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from .models import Transactions
from . import db
from flask import flash
from flask import url_for

views = Blueprint('views', __name__)









@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
     if request.method == 'POST':
        description = request.form.get('description')
        transction_type = request.form.get('transaction_type')
        amount = request.form.get('amount')
        new_transaction = Transactions(description=description, transaction_type=transction_type, amount=amount, user_id=current_user.id)

        db.session.add(new_transaction)
        db.session.commit()
        flash('Transaction added!', category='success')
        return redirect(url_for('views.home'))
    
     user_id = current_user.id  # Assuming current_user has an 'id' attribute
     
     
     transactions = Transactions.query.filter_by(user_id=user_id).all()
     latest_balance = Transactions.query.filter_by(user_id=user_id).order_by(Transactions.transaction_date.desc()).first()
     balance = latest_balance.balance if latest_balance else 0

     total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
     total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    
     return render_template("dashboard.html", user = current_user, total_income=total_income, total_expenses=total_expenses, balance=balance)  
 
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user) 



# @views.route('/transaction-history')
# @login_required
# def transaction_history():
#     # Query transactions
#     user_id = current_user  # Replace with the user's ID
#     # user_transactions = Transactions.query.filter_by(user_id=user_id).all()

#     transactions = db.session.query(Transactions).filter_by(user_id=user_id).all()
    
#     # Calculate total income and total expenses
#     # total_income = sum(transaction.income for transaction in transactions)
#     # total_expenses = sum(transaction.expense for transaction in transactions)
    
#     total_income = db.session.query(Transactions).filter_by(user_id=user_id, transaction_type='Income').all()
#     total_expenses = db.session.query(Transactions).filter_by(user_id=user_id, transaction_type='Expense').all()
#     income = sum(transaction.amount for transaction in total_income)
#     total_expenses  = sum(transaction.amount for transaction in total_expenses)

#     print()
#     # pritnt(trhansactions=user_transactions, total_income=total_income, total_expenses=total_expenses)
#     return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses,)

@views.route('/transaction-history')
@login_required
def transaction_history():
    # Query transactions
    user_id = current_user.id  # Assuming current_user has an 'id' attribute

    transactions = Transactions.query.filter_by(user_id=user_id).all()
    
    # Calculate total income and total expenses
    global total_income, total_expenses
    total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')

    # global total_income, total_expenses
    return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, user=current_user)
