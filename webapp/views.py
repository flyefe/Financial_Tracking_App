from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "Hello World"

@views.route('/dashboard')
def dashboard():
    return "dashboard page"

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