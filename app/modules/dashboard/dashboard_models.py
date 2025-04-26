
# Тестовый импорт. Удалить потом!!!
from dashboard_common_test_data import test_orders, test_recent_orders, test_user_names, test_role_titles


from flask import session

# ИММИТАЦИЯ РАБОТЫ С БД
def get_user_data(user_id):
    """
    Получает данные пользователя из базы данных.
    В демонстрационных целях возвращает тестовые данные.
    """

    test_data = test_user_names

    role = session.get('role')
    return test_data.get(role, {})


def get_recent_orders(user_id, role):
    """
    Получает список недавних заказов пользователя.
    В демонстрационных целях возвращает тестовые данные.
    """
    
    recent_orders = test_recent_orders

    return recent_orders


def get_order_history(user_id, role):
    """
    Получает полную историю заказов пользователя.
    В демонстрационных целях возвращает тестовые данные.
    """
    # Демонстрационные заказы для истории
    orders = test_orders

    return orders


def get_order_details(order_id, user_id, role):
    """
    Получает детальную информацию о конкретном заказе.
    В демонстрационных целях проверяет, есть ли заказ с таким ID
    в тестовых данных.
    """
    orders = get_order_history(user_id, role)
    for order in orders:
        if order['id'] == order_id:
            return order
    return None


def get_role_title(role):
    """
    Возвращает название роли для отображения на странице.
    """
    role_titles = test_role_titles

    return role_titles.get(role, 'Пользователь')