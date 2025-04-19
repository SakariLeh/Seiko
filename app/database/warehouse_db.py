# types
from typing import List, Dict, Optional, Any

# models
from app.models.warehouse import Product, Reservation
from app.models.user import User

# types
from app.types import ERoleUser

"""
Временная база данных для товаров на складе и бронирований
"""

# Инициализация базы данных товаров
products_db: List[Product] = [
    Product(
        id=1,
        name='A-ZONE 1.67 BASE 5/3',
        description='Seiko / ... / Биасферические',
        quantity=24,
        available=True,
        manufacturer='Seiko',
        type='Биасферические',
        category='Линзы'
    ),
    Product(
        id=2,
        name='PREMIUM 1.5 SP',
        description='HyperOptics / ... / Стандартные',
        quantity=36,
        available=True,
        manufacturer='HyperOptics',
        type='Стандартные',
        category='Линзы'
    ),
    Product(
        id=3,
        name='ULTRA 1.74 ASPH',
        description='VisionTech / ... / Асферические',
        quantity=18,
        available=True,
        manufacturer='VisionTech',
        type='Асферические',
        category='Линзы'
    ),
    Product(
        id=4,
        name='PHOTOCHROMIC 1.6',
        description='OptiLight / ... / Фотохромные',
        quantity=12,
        available=True,
        manufacturer='OptiLight',
        type='Фотохромные',
        category='Линзы'
    ),
    Product(
        id=5,
        name='BLUE CUT 1.67',
        description='Seiko / ... / Защита от синего света',
        quantity=0,
        available=False,
        manufacturer='Seiko',
        type='Защита от синего света',
        category='Линзы'
    )
]

# Инициализация базы данных бронирований
reservations_db: List[Reservation] = []


def get_product_by_id(product_id: int) -> Optional[Product]:
    """
    Получение товара по ID
    """
    for product in products_db:
        if product.id == product_id:
            return product
    return None


def get_all_products() -> List[Product]:
    """
    Получение всех товаров
    """
    return products_db


def update_product_quantity(product_id: int, new_quantity: int) -> Optional[Product]:
    """
    Обновление количества товара
    """
    product = get_product_by_id(product_id)
    if product:
        product.quantity = new_quantity
        product.available = new_quantity > 0
        return product
    return None


def create_reservation(product_id: int, quantity: int, user: User) -> Optional[Reservation]:
    """
    Создание бронирования товара
    """
    product = get_product_by_id(product_id)

    # Проверка наличия товара и достаточного количества
    if not product or not product.available or product.quantity < quantity:
        return None

    # Определение статуса бронирования в зависимости от роли
    # Администраторы и поддержка получают автоматическое подтверждение
    initial_status = 'approved' if user.role in [ERoleUser.ADMIN, ERoleUser.SUPPORT] else 'pending'

    # Создание нового бронирования
    reservation_id = len(reservations_db) + 1
    reservation = Reservation(
        id=reservation_id,
        product_id=product_id,
        quantity=quantity,
        user_id=user.id,
        company=user.company,
        location=user.location,
        status=initial_status
    )

    # Добавление бронирования в базу
    reservations_db.append(reservation)

    # Если бронирование подтверждено, уменьшаем количество доступного товара
    if initial_status == 'approved':
        product.quantity -= quantity
        product.available = product.quantity > 0

    return reservation


def get_reservations_by_user(user_id: int) -> List[Reservation]:
    """
    Получение бронирований пользователя
    """
    return [r for r in reservations_db if r.user_id == user_id]


def get_all_reservations() -> List[Reservation]:
    """
    Получение всех бронирований
    """
    return reservations_db


def get_reservation_by_id(reservation_id: int) -> Optional[Reservation]:
    """
    Получение бронирования по ID
    """
    for reservation in reservations_db:
        if reservation.id == reservation_id:
            return reservation
    return None


def update_reservation_status(reservation_id: int, new_status: str) -> Optional[Reservation]:
    """
    Обновление статуса бронирования
    """
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        return None

    old_status = reservation.status
    reservation.status = new_status

    # Если статус изменился с pending на approved, уменьшаем количество товара
    if old_status == 'pending' and new_status == 'approved':
        product = get_product_by_id(reservation.product_id)
        if product:
            product.quantity -= reservation.quantity
            product.available = product.quantity > 0

    # Если статус изменился с approved на rejected, возвращаем товар на склад
    elif old_status == 'approved' and new_status == 'rejected':
        product = get_product_by_id(reservation.product_id)
        if product:
            product.quantity += reservation.quantity
            product.available = True

    return reservation


def delete_reservation(reservation_id: int) -> Optional[Reservation]:
    """
    Удаление бронирования
    """
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        return None

    # Если бронирование было подтверждено, возвращаем товар на склад
    if reservation.status == 'approved':
        product = get_product_by_id(reservation.product_id)
        if product:
            product.quantity += reservation.quantity
            product.available = True

    # Удаляем бронирование из базы
    reservations_db.remove(reservation)
    return reservation