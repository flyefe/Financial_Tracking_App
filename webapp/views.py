from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
        return render_template("dashboard.html")


# @views.route('/dashboard')
# def dashboard():
#     return render_template("dashboard.html")

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