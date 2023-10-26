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

     return render_template("dashboard.html", user = current_user)  
 
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user) 