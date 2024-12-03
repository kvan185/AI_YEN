from flask import Blueprint, jsonify, request
from flask_pymongo import PyMongo
from .models import BirdData

main_routes = Blueprint('main_routes', __name__)

# Kết nối MongoDB
from flask import current_app
mongo = PyMongo()

@main_routes.before_app_first_request
def initialize_database():
    mongo.init_app(current_app)

# Route kiểm tra API hoạt động
@main_routes.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "API is running"})

# Route thêm dữ liệu chim yến
@main_routes.route('/api/birds', methods=['POST'])
def add_bird_data():
    data = request.get_json()
    mongo.db.bird_data.insert_one(data)
    return jsonify({"message": "Data added successfully"}), 201

# Route lấy tất cả dữ liệu chim yến
@main_routes.route('/api/birds', methods=['GET'])
def get_bird_data():
    data = list(mongo.db.bird_data.find())
    for item in data:
        item['_id'] = str(item['_id'])  # Chuyển ObjectId thành chuỗi
    return jsonify(data)
