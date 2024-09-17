# upload_routes.py
from flask import Blueprint, request, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from datetime import datetime  # Add this import
import os
from app import mongo

upload_bp = Blueprint('upload', __name__)


UPLOAD_FOLDER =  os.path.join(os.path.dirname(os.path.abspath(__file__)), '../uploads')  # Directory for uploaded files

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@upload_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Route to handle file uploads
@upload_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        # Save file information to MongoDB (including description)
        user_id = get_jwt_identity()
        mongo.db.uploads.insert_one({
            "user_id": user_id,
            "filename": filename,
            "description": request.form.get('description', ''),
            "owner": request.form.get('owner', 'Anonymous'),  # Add owner info
            "upload_date": datetime.utcnow()  # Save the current date and time
        })

        return jsonify({"message": "File uploaded successfully!"}), 201

# Pagination function for retrieving uploads
@upload_bp.route('/uploads', methods=['GET'])
@jwt_required()
def get_all_uploads():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    current_user = get_jwt_identity()

    # Assuming the admin check or specific users have access to their uploads
    user_uploads = mongo.db.uploads.find({"user_id": current_user}).skip((page - 1) * limit).limit(limit)
    
    uploads = []
    for upload in user_uploads:
        uploads.append({
            "filename": upload['filename'],
            "description": upload['description'],
            "file_url": f"http://localhost:5000/uploads/{upload['filename']}",
            "owner": upload['owner'],  # Add owner info
            "upload_date": upload['upload_date']  # Add upload date
        })

    total_uploads = mongo.db.uploads.count_documents({"user_id": current_user})
    total_pages = (total_uploads + limit - 1) // limit

    return jsonify({
        "uploads": uploads,
        "total_pages": total_pages
    }), 200