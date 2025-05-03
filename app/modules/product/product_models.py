
from app.infrastructure import db

class ProductModel(db.Model):
    """
    Модель продукта
    """

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description_intro = db.Column(db.String(255), nullable=False)
    description_text = db.Column(db.Text, nullable=False)


class ProductQuantityModel(db.Model):
    """
    Модель количества продуктов
    """
    __tablename__ = 'product_quantities'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    is_available = db.Column(db.Boolean, nullable=False, default=True)