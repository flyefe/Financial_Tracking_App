from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from .models import Account
from . import db
from flask import flash
from flask import url_for

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
def home():
     if request.method == 'POST':
        description = request.form.get('description')
        category = request.form.get('category')
        amount = request.form.get('amount')
        income = 0
        expense = 0
        if category == "income":
            income = amount
        else:
            expense = amount
        
        record_amount = Account(description=description, income=income, expense=expense, user_id=current_user.id)

        # record_amount= Account(discription=discription, income=income, expense=expense, category=category, user_id=current_user.id)
        db.session.add(record_amount)
        db.session.commit()
        flash('Record Added!', category='success')
        return redirect(url_for('views.home'))

     return render_template("dashboard.html", user = current_user)  
 
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user) 