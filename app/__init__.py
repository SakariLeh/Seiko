from flask import Flask
from app.config import Config


def create_app(config_class=Config, testing=False):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['TESTING'] = testing



    # Настройка статических файлов
    app.static_folder = 'static'

    # Регистрация Blueprint'ов
    from app.modules.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.chat_routes import chat_bp
    from app.modules.user import user_bp
    from app.modules.news import news_bp
    from app.modules.warehouse import warehouse_bp

    app.register_blueprint(chat_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(warehouse_bp)
    return app