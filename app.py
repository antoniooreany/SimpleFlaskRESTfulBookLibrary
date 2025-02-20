from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'a73335abd8e3a7683de8a98a2ece9581'  # Replace with a real secret key

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models after db is defined
from app.models import User, Book