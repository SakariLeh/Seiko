
# from app.infrastructure import db



# from sqlalchemy import Enum

# from app.types.status_enum import EStatus

# class WarehouseOrderModel(db.Model):
#     """
#     Модель Бронирование товара
#     """

#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     status = db.Column(Enum(EStatus), nullable=False, default=EStatus.IN_REVIEW)
#     location = db.Column(db.String(100), nullable=False)
#     company = db.Column(db.String(100), nullable=False) 