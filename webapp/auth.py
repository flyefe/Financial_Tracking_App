from flask import Blueprint, render_template, redirect, request, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from flask_login import login_user, logout_user, login_required, current_user
auth = Blueprint('auth', __name__)





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
        # elif User.query.filter_by(email=email).first():
        #     flash("Email already exists", category='error')
        
        else:
            new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password, method='sha256')  )
            db.session.add(new_user)
            db.session.commit()
            flash ("Account created!", category='success')
            return redirect (url_for('views.profile'))
    
    return render_template("sign-up.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(email, password)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "Logout page"
