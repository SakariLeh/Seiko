# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask





# class DBConfigSQLite:
#     """
#     Конфигурация базы данных SQLite.
#     """
#     db_uri: str 
#     track_modifications: bool
#     db: SQLAlchemy

#     def __init__(self):
#         self.db_uri = 'sqlite:///seiko.db'
#         self.track_modifications = False

#     def init_app(self, app: Flask):
#         app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = self.track_modifications
#         self.db = SQLAlchemy(app)
#         with app.app_context():
#             self.db.create_all()
    

#     def get_db(self):   
#         """
#         Возвращает объект базы данных SQLAlchemy.
#         """
#         return self.db