from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.admin.views import blueprint as admin_blueprint
from webapp.config import (
    REMEMBER_COOKIE_DURATION,
    SECRET_KEY,
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS,
)
from webapp.db import db
from webapp.event.views import blueprint as event_blueprint
from webapp.map.views import blueprint as map_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["REMEMBER_COOKIE_DURATION"] = REMEMBER_COOKIE_DURATION
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    migrate = Migrate(app, db)  # noqa

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(map_blueprint)
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
