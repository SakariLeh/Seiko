
from typing import List, Dict, Any

from flask import current_app

# module product 
from app.modules.product import get_all_products_fetch, get_all_quantity_products_fetch, get_product_by_id_fetch
from app.modules.product import ProductModel, ProductQuantityModel



def get_warehouse_products_service() -> List[Dict[str, Any]]:
    """
    Возвращает список товаров на складе.
    В реальном приложении данные будут извлекаться из базы данных.
    """
    products: list[ProductModel] | list = get_all_products_fetch()
    return products

# def create_reservation_service(product_id: int, quantity: int, user_id: int, role: str, company: str, location: str) -> WarehouseOrderModel | None:
#     """
#     Создает бронирование товара
#     """
#     # return Reservation.create_reservation(
#     #     product_id,
#     #     quantity,
#     #     user_id,
#     #     role,
#     #     company,
#     #     location
#     # )

#     reservation = None 

#     with current_app.app_context():
#         reservation = WarehouseOrderModel(
#             product_id=product_id,
#             quantity=quantity,
#             user_id=user_id,
#             company=company,
#             location=location
#         )
#         current_app.db.session.add(reservation)
#         current_app.db.session.commit()


#     return reservation


def get_all_quantity_products_service() -> list[ProductQuantityModel] | list:
    """
    Возвращает общее количество товаров на складе.
    В реальном приложении данные будут извлекаться из базы данных.
    """

    
    return get_all_quantity_products_fetch() 


def get_total_sum_quantity_service() -> int:
    """
    Возвращает общее количество товаров на складе.
    В реальном приложении данные будут извлекаться из базы данных.
    """
    return sum(product.quantity for product in get_all_quantity_products_fetch())



def get_warehouse_product_by_id_service(id: int) -> ProductModel | None:
    return get_product_by_id_fetch(id)