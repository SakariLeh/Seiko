from datetime import datetime


class Reservation:
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

    @staticmethod
    def create_reservation(product_id, quantity, user_id, role, company, location=None):
        """
        Создает бронирование товара на основе роли пользователя.
        В реальном приложении это будет сохранено в базе данных.

        Возвращает:
        - True: бронирование успешно создано
        - False: бронирование не удалось (например, недостаточно товара)
        """
        # Проверяем доступность товара
        products = get_warehouse_products()
        product = next((p for p in products if p['id'] == product_id), None)

        if not product or product['quantity'] < quantity:
            return False

        # Генерируем уникальный ID (в реальном приложении это сделает база данных)
        reservation_id = len(reservations) + 1

        reservation = Reservation(
            id=reservation_id,
            product_id=product_id,
            quantity=quantity,
            user_id=user_id,
            company=company,
            location=location,
            status='approved'  # Для демо сразу утверждаем бронирование
        )

        # В реальном приложении здесь будет сохранение в базу данных
        reservations.append(reservation.__dict__)

        # Уменьшаем доступное количество товара
        product['quantity'] -= quantity
        if product['quantity'] == 0:
            product['available'] = False

        return True


# Глобальный список для хранения бронирований (в реальном приложении это будет база данных)
reservations = []


def get_warehouse_products():
    """
    Получает список товаров на складе.
    В реальном приложении данные будут извлекаться из базы данных.
    Этот метод должен совпадать с методом в dashboard.py
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
            'category': 'Линзы'
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