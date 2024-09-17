from flask import Flask
from .mongo_setup import mongo 
from flask_cors import CORS
from dotenv import load_dotenv
from .auth_routes import auth_bp
from flask_jwt_extended import JWTManager
from .todo_routes import todo_bp
from .upload_routes import upload_bp 
import os



jwt = JWTManager()
# Initialize the Flask app and MongoDB
def create_app():

     # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)
    # MongoDB configuration
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    mongo.init_app(app)
    jwt.init_app(app)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Register routes
    from .auth_routes import auth_bp
    from .todo_routes import todo_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)
    app.register_blueprint(upload_bp)  # New file routes

    return app
