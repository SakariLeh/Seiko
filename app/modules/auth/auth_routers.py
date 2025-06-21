# config
from .auth_config import authConf

# flask 
from flask import Blueprint, render_template, redirect, url_for, request

# services
from .auth_services import login_service
from .auth_services import logout_service
from .auth_services import is_signed_in_service

# middlewares
from app.middlewares import check_auth_middleware


# utils 
from app.utils import validate_phone
from app.utils import validate_password




auth_bp = Blueprint('auth', __name__)


@auth_bp.route(
    authConf.r.get_path("Проверка авторизации пользователя"), 
    methods = authConf.r.get_methods("Проверка авторизации пользователя") 
)
def auth_route():

    

    if is_signed_in_service():
        return redirect(url_for('dashboard.index'))
    return render_template(authConf.r.get_temp("Проверка авторизации пользователя"))



@auth_bp.route(
    authConf.r.get_path("Вход в систему(номер телефона)"), 
    methods = authConf.r.get_methods("Вход в систему(номер телефона)") 
)
def login_phone_route():
    phone = request.form.get('phone', '').strip()

    # Удаляем возможные пробелы, скобки, дефисы и плюсы
    phone = phone.replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('+', '')

    if not validate_phone(phone):
        return render_template(
            'index.html', 
            error='Введите корректный номер телефона в формате 998XXXXXXXXX',              
            phone=phone
        )


    return render_template(
        authConf.r.get_temp("Вход в систему(номер телефона)"),
        phone=phone
    )


@auth_bp.route(
    authConf.r.get_path("Вход в систему(пароль)"), 
    methods = authConf.r.get_methods("Вход в систему(пароль)") 
)
def login_password_route():
    phone = request.form.get('phone', '')
    password = request.form.get('password', '')

    if not validate_password(password):
        return render_template(
            'password.html', 
            error='Введите корректный 4-значный пароль', 
            phone=phone
        )
    
    user = login_service(phone, password)
    print(user)

    if not user:
        return render_template(
            'password.html', 
            error='Неверный номер телефона или пароль', 
            phone=phone
        )
        
    return redirect(url_for(authConf.r.get_temp("Вход в систему(пароль)")))



@auth_bp.route(
    authConf.r.get_path("Выход из системы"), 
    methods = authConf.r.get_methods("Выход из системы") 
)
@check_auth_middleware
def logout_route():
    logout_service()
    return redirect(url_for(authConf.r.get_temp("Выход из системы")))