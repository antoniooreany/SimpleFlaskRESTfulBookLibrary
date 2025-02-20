from flask import Blueprint, request, jsonify
import logging

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Dummy authentication logic
    if username == 'admin' and password == 'password':
        logging.info(f"User {username} logged in successfully.")
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f"Failed login attempt for username: {username}")
        return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    username = data.get('username')

    logging.info(f"User {username} logged out.")
    return jsonify({"message": "Logout successful"}), 200
