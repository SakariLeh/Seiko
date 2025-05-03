
from app.infrastructure import db

from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from app.types.status_enum import EStatus

class WarehouseOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ordered_quantity = db.Column(db.Integer, nullable=False)
    status = Column(PgEnum(EStatus, name='order_status_enum', create_type=False), nullable=False, default=EStatus.IN_REVIEW)