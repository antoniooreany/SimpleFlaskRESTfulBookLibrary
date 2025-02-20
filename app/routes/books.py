from flask import Blueprint, jsonify, request

books_bp = Blueprint('books', __name__)

books = [
    {"id": 1, "title": "War and Peace", "author": "Leo Tolstoy"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]


@books_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the SimpleFlaskRESTfulBookLibrary API"})


@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify(book) if book else (jsonify({"error": "Book not found"}), 404)


@books_bp.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = max(book['id'] for book in books) + 1
    books.append(new_book)
    return jsonify(new_book), 201


@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify(book)


@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return '', 204  # Example blueprint for book routes
