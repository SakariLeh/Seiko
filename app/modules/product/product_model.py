
from app.infrastructure import db

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description_intro = db.Column(db.String(255), nullable=False)
    description_text = db.Column(db.Text, nullable=False)