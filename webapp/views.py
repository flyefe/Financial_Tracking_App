from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from .models import Transactions, Users
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
        # transaction_id = [result[0] for result in db.session.query(Transactions.transaction_id).all()] # Replace with the transaction ID
        transaction_id = db.session.query(Transactions.transaction_id).all()
        
        transactions = Transactions.query.filter_by(user_id=current_user.id).all()

        transaction = db.session.query(Transactions.amount).filter(Transactions.transaction_id == transaction_id).all()

        transaction_type = Transactions.transaction_type

        for transid in transaction_id:
            if  transaction_type== 'income':
                income = (
                    db.session.query(Transactions.amount)
                    .filter(
                        Transactions.user_id == current_user.id,
                        Transactions.transaction_id == transid,
                        Transactions.transaction_type == 'income'
                    )
                    .scalar()
                        )
            else:
                # Query the expense amount for a specific user and transaction
                expense = (
                    db.session.query(Transactions.amount)
                    .filter(
                        Transactions.user_id == current_user.id,
                        Transactions.transaction_id == transid,
                        Transactions.transaction_type == 'expense'
                    )
                    .scalar() )
           
        return render_template("history.html", transactions=transactions, income=income, expense=expense, user=current_user)
    # Render transaction history pagereturn render_template("transaction_history.html", transactions=transactions, user=current_user)


@views.route('/test')
@login_required  
def test():
    user = db.session.query(Users).all()
    print(user)
    all_transactions = db.session.query(Transactions.transaction_type).all()
    query = all_transactions


    return render_template("addrecord.html", user=current_user, query=query)