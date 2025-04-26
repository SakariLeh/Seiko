from flask import session, render_template

from app.types import ESessionUser

from app.models import User

from .dashboard_models import get_user_data, get_recent_orders, get_order_history, get_order_details, get_role_title




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

# def storage():
#     role = session.get('role')
#     user_id = session.get('user_id')
#     company = session.get('company')
#     location = session.get('location')

#     # Получаем все товары на складе
#     products = get_warehouse_products()

#     # Общее количество товаров на складе
#     total_items = sum(product['quantity'] for product in products)

#     return render_template(
#         'warehouse_page.html',
#         products=products,
#         total_items=total_items,
#         role=role,
#         company=company,
#         location=location
#     )

# def reservations():
#     role = session.get('role')
#     user_id = session.get('user_id')
#     company = session.get('company')
#     location = session.get('location')

#     # Получаем бронирования в зависимости от роли
#     if role in ['admin', 'support']:
#         reservations_list = Reservation.get_all_reservations()
#     elif role == 'store':
#         reservations_list = Reservation.get_company_reservations(company)
#     else:  # branch
#         reservations_list = Reservation.get_location_reservations(location)

#     # Получаем информацию о товарах для отображения названий
#     products = {p['id']: p for p in get_warehouse_products()}

#     return render_template(
#         'reservations.html',
#         reservations=reservations_list,
#         products=products,
#         role=role,
#         company=company,
#         location=location
#     )

# def communication():
#     # Перенаправляем на новый маршрут чатов
#     return redirect(url_for('chat.index'))