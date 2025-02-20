import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books_returns_all_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_book_returns_correct_book(client):
    response = client.get('/books/1')
    assert response.status_code == 200
    assert response.json['title'] == "War and Peace"

def test_get_book_returns_404_for_nonexistent_book(client):
    response = client.get('/books/999')
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"

def test_add_book_creates_new_book(client):
    new_book = {"title": "New Book", "author": "New Author"}
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    assert response.json['title'] == "New Book"

def test_update_book_modifies_existing_book(client):
    updated_book = {"title": "Updated Title"}
    response = client.put('/books/1', json=updated_book)
    assert response.status_code == 200
    assert response.json['title'] == "Updated Title"

def test_delete_book_removes_book(client):
    response = client.delete('/books/1')
    assert response.status_code == 204
    response = client.get('/books/1')
    assert response.status_code == 404
