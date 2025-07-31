
from flask import current_app

from app.infrastructure import db

from .reservation_models import ReservationModel

from app.modules.product import ProductQuantityModel

def create_reservation_service(product_id: int, quantity: int, user_id: int, role: str, company: str, location: str) -> ReservationModel | None:
    """
    Создает бронирование товара
    """


    reservation = None 

    with current_app.app_context():
        current_product = ProductQuantityModel.query.filter_by(product_id=product_id).first()

        if current_product.quantity - quantity < 0:
            return None
            
        

        reservation = ReservationModel(
            product_id=product_id,
            user_id=user_id,
            quantity=quantity,
            
            company=company,
            location=location
        )

        current_product.quantity -= quantity

        if current_product.quantity == 0:
            current_product.is_available = False

        db.session.add(reservation)
        db.session.commit()


    return reservation


def find_all_reservations() -> list[ReservationModel]:
    return ReservationModel.query.all()