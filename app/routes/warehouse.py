from flask import Blueprint, render_template, session, redirect, url_for, abort, jsonify, request
from datetime import datetime

from functools import wraps

from app.models.warehouse import Reservation

# warehouse_bp = Blueprint('warehouse', __name__)


# Функция-декоратор для проверки авторизации
# def login_required(view_func):
#     @wraps(view_func)
#     def wrapped_view(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('auth.index'))
#         return view_func(*args, **kwargs)

#     return wrapped_view


# Функция для получения тестовых товаров склада
# def get_warehouse_products():
#     """
#     Возвращает список товаров на складе.
#     В реальном приложении данные будут извлекаться из базы данных.
#     """
#     products = [
#         {
#             'id': 1,
#             'name': 'A-ZONE 1.67 BASE 5/3',
#             'description': 'Seiko / ... / Биасферические',
#             'quantity': 24,
#             'available': True,
#             'manufacturer': 'Seiko',
#             'type': 'Биасферические',
#             'category': 'Линзы',
#             'parameters': {
#                 'sphereRight': "-1.00", # dpt
#                 'shereLeft': "-1.00",
#                 'cylinderRight': "+1.00",
#                 'cylinderLeft': "+1.00",
#                 'axisRight': 94,
#                 'axisLeft': 94,
#                 'additionRight': "+1.75",
#                 'additionLeft': "+1.75",
#                 'lensRight': "Brilliance 1.60 Sensity",
#                 'lensLeft': "Brilliance 1.60 Sensity",
#                 'diameterRight': 75,
#                 'diameterLeft': 75,
#                 'corridorLength': 12,
#                 'nearDistanse': "40.00",
#                 'personalDesignCode': "FNCC",
#                 'coatingRight': 'SRB',
#                 'coatingLeft': 'SRB',
#                 'pplRight': 'Sensity Dark Grey', # ppl - Photo/Pola/Filter
#                 'pplLeft': 'Sensity Dark Grey',
#                 'farPupilDistanceRight': '32.00',
#                 'farPupilDistanceLeft': '33.00',
#                 'eyePointHeightRight': '30.00',
#                 'eyePointHeightLeft': '30.00',
#                 'aRight': '50.00',
#                 'aLeft': '50.00',
#                 'bRight': '43.00',
#                 'bLeft': '43.00',
#                 'dbl': '24.00',
#                 'frameType': 'Acetate(HI)',
#                 "cCode": "2233",
#                 'corneaDistanceRight': "14.00",
#                 'corneaDistanceLeft': "14.00",
#                 'pantoscopicAngle': "19.00",
#                 "frameangle": "4.00"
#             }

#         },
#         {
#             'id': 2,
#             'name': 'PREMIUM 1.5 SP',
#             'description': 'HyperOptics / ... / Стандартные',
#             'quantity': 36,
#             'available': True,
#             'manufacturer': 'HyperOptics',
#             'type': 'Стандартные',
#             'category': 'Линзы'
#         },
#         {
#             'id': 3,
#             'name': 'ULTRA 1.74 ASPH',
#             'description': 'VisionTech / ... / Асферические',
#             'quantity': 18,
#             'available': True,
#             'manufacturer': 'VisionTech',
#             'type': 'Асферические',
#             'category': 'Линзы'
#         },
#         {
#             'id': 4,
#             'name': 'PHOTOCHROMIC 1.6',
#             'description': 'OptiLight / ... / Фотохромные',
#             'quantity': 12,
#             'available': True,
#             'manufacturer': 'OptiLight',
#             'type': 'Фотохромные',
#             'category': 'Линзы'
#         },
#         {
#             'id': 5,
#             'name': 'BLUE CUT 1.67',
#             'description': 'Seiko / ... / Защита от синего света',
#             'quantity': 0,
#             'available': False,
#             'manufacturer': 'Seiko',
#             'type': 'Защита от синего света',
#             'category': 'Линзы'
#         }
#     ]
#     return products


# @warehouse_bp.route('/reserve_product', methods=['POST'])
# @login_required
# def reserve_product():
#     role = session.get('role')
#     user_id = session.get('user_id')
#     company = session.get('company')
#     location = session.get('location')

#     product_id = request.form.get('product_id', type=int)
#     quantity = request.form.get('quantity', type=int)
#     target_location = request.form.get('location')

#     # Проверка прав доступа для бронирования
#     if role == 'branch' and target_location and target_location != location:
#         # Отделение может бронировать только для себя
#         return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другого отделения'})

#     if role == 'store' and company != request.form.get('company'):
#         # Компания может бронировать только для своих отделений
#         return jsonify({'success': False, 'message': 'У вас нет прав бронировать товар для другой компании'})

#     # Только admin и support могут бронировать для любого отделения

#     # Создаем бронирование
#     success = Reservation.create_reservation(
#         product_id,
#         quantity,
#         user_id,
#         role,
#         company,
#         target_location or location
#     )

#     if success:
#         return jsonify({'success': True, 'message': 'Товар успешно забронирован'})
#     else:
#         return jsonify({'success': False, 'message': 'Не удалось забронировать товар'})