# from flask import Blueprint, jsonify, request
#
# books_bp = Blueprint('books', __name__)
#
# books = [
#     {"id": 1, "title": "War and Peace", "author": "Leo Tolstoy"},
#     {"id": 2, "title": "1984", "author": "George Orwell"}
# ]
#
#
# @books_bp.route('/')
# def index():
#     return jsonify({"message": "Welcome to the SimpleFlaskRESTfulBookLibrary API"})
#
#
# @books_bp.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)
#
#
# @books_bp.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((book for book in books if book['id'] == book_id), None)
#     return jsonify(book) if book else (jsonify({"error": "Book not found"}), 404)
#
#
# @books_bp.route('/books', methods=['POST'])
# def add_book():
#     new_book = request.json
#     new_book['id'] = max(book['id'] for book in books) + 1
#     books.append(new_book)
#     return jsonify(new_book), 201
#
#
# @books_bp.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((book for book in books if book['id'] == book_id), None)
#     if book:
#         book.update(request.json)
#         return jsonify(book)
#
#
# @books_bp.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [book for book in books if book['id'] != book_id]
#     return '', 204  # Example blueprint for book routes

from flask import Blueprint, jsonify, request
from app.models import Book
from app import db

books_bp = Blueprint('books', __name__)


@books_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the SimpleFlaskRESTfulBookLibrary API"})


@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])


@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())


# @books_bp.route('/books', data = request.json
#     data = request.json
#     new_book = Book(title=data['title'], author=data['author'])
#     db.session.add(new_book)
#     db.session.commit()
#     return jsonify(new_book.to_dict()), 201


@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201


@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    db.session.commit()
    return jsonify(book.to_dict())


@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204
