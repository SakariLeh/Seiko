from datetime import datetime
from typing import List, Dict, Any, Optional


class Product:
    def __init__(self, id=None, name=None, description=None, quantity=None, available=True,
                 manufacturer=None, type=None, category=None):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.available = available
        self.manufacturer = manufacturer
        self.type = type
        self.category = category


class Reservation:
    # Хранилище бронирований в памяти
    _reservations = []
    _reservation_id_counter = 1

    def __init__(self, id=None, product_id=None, quantity=None, user_id=None, company=None,
                 location=None, timestamp=None, status='pending'):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.user_id = user_id
        self.company = company
        self.location = location
        self.timestamp = timestamp or datetime.now()
        self.status = status  # 'pending', 'approved', 'rejected'

    @classmethod
    def create_reservation(cls, product_id, quantity, user_id, role, company, location):
        """
        Создает новое бронирование товара

        :param product_id: ID товара
        :param quantity: Количество
        :param user_id: ID пользователя
        :param role: Роль пользователя
        :param company: Компания
        :param location: Отделение
        :return: True если бронирование успешно создано, иначе False
        """
        try:
            # Проверяем наличие товара и достаточное количество
            products = get_warehouse_products()
            product = next((p for p in products if p['id'] == product_id), None)

            if not product:
                return False

            if not product['available'] or product['quantity'] < quantity:
                return False

            # Создаем бронирование
            reservation = cls(
                id=cls._reservation_id_counter,
                product_id=product_id,
                quantity=quantity,
                user_id=user_id,
                company=company,
                location=location
            )

            # Увеличиваем счетчик ID для следующего бронирования
            cls._reservation_id_counter += 1

            # Добавляем бронирование в хранилище
            cls._reservations.append(reservation)

            # Обновляем доступное количество товара
            product['quantity'] -= quantity
            if product['quantity'] == 0:
                product['available'] = False

            return True
        except Exception as e:
            print(f"Error creating reservation: {e}")
            return False

    @classmethod
    def get_all_reservations(cls):
        """
        Возвращает все бронирования

        :return: Список всех бронирований
        """
        return cls._reservations

    @classmethod
    def get_user_reservations(cls, user_id):
        """
        Возвращает все бронирования пользователя

        :param user_id: ID пользователя
        :return: Список бронирований пользователя
        """
        return [r for r in cls._reservations if r.user_id == user_id]

    @classmethod
    def get_company_reservations(cls, company):
        """
        Возвращает все бронирования компании

        :param company: Название компании
        :return: Список бронирований компании
        """
        return [r for r in cls._reservations if r.company == company]

    @classmethod
    def get_location_reservations(cls, location):
        """
        Возвращает все бронирования отделения

        :param location: Название отделения
        :return: Список бронирований отделения
        """
        return [r for r in cls._reservations if r.location == location]


# Функция получения товаров перенесена из routes/warehouse.py для избежания циклического импорта
def get_warehouse_products():
    """
    Возвращает список товаров на складе.
    В реальном приложении данные будут извлекаться из базы данных.
    """
    products = [
        {
            'id': 1,
            'name': 'A-ZONE 1.67 BASE 5/3',
            'description': 'Seiko / ... / Биасферические',
            'quantity': 24,
            'available': True,
            'manufacturer': 'Seiko',
            'type': 'Биасферические',
            'category': 'Линзы',
            'parameters': {
                # ... параметры товара
            }
        },
        {
            'id': 2,
            'name': 'PREMIUM 1.5 SP',
            'description': 'HyperOptics / ... / Стандартные',
            'quantity': 36,
            'available': True,
            'manufacturer': 'HyperOptics',
            'type': 'Стандартные',
            'category': 'Линзы'
        },
        {
            'id': 3,
            'name': 'ULTRA 1.74 ASPH',
            'description': 'VisionTech / ... / Асферические',
            'quantity': 18,
            'available': True,
            'manufacturer': 'VisionTech',
            'type': 'Асферические',
            'category': 'Линзы'
        },
        {
            'id': 4,
            'name': 'PHOTOCHROMIC 1.6',
            'description': 'OptiLight / ... / Фотохромные',
            'quantity': 12,
            'available': True,
            'manufacturer': 'OptiLight',
            'type': 'Фотохромные',
            'category': 'Линзы'
        },
        {
            'id': 5,
            'name': 'BLUE CUT 1.67',
            'description': 'Seiko / ... / Защита от синего света',
            'quantity': 0,
            'available': False,
            'manufacturer': 'Seiko',
            'type': 'Защита от синего света',
            'category': 'Линзы'
        }
    ]
    return products