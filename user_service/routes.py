import jwt
from flask import jsonify, request, Blueprint
import requests

user_routes = Blueprint('user_routes', __name__)
users = []

# URL of the auth_service for token verification
AUTH_SERVICE_URL = 'http://localhost:5000/token'


# Secret key for decoding JWT tokens (must match the secret key used in auth_service)
SECRET_KEY = 'your_secret_key'

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Token is invalid


def verify_token(token):
    # Make a request to the auth_service for token verification
    response = requests.get(AUTH_SERVICE_URL, headers={'Authorization': token})

    if response.status_code == 200:
        return True  # Token is valid
    else:
        return False  # Token is invalid

@user_routes.before_request
def authenticate_user():
    if request.endpoint != 'user_routes.register':  # Exclude registration route from authentication
        token = request.headers.get('Authorization')

        if not token:
            return jsonify(message="Missing token"), 401

        # Verify token using the auth_service
        if not verify_token(token):
            return jsonify(message="Invalid token"), 401

@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if username is already taken
    if any(user['username'] == username for user in users):
        return jsonify(message="Username already taken"), 400

    # Create new user
    new_user = {'username': username, 'email': email, 'password': password}
    users.append(new_user)

    return jsonify(message="User registered successfully"), 201

@user_routes.route('/profile', methods=['GET'])
def get_profile():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify(message="Missing token"), 401

    decoded_token = decode_jwt_token(token)  # Example function to decode JWT token

    if not decoded_token:
        return jsonify(message="Invalid token"), 401

    # Retrieve user profile based on authentication token
    # This logic will be implemented using the decoded token (e.g., fetch user data from database)
    username = decoded_token.get('username')
    # Retrieve user profile from database (dummy response for now)
    user_profile = {'username': username, 'email': 'user@example.com'}
    return jsonify(user_profile)

@user_routes.route('/profile', methods=['PUT'])
def update_profile():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify(message="Missing token"), 401

    # Verify token using the auth_service
    if not verify_token(token):
        return jsonify(message="Invalid token"), 401

    # Update user profile based on authentication token
    # This logic will be implemented using the decoded token (e.g., update user data in database)
    if decode_jwt_token:
        username = decode_jwt_token.get('username')
        # Update user profile in database (dummy response for now)
        return jsonify(message="User profile updated successfully")
    else:
        return jsonify(message="Invalid token"), 401
