from flask import session

from app.types import ESessionUser

from app.models import User




# def index():
#     role = session.get('role') 


#     # Получаем данные пользователя в зависимости от роли
#     user_data = get_user_data(session.get('user_id'))

#     # Недавние заказы для демонстрации
#     recent_orders = get_recent_orders(session.get('user_id'), role)

#     # Определяем заголовок роли для отображения на странице
#     role_title = get_role_title(role)

#     print(session)

#     return render_template(
#         'owner_main_page.html',
#         role=role,
#         role_title=role_title,
#         user_name=user_data['name'],
#         company_name=user_data['company'],
#         location=user_data.get('location', ''),
#         recent_orders=recent_orders
#     )