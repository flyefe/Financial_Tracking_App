from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:maestro@localhost/fintracker'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your-username:your-password@your-hostname:5432/your-database-name'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://maestro:j49WApjiFDSZu1WJZADo4Q0qOBymDyNK@dpg-cl3gh4iuuipc738cmgjg-a.oregon-postgres.render.com/fintracker'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:maestro@localhost:5432/fintrack'
    






    db.init_app(app)



    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))



    return app
