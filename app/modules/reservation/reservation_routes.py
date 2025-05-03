


# flask
from flask import Blueprint, session, request, render_template, jsonify

# config
from .reservation_config import reservationConf



# services
from .reservation_service import create_reservation_service
from app.modules.auth import get_info_auth_service


# middlewares
from app.middlewares import role_required_middleware


# types 
from app.types import ERoleUser, ESessionUser

reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route(
    reservationConf.r.get_path("Бронирование товара"),
    methods=reservationConf.r.get_methods("Бронирование товара")
)

@role_required_middleware([ERoleUser.ADMIN, ERoleUser.SUPPORT])
def reserve_product_route():
    """
    Страница для бронирования товара
    """

    # информация о сессии пользователя
    info_auth = get_info_auth_service()


    role = info_auth[ESessionUser.ROLE]
    user_id = info_auth[ESessionUser.USER_ID]
    company = info_auth[ESessionUser.COMPANY]
    location = info_auth[ESessionUser.LOCATION]

    product_id = request.form.get('product_id', type=int)
    quantity = request.form.get('quantity', type=int)
    target_location = request.form.get('location')

    

    # Проверка прав доступа для бронирования
    if role == ERoleUser.BRANCH and target_location and target_location != location:
        # Отделение может бронировать только для себя
        return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другого отделения'})

    if role == ERoleUser.STORE and company != request.form.get('company'):
        # Компания может бронировать только для своих отделений
        return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другой компании'})

    # Только admin и support могут бронировать для любого отделения

    # Создаем бронирование
    new_reservation = create_reservation_service(
        product_id,
        quantity,
        user_id,
        role,
        company,
        target_location or location or "location"
    )

    if new_reservation:
        return jsonify({'success': True, 'message': 'Бронирование успешно создано'})
    else:
        return jsonify({'success': False, 'message': 'Произошла ошибка при создании бронирования'})