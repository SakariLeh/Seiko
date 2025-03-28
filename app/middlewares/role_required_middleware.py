

from flask import session, redirect, url_for
from app.types import ERoleUser

def role_required_middleware(required_role: ERoleUser):
    def decorator(view_func):
        def wrapped_view(*args, **kwargs):
            # Проверяем, есть ли user_id в сессии
            if 'user_id' not in session:
                return redirect(url_for('auth.index'))

            # Проверяем роль пользователя
            user_role = session.get('role')  # Получаем роль из сессии
            if user_role != required_role:
                # Можно перенаправить на страницу с ошибкой или другую страницу
                return redirect(url_for('dashboard.index'))

            return view_func(*args, **kwargs)

        wrapped_view.__name__ = view_func.__name__
        return wrapped_view
    return decorator