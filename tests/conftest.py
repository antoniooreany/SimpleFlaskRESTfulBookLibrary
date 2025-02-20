# # conftest.py
#
# import warnings
# from sqlalchemy.exc import SAWarning
#
#
# def pytest_configure(config):
#     warnings.filterwarnings("ignore", category=SAWarning, message=".*Query.get.*")
#     warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*LegacyAPIWarning.*")


import pytest
from app import create_app, db
from app.models import Book

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    with app.app_context():
        db.session.add_all([
            Book(title="War and Peace", author="Leo Tolstoy"),
            Book(title="1984", author="George Orwell")
        ])
        db.session.commit()
        yield db
        db.session.remove()