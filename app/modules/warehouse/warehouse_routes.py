# flask
from flask import Blueprint, session, request, render_template


# config
from .warehouse_config import warehouseConf



# services
from .warehouse_services import get_warehouse_products_service
from app.modules.auth import get_info_auth_service
from .warehouse_services import get_all_quantity_products_service
from .warehouse_services import get_total_sum_quantity_service
from .warehouse_services import get_warehouse_product_by_id_service

# middlewares
from app.middlewares import check_auth_middleware, role_required_middleware


# types 
from app.types import ERoleUser, ESessionUser



warehouse_bp = Blueprint('warehouse', __name__)

# @warehouse_bp.route(
#     warehouseConf.r.get_path("Бронирование товара"),
#     methods=warehouseConf.r.get_methods("Бронирование товара")
# )

# @role_required_middleware([ERoleUser.ADMIN, ERoleUser.SUPPORT])
# def reserve_product_route():
#     """
#     Страница для бронирования товара
#     """

#     # информация о сессии пользователя
#     info_auth = get_info_auth_service()


#     role = info_auth[ESessionUser.ROLE]
#     user_id = info_auth[ESessionUser.USER_ID]
#     company = info_auth[ESessionUser.COMPANY]
#     location = info_auth[ESessionUser.LOCATION]

#     product_id = request.form.get('product_id', type=int)
#     quantity = request.form.get('quantity', type=int)
#     target_location = request.form.get('location')

#     # Проверка прав доступа для бронирования
#     if role == ERoleUser.BRANCH and target_location and target_location != location:
#         # Отделение может бронировать только для себя
#         return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другого отделения'})

#     if role == ERoleUser.STORE and company != request.form.get('company'):
#         # Компания может бронировать только для своих отделений
#         return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другой компании'})

#     # Только admin и support могут бронировать для любого отделения

#     # Создаем бронирование
#     new_reservation = create_reservation_service(
#         product_id,
#         quantity,
#         user_id,
#         role,
#         company,
#         target_location or location
#     )

#     if new_reservation:
#         return jsonify({'success': success, 'message': 'Бронирование успешно создано'})
#     else:
#         return jsonify({'success': False, 'message': 'Произошла ошибка при создании бронирования'})

    


@warehouse_bp.route(
    warehouseConf.r.get_path("Все товары на складе"),
    methods=warehouseConf.r.get_methods("Все товары на складе")
)

@check_auth_middleware
def warehouse_storage_route():
    """
    Отображение страницы склада
    """

    # информация о сессии пользователя
    info_auth = get_info_auth_service()
    

    # Получаем все товары на складе
    products_all = get_warehouse_products_service()

    # получение всех количество товаров на складе
    products_quantity = get_all_quantity_products_service()

  
    # Общее количество товаров на складе
    total_items = get_total_sum_quantity_service()

    
    return render_template(
        warehouseConf.r.get_temp("Все товары на складе"),
        zip = zip,
        products=products_all,
        products_quantity = products_quantity,
        total_items=total_items,
        role=info_auth[ESessionUser.ROLE],
        company=info_auth[ESessionUser.COMPANY],
        location=info_auth[ESessionUser.LOCATION]
    )


@warehouse_bp.route(
    warehouseConf.r.get_path("Подробнее о товаре на складе"),
    methods=warehouseConf.r.get_methods("Подробнее о товаре на складе")
)

@check_auth_middleware
def warehouse_product_router(id: int):
    """
    Подробнее о товаре на складе
    """

    product = get_warehouse_product_by_id_service(id)

    return render_template(
        warehouseConf.r.get_temp("Подробнее о товаре на складе"), product = product
    )