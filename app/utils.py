from flask import jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify

# Create JWT token
def create_jwt(user_id):
    token = create_access_token(identity={"user_id": user_id})
    return token

# Get user ID from JWT token (automatically handled by flask_jwt_extended in protected routes)
def get_user_id():
    user_id = get_jwt_identity()
    return user_id
