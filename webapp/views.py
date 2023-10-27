from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from .models import Transactions
from . import db
from flask import flash
from flask import url_for
from sqlalchemy import func

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

     return render_template("dashboard.html", user = current_user)  
 
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user) 



@views.route('/transaction-history')
@login_required
def transaction_history():  
    # Query transactions
   if True:
        user_id = 1  # Replace with the user's ID
        
        transactions = Transactions.query.filter_by(user_id=current_user.id).all()
        income = Transactions.query.filter_by(user_id=current_user.id, transaction_type='Income').all()
        expense = Transactions.query.filter_by(user_id=current_user.id, transaction_type='Expense').all()
        # total_income = db.session.query(func.sum(Transactions.amount).filter(Transactions.user_id == user_id, Transactions.transaction_type == 'income')).scalar() or 0
        # total_expenses = db.session.query(func.sum(Transactions.amount).filter(Transactions.user_id == user_id, Transactions.transaction_type == 'expense')).scalar() or 0

        balance = 0

        for transaction in transactions:
            if transaction.transaction_type == 'Income':
                balance += transaction.amount
            else:
                balance -= transaction.amount

        return render_template("history.html", transactions=transactions, income=income, expense=expense, user=current_user, balance=balance)
    
    # Render transaction history pagereturn render_template("transaction_history.html", transactions=transactions, user=current_user)
