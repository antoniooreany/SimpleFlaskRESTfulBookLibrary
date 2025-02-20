from flask import Blueprint, request, jsonify
import logging

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username') # Get the username from the request
    password = data.get('password') # Get the password from the request

    # Dummy authentication logic
    if username == 'admin' and password == 'password': # todo Replace with a real authentication logic
        logging.info(f"User {username} logged in successfully.")
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f"Failed login attempt for username: {username}")
        return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json() # Get the JSON data from the request
    username = data.get('username') # Get the username from the request

    logging.info(f"User {username} logged out.") # Log the logout event
    return jsonify({"message": "Logout successful"}), 200 # Return a JSON response with a message and a status code of 200
