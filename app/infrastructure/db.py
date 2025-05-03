
from flask_sqlalchemy import SQLAlchemy



class SQLiteDB(SQLAlchemy):
    """
    Класс для создания базы данных SQLite на
    основе SQLAlchemy
    """

    def init_app(self, app):
        uri_default = 'sqlite:///seiko.db'
        app.config.setdefault('SQLALCHEMY_DATABASE_URI', uri_default)
        app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

        super().init_app(app)

class PostgresDB(SQLAlchemy):
    """
    Класс для создания базы данных Postgres на
    основе SQLAlchemy
    """

    def init_app(self, app):
        app.config.setdefault(
            'SQLALCHEMY_DATABASE_URI',
            'postgresql://postgres:postgres@localhost:5432/seiko_db'
        )
        app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
        super().init_app(app)

db = SQLiteDB()




    

