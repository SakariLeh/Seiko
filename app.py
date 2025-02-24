from flask import Flask
from config import Config
from routes.phone import phone_bp
from routes.password import password_bp
from models import init_db

app = Flask(__name__)
app.config.from_object(Config)

# Регистрируем Blueprints
app.register_blueprint(phone_bp)
app.register_blueprint(password_bp)

if __name__ == '__main__':
    init_db()  # Инициализация базы перед стартом
    app.run(debug=True)
