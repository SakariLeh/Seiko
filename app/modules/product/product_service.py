
from .product_models import ProductModel, ProductQuantityModel
from app.infrastructure import db 


def create_product_service(name: str, description_intro: str, description_text: str) -> ProductModel:
    """
    Создает новый продукт в базе данных
    :param name: название продукта
    :param description_intro: краткое описание продукта
    :param description_text: полное описание продукта
    :return: объект ProductModel
    """
    product = ProductModel(
        name= name, 
        description_intro=description_intro,
        description_text=description_text
    )
    db.session.add(product)
    db.session.commit()
    return product


def get_product_by_id_service(product_id: int) -> ProductModel:
    """
    Получает запись из таблицы products по id
    :param product_id: id продукта
    :return: объект ProductModel или None, если запись не найдена
    """
    return ProductModel.query.get(product_id)


def get_all_products_service() -> list[ProductModel]:
    """
    Получает все записи из таблицы products
    :return: список объектов ProductModel
    """
    return ProductModel.query.all()


def get_quantity_products_service() -> int:
    """
    Получает количество продуктов в базе данных
    :return: количество продуктов
    """
    return ProductQuantityModel.query.all()