# config
from .auth_config import authConf

# flask 
from flask import Blueprint, render_template, redirect, url_for, session

# services
from .auth_services import logout_service
from .auth_services import is_logged_in_service

# middlewares
from app.middlewares import check_auth_middleware


auth_bp = Blueprint('auth', __name__)


@auth_bp.route(
    authConf.r.get_path("Проверка авторизации пользователя"), 
    methods = authConf.r.get_methods("Проверка авторизации пользователя") 
)
def auth_route():

    if is_logged_in_service():
        return redirect(url_for('dashboard.index'))
    return render_template(authConf.r.get_template("Проверка авторизации пользователя"))



@auth_bp.route(
    authConf.r.get_path("Вход в систему(номер телефона)"), 
    methods = authConf.r.get_methods("Вход в систему(номер телефона)") 
)
def login_phone_route():
    return render_template(authConf.r.get_template("Вход в систему(номер телефона)"))


@auth_bp.route(
    authConf.r.get_path("Вход в систему(пароль)"), 
    methods = authConf.r.get_methods("Вход в систему(пароль)") 
)
def login_password_route():
    return render_template(authConf.r.get_template("Вход в систему(пароль)"))


@auth_bp.route(
    authConf.r.get_path("Выход из системы"), 
    methods = authConf.r.get_methods("Выход из системы") 
)
@check_auth_middleware
def logout_route():
    logout_service()
    return redirect(authConf.r.get_template("Вход в систему"))