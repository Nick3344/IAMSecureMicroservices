from flask import jsonify, request, Blueprint
import jwt
import datetime

auth_routes = Blueprint('auth_routes', __name__)

# Secret key for encoding/decoding JWT tokens (replace with a strong, random key)
SECRET_KEY = 'your_secret_key'

@auth_routes.route('/login', methods=['POST'])
def login():
    # Dummy authentication logic
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin_password':
        # Generate JWT token
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY)
        return jsonify(message="Login successful", token=token.decode('utf-8'))
    else:
        return jsonify(message="Invalid credentials"), 401


@auth_routes.route('/token', methods=['GET'])
def generate_token():
    return jsonify(token="dummy_token")
