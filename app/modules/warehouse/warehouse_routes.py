from flask import Blueprint, session, redirect, url_for, jsonify, request
from functools import wraps
from .warehouse_config import warehouseConf
from .warehouse_services import get_warehouse_products, create_reservation_service

# сначало создаём blueprint для модуля
warehouse_bp = Blueprint('warehouse', __name__)

# Функция-декоратор для проверки авторизации
def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.index'))
        return view_func(*args, **kwargs)

    return wrapped_view

# далее создаём роуты для модуля
@warehouse_bp.route(
    warehouseConf.r.get_path("Бронирование товара"),
    methods=warehouseConf.r.get_methods("Бронирование товара")
)

@login_required
def reserve_product():
    role = session.get('role')
    user_id = session.get('user_id')
    company = session.get('company')
    location = session.get('location')

    product_id = request.form.get('product_id', type=int)
    quantity = request.form.get('quantity', type=int)
    target_location = request.form.get('location')

    # Проверка прав доступа для бронирования
    if role == 'branch' and target_location and target_location != location:
        # Отделение может бронировать только для себя
        return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другого отделения'})

    if role == 'store' and company != request.form.get('company'):
        # Компания может бронировать только для своих отделений
        return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другой компании'})

    # Только admin и support могут бронировать для любого отделения

    # Создаем бронирование
    success = create_reservation_service(
        product_id,
        quantity,
        user_id,
        role,
        company,
        target_location or location
    )

    if success:
        return jsonify({'success': True, 'message': 'Товар успешно забронирован'})
    else:
        return jsonify({'success': False, 'message': 'Не удалось забронировать товар'})