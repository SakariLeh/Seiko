from flask import Flask
from app.config import Config





from app.infrastructure import db, migrationDB, get_socketio




from flask_cors import CORS


def create_app(config_class=Config, testing=False) -> Flask:
    app = Flask(__name__)

    CORS(app)
    
    
    
    app.config.from_object(config_class)
    app.config['TESTING'] = testing
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seiko.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    get_socketio().init_app(app, cors_allowed_origins="*", manage_session=False)

    

    with app.app_context():
        db.create_all()
        migrationDB.init_table_data()
    
    


    # Настройка статических файлов
    app.static_folder = 'static'

    # Регистрация Blueprint'ов
    from app.modules.auth import auth_bp
    from app.routes.dashboard import dashboard_bp

    from app.modules.user import user_bp
    from app.modules.news import news_bp
    from app.modules.warehouse import warehouse_bp
    from app.modules.reservation import reservation_bp
    from app.modules.chats import chat_bp


    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(warehouse_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(chat_bp)

    return app


__all__ = [
    "create_app",
]
    

