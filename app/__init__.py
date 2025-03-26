from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Настройка статических файлов
    app.static_folder = 'static'

    # Регистрация Blueprint'ов
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.chat_routes import chat_bp

    app.register_blueprint(chat_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app