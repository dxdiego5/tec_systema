import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os.path
filepath = os.path.abspath('app/data.db')
# Leave this out if the file doesn't exist yet
assert os.path.exists(filepath)
print(os.path.exists(filepath))
print(filepath)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():

    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = 'secret-key-1020304050-60708090100'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+filepath
    db.init_app(app)

    from .models.models import Users
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Users.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes.ticket import ticket as ticket_blueprint
    app.register_blueprint(ticket_blueprint)

    return app