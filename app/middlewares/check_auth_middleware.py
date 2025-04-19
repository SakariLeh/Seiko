from flask import session, redirect, url_for

#types 
from app.types import ESessionUser

# функция для проверки авторизации
def check_auth_middleware(view_func):
    def wrapped_view(*args, **kwargs):
        if ESessionUser.USER_ID not in session:
            return redirect(url_for('auth.auth_route'))
        return view_func(*args, **kwargs)

    wrapped_view.__name__ = view_func.__name__
    return wrapped_view