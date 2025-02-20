from flask import Flask
from app.routes.books import books_bp
from app.errors.handlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(books_bp)
    register_error_handlers(app)

    return app# Flask app package initializer