# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# db = SQLAlchemy()
# migrate = Migrate()
#
# # def create_app():
# #     app = Flask(__name__)
# #     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# #     app.config['SECRET_KEY'] = 'a73335abd8e3a7683de8a98a2ece9581'
# #
# #     db.init_app(app)
# #     migrate.init_app(app, db)
# #
# #     from app.routes.books import books_bp
# #     app.register_blueprint(books_bp)
# #
# #     return app
#
#
# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#     app.config['SECRET_KEY'] = 'a73335abd8e3a7683de8a98a2ece9581'
#
#     db.init_app(app)
#     migrate.init_app(app, db)
#
#     from app.routes.books import books_bp
#     app.register_blueprint(books_bp)
#
#     return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SECRET_KEY'] = 'a73335abd8e3a7683de8a98a2ece9581'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.books import books_bp
    app.register_blueprint(books_bp)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
