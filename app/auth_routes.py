# auth_routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from bson.objectid import ObjectId

auth_bp = Blueprint('auth', __name__)

# Registration route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.find_by_username(username):
        return jsonify({"message": "User already exists"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create new user
    new_user = User(username=username, password=hashed_password)
    new_user.save()

    return jsonify({"message": "User registered successfully"}), 201

# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.find_by_username(username)

    if user and check_password_hash(user['password'], password):
        # Create JWT token
        token = create_access_token(identity={"user_id": str(user['_id'])})
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials!!"}), 401

# Protected route example
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()  # This protects the route, requiring a valid JWT to access it
def protected():
    current_user = get_jwt_identity()  # Get the current user's identity from the JWT
    return jsonify(logged_in_as=current_user), 200
