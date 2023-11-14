from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import current_user, login_required
from .models import Transactions, Users
from . import db
from datetime import datetime, timedelta
from sqlalchemy import func


views = Blueprint('views', __name__)






@views.route('/all-users')
@login_required
def all_users():
    # Query users
    users = Users.query.all()

    return render_template("users.html", users=users, user=current_user)
  




@views.route('/', methods=['GET', 'POST'])
@login_required
def home():         
     user_id = current_user.id  # Assuming current_user has an 'id' attribute
     
     transactions = Transactions.query.filter_by(user_id=user_id).all()

     
       # Query total income and total expenses for the current date
     today = datetime.now().date()
     total_income_today = sum(transaction.amount for transaction in transactions
                            if transaction.transaction_type == 'income' and transaction.transaction_date.date() == today)
     total_expenses_today = sum(transaction.amount for transaction in transactions
                            if transaction.transaction_type == 'expense' and transaction.transaction_date.date() == today)
     
     seven_days_ago = datetime.now().date() - timedelta(days=7)
     total_income_last_7_days = sum(transaction.amount for transaction in transactions
                                if transaction.transaction_type == 'income' and seven_days_ago <= transaction.transaction_date.date() <= today)
     total_expenses_last_7_days = sum(transaction.amount for transaction in transactions
                                    if transaction.transaction_type == 'expense' and seven_days_ago <= transaction.transaction_date.date() <= today)

     latest_balance = Transactions.query.filter_by(user_id=user_id).order_by(Transactions.transaction_date.desc()).first()
     balance = latest_balance.balance if latest_balance else 0

     total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
     total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
     
     
     if request.method == 'POST':
        description = request.form.get('description')
        transction_type = request.form.get('transaction_type')
        amount = request.form.get('amount')
        date = request.form.get('datetime')
        new_transaction = Transactions(description=description, transaction_type=transction_type, date=date, amount=amount, user_id=current_user.id)

        if transction_type == 'expense' and float(amount) > balance:
                flash(f'your have ₦{balance} left. want to add more funds to your fundtracker?')
        else:
            db.session.add(new_transaction)
            db.session.commit()
            if transction_type == 'income':
                flash(f'Congratulations {current_user.first_name}!!! ₦{amount} added successfully. Remember your your tracker when you spend from {description}. Good Job.😊', category='success')
            else:
                flash(f'Welldone {current_user.first_name}!!! ₦{amount} was spent for {description}. Keep tracking your expenses. Good Job😊', category='success')
        
        return redirect(url_for('views.home'))
        
     return render_template("dashboard.html", user = current_user, total_income=total_income, total_expenses=total_expenses, balance=balance,
                                total_expenses_today=total_expenses_today, total_income_today=total_income_today,
                                total_expenses_last_7_days=total_expenses_last_7_days, total_income_last_7_days=total_income_last_7_days)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user) 


@views.route('/transaction-history')
@login_required
def all_transactions():
    # Query transactions
    user_id = current_user.id  # Assuming current_user has an 'id' attribute

    transactions = Transactions.query.filter_by(user_id=user_id).all()
    
    # Calculate total income and total expenses
    global total_income, total_expenses
    total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')

    # global total_income, total_expenses
    return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, user=current_user)

# All todays transactions
@views.route('/transaction-history/today', methods=['GET'])
@login_required
def transactions_today():
    user_id = current_user.id
    end_date = datetime.now().date()
    start_date = end_date
    transactions = Transactions.query.filter(
        Transactions.user_id == user_id,
        func.date(Transactions.transaction_date).between(start_date, end_date)
    ).all()
    total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, user=current_user)

@views.route('/transaction-history/last-7-days', methods=['GET'])
@login_required
def transactions_last_7_days():
    user_id = current_user.id
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)
    transactions = Transactions.query.filter(
        Transactions.user_id == user_id,
        func.date(Transactions.transaction_date).between(start_date, end_date)
    ).all()
    total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, user=current_user)


# Select date range
# @views.route('/transaction-history/selected-range', methods=['GET'])
# @login_required
# def transactions_selected_range():
#     user_id = current_user.id
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')

    

#     # Parse dates into datetime objects if provided
#     if start_date:
#         start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
#     if end_date:
#         end_date = datetime.strptime(end_date, '%Y-%m-%d').date()


#      # Ensure that the date range is valid
#     user_registration_date = Users.query.filter_by(id=user_id).first().date_joined.date()

#     if start_date < user_registration_date:
#         start_date = user_registration_date

    
#     if end_date < start_date:
#         end_date = start_date

#     if end_date < start_date

#     transactions = Transactions.query.filter(
#         Transactions.user_id == user_id,
#         func.date(Transactions.transaction_date).between(start_date, end_date)
#     ).all()

#     total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
#     total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    

#     return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, user=current_user)
# Select date range
@views.route('/transaction-history/selected-range', methods=['GET'])
@login_required
def transactions_selected_range():
    user_id = current_user.id
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Parse dates into datetime objects if provided
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    else:
        # Set a default start date if it's empty
        start_date = datetime.min.date()

    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    else:
        end_date = datetime.max.date()

    # Ensure that the date range is valid
    user_registration_date = Users.query.filter_by(id=user_id).first().date_joined.date()

    if start_date < user_registration_date:
        start_date = user_registration_date

    if end_date < start_date:
        end_date = start_date

    transactions = Transactions.query.filter(
        Transactions.user_id == user_id,
        func.date(Transactions.transaction_date).between(start_date, end_date)
    ).all()

     # Calculate total income and total expenses for the date range
    # total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    # total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')
    total_income = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'income')
    total_expenses = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'expense')

    return render_template('history.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, user=current_user)

from flask import render_template

@views.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
@login_required
def edit(transaction_id):

    user=current_user
    # Fetch the transaction by ID from the database
    transaction = Transactions.query.get(transaction_id)

    if not transaction:
        flash('Transaction not found', category='error')
        return redirect(url_for('views.transaction_history'))

    if request.method == 'POST':
        # Handle the form submission to update the transaction
        # Update the transaction fields based on the form data
        transaction.description = request.form.get('description')
        transaction.transaction_type = request.form.get('transaction_type')
        transaction.amount = request.form.get('amount')

        # Commit the changes to the database
        db.session.commit()

        flash('Transaction updated successfully!', category='success')
        return redirect(url_for('views.transaction_history'))

    # Render the edit form with the transaction data
    return render_template('edit.html', transaction=transaction, user=current_user)

# @views.route('/delete/<int:transaction_id>', methods=['POST'])
# @login_required
# def delete(transaction_id):
#     # Fetch the transaction by ID from the database
#     transaction = Transactions.query.get(transaction_id)

#     if not transaction:
#         flash('Transaction not found', category='error')
#         return redirect(url_for('views.transaction_history'))

#     # Delete the transaction from the database
#     db.session.delete(transaction)
#     db.session.commit()

#     flash('Transaction deleted successfully!', category='success')
#     return redirect(url_for('views.transaction_history'))

@views.route('/test')
def test():
    return render_template("test.html")