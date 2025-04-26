from flask import Blueprint, render_template, session, redirect, url_for, abort, jsonify, request
from datetime import datetime

from functools import wraps

from app.models.warehouse import Reservation, get_warehouse_products
from app.routes.warehouse import warehouse_bp

# dashboard_bp = Blueprint('dashboard', __name__)


# Функция-декоратор для проверки авторизации
def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.auth_route'))
        return view_func(*args, **kwargs)

    return wrapped_view


@dashboard_bp.route('/storage')
@login_required
def storage():
    role = session.get('role')
    user_id = session.get('user_id')
    company = session.get('company')
    location = session.get('location')

    # Получаем все товары на складе
    products = get_warehouse_products()

    # Общее количество товаров на складе
    total_items = sum(product['quantity'] for product in products)

    return render_template(
        'warehouse_page.html',
        products=products,
        total_items=total_items,
        role=role,
        company=company,
        location=location
    )


@dashboard_bp.route('/reserve_product', methods=['POST'])
@login_required
def reserve_product():
    # Переадресуем запрос в route из warehouse_bp
    return warehouse_bp.reserve_product()


@dashboard_bp.route('/dashboard')
@login_required
def index():
    role = session.get('role') 


    # Получаем данные пользователя в зависимости от роли
    user_data = get_user_data(session.get('user_id'))

    # Недавние заказы для демонстрации
    recent_orders = get_recent_orders(session.get('user_id'), role)

    # Определяем заголовок роли для отображения на странице
    role_title = get_role_title(role)

    print(session)

    return render_template(
        'owner_main_page.html',
        role=role,
        role_title=role_title,
        user_name=user_data['name'],
        company_name=user_data['company'],
        location=user_data.get('location', ''),
        recent_orders=recent_orders
    )


@dashboard_bp.route('/reservations')
@login_required
def reservations():
    role = session.get('role')
    user_id = session.get('user_id')
    company = session.get('company')
    location = session.get('location')

    # Получаем бронирования в зависимости от роли
    if role in ['admin', 'support']:
        reservations_list = Reservation.get_all_reservations()
    elif role == 'store':
        reservations_list = Reservation.get_company_reservations(company)
    else:  # branch
        reservations_list = Reservation.get_location_reservations(location)

    # Получаем информацию о товарах для отображения названий
    products = {p['id']: p for p in get_warehouse_products()}

    return render_template(
        'reservations.html',
        reservations=reservations_list,
        products=products,
        role=role,
        company=company,
        location=location
    )


@dashboard_bp.route('/communication')
@login_required
def communication():
    # Перенаправляем на новый маршрут чатов
    return redirect(url_for('chat.index'))


# @dashboard_bp.route('/news')
# @login_required
# def news():
#     pass
    #return render_template()


@dashboard_bp.route('/order')
@login_required
def order():
    return "Страница заказа"


@dashboard_bp.route('/order_history')
@login_required
def order_history():
    role = session.get('role')
    user_id = session.get('user_id')

    # Получаем историю заказов
    orders = get_order_history(user_id, role)

    return render_template(
        'order_history_page.html',
        orders=orders,
        role=role
    )


@dashboard_bp.route('/order_details/<order_id>')
@login_required
def order_details(order_id):
    role = session.get('role')
    user_id = session.get('user_id')

    # Получаем данные о заказе
    order = get_order_details(order_id, user_id, role)

    if not order:
        abort(404)  # Если заказ не найден или не принадлежит пользователю

    return f"Детали заказа №{order_id}"


@dashboard_bp.route('/analytics')
@login_required
def analytics():
    role = session.get('role')
    if role not in ['admin', 'support']:
        return redirect(url_for('dashboard.index'))
    return "Страница аналитики"


@dashboard_bp.route('/manage_users')
@login_required
def manage_users():
    role = session.get('role')
    if role != 'admin':
        return redirect(url_for('dashboard.index'))
    return render_template('admin/manage_users_page.html')


