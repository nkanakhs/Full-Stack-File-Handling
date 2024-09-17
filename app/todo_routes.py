from flask import Blueprint, request, jsonify
from app.models import Todo
from bson.objectid import ObjectId

# Define the todo Blueprint
todo_bp = Blueprint('todo', __name__)

# Route for creating a new todo
@todo_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    task = data.get('task')
    location = data.get('location')
    user_id = data.get('user_id')

    new_todo = Todo(task=task, location=location, user_id=user_id)
    new_todo.save()

    return jsonify({"message": "Todo created successfully!"}), 201

# Additional routes for fetching, updating, deleting todos can be added here
