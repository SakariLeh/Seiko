


# Экспорт функций работы со складом и бронированиями
from .warehouse_db import (
    products_db,
    reservations_db,
    get_product_by_id,
    get_all_products,
    update_product_quantity,
    create_reservation,
    get_reservations_by_user,
    get_all_reservations,
    get_reservation_by_id,
    update_reservation_status,
    delete_reservation
)


from .user_db import users_db
from .new_db import news_db
