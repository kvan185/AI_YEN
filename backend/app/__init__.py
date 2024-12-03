from flask import Flask
from flask_cors import CORS
from .routes import main_routes  # Import routes từ file routes.py

def create_app():
    app = Flask(__name__)

    # Cấu hình CORS để cho phép giao tiếp với frontend React
    CORS(app)

    # Load các cấu hình từ file config.py
    app.config.from_object('config.Config')

    # Đăng ký các route
    app.register_blueprint(main_routes)

    return app
