

from .product_fetch import create_product_fetch, get_product_by_id_fetch, get_all_products_fetch
from .product_models import ProductModel, ProductQuantityModel
from .product_fetch import get_all_quantity_products_fetch

# export нужные функции из модуля наружу

__all__ = [
    "create_product_fetch",
    "get_product_by_id_fetch",
    "get_all_products_fetch",
    "ProductModel",
    "ProductQuantityModel",
    "get_all_quantity_products_fetch"
]


