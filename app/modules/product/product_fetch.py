
from .product_service import (
    create_product_service,
    get_product_by_id_service,
    get_all_products_service
)

from .product_model import ProductModel


from flask import current_app


def create_product_fetch(name: str, description_intro: str, description_text: str) -> ProductModel | None:
    """
    Создает новый продукт в базе данных
    :param name: название продукта
    :param description_intro: краткое описание продукта
    :param description_text: полное описание продукта
    :return: объект ProductModel
    """

    new_product = None 

    try:

        with current_app.app_context():
            new_product = create_product_service(
                name = "Продукт А", 
                description_intro="Краткое описание продукта А",
                description_text="Полное описание продукта А"
            )
    except Exception as e:
        print(f"Ошибка при создании продукта: {e}")
        return new_product
    print("Продукт успешно создан")
    return new_product



def get_product_by_id_fetch(product_id: int) -> ProductModel | None:
    """
    Получает запись из таблицы products по id
    :param product_id: id продукта
    :return: объект ProductModel или None, если запись не найдена
    """


    if not isinstance(product_id, int):
        raise ValueError("product_id должен быть целым числом")
    
    if product_id < 1:
        raise ValueError("product_id должен быть больше 0")

    product = None

    try:
        with current_app.app_context():
            product = get_product_by_id_service(product_id)
    except Exception as e:
        print(f"Ошибка при получении записи таблицы(products) с id {product_id}: {e}")
        return None

    if not product:
        print(f"Запись с id {product_id} не найдена")
        return None
    
    print(product)

    return product

def get_all_products_fetch() -> list[ProductModel] | None:
    """
    Получает все записи из таблицы products
    :return: список объектов ProductModel
    """

    products = None

    try:
        with current_app.app_context():
            products = get_all_products_service()
    except Exception as e:
        print(f"Ошибка при получении всех записей таблицы(products): {e}")
        return None
    
    print(products)

    return products