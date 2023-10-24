from flask import Blueprint

auth = Blueprint('auth', __name__)





@auth.route('/signup')
def signup():
    return "signup page"

@auth.route('/login')
def login():
    return "Login"

@auth.route('/logout')
def logout():
    return "Logout page"

@auth.route('/dashboard')
def dashboard():
    return "dashboard page"