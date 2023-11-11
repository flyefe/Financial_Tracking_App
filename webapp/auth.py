from flask import Blueprint, render_template, redirect, request, url_for, flash
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import session
from flask_login import login_user, logout_user, login_required, current_user
auth = Blueprint('auth', __name__)






@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.profile', user = current_user))
            else:
                flash("Incorrect password, try again", category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
       

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category='error')
        elif len(first_name) < 2 and len(last_name) < 2:
            flash('First name and last name must be greater than 1 character', category='error')
        elif password != confirm_password:
            flash("Passwords don't match", category='error')
        elif len(password) < 7:
            flash("Password must be at least 7 characters", category='error')
        elif Users.query.filter_by(email=email).first():
            flash("Email already exists", category='error')
        
        else:
            new_user = Users(username=username, first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password, method='sha256')  )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash ("Account created!", category='success')
            return redirect (url_for('views.profile'))
    flash ("Ready to Monitor Your Finances? Sign Up to get started", category='success')
    return render_template("sign-up.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    session.clear()
    flash("Logged out successfully", category='success')
    logout_user()
    return redirect(url_for('auth.login'))
