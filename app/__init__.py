from flask import Flask
from app.config import Config





from app.infrastructure import db 









def create_app(config_class=Config, testing=False) -> Flask:
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    app.config['TESTING'] = testing
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seiko.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    


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
<<<<<<< HEAD
    return app


__all_ = [
    "app",
    "db",
    "create_app",
]
=======
    app.register_blueprint(warehouse_bp)
    return app
>>>>>>> 1a455304a1b4069e3deb9f85a4e9c0f958dce519
