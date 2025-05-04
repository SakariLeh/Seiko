
from flask import current_app

from app.infrastructure import db

from .reservation_models import ReservationModel

def create_reservation_service(product_id: int, quantity: int, user_id: int, role: str, company: str, location: str) -> ReservationModel | None:
    """
    Создает бронирование товара
    """
    # return Reservation.create_reservation(
    #     product_id,
    #     quantity,
    #     user_id,
    #     role,
    #     company,
    #     location
    # )

    reservation = None 

    with current_app.app_context():
        reservation = ReservationModel(
            product_id=product_id,
            user_id=user_id,
            quantity=quantity,
            
            company=company,
            location=location
        )

        db.session.add(reservation)
        db.session.commit()


    return reservation