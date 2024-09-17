from bson.objectid import ObjectId
from .mongo_setup import mongo 
import bcrypt

class User:
    def __init__(self, username, password=None, _id=None):
        self.username = username
        self.password = password
        self._id = _id

    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

    def save(self):
        user_data = {"username": self.username, "password": self.password}
        mongo.db.users.insert_one(user_data)

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def verify_password(stored_password, provided_password):
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

class Todo:
    def __init__(self, task, location, user_id, _id=None):
        self.task = task
        self.location = location
        self.user_id = user_id
        self._id = _id

    def save(self):
        todo_data = {"task": self.task, "location": self.location, "user_id": self.user_id}
        mongo.db.todos.insert_one(todo_data)

    @staticmethod
    def find_by_user_id(user_id):
        return mongo.db.todos.find({"user_id": user_id})

    def update(self, task):
        mongo.db.todos.update_one({"_id": ObjectId(self._id)}, {"$set": {"task": task}})

    def delete(self):
        mongo.db.todos.delete_one({"_id": ObjectId(self._id)})
