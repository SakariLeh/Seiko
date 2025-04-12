

from flask import session, redirect, url_for

# types
from app.types import ERoleUser
from app.types import ESessionUser
from typing import List

# функция для проверки роли и авторизации
def role_required_middleware(required_roles: List[ERoleUser]):
    def decorator(view_func):
        def wrapped_view(*args, **kwargs):
            # Проверяем, есть ли user_id в сессии
            if ESessionUser.USER_ID not in session:
                return redirect(url_for('auth.auth_route'))

            # Проверяем роль пользователя
            user_role = session.get(ESessionUser.ROLE)  # Получаем роль из сессии
            if user_role not in required_roles:
                # Можно перенаправить на страницу с ошибкой или другую страницу
                return redirect(url_for('dashboard.auth_route'))

            return view_func(*args, **kwargs)

        wrapped_view.__name__ = view_func.__name__
        return wrapped_view
    return decorator