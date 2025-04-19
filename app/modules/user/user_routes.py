
from flask import Blueprint, render_template, request, redirect, url_for

# types 
from app.types import ERoleUser, EMethod

# services
from .user_service import add_new_partner_service
from .user_service import get_all_partners_service
from .user_service import delete_partner_service
from .user_service import get_partner_by_id_service
from .user_service import edit_partner_service

# middlewares
from app.middlewares import role_required_middleware


# utils
from app.utils import validate_phone, validate_password, validate_role

# config
from .user_config import userConf

user_bp = Blueprint('user', __name__)

"""
Пути только для администратора(Владелец)
"""



@user_bp.route(
    userConf.r.get_path("Добавление нового партнёра"), 
    methods=userConf.r.get_methods("Добавление нового партнёра")
)
@role_required_middleware([ERoleUser.ADMIN, ERoleUser.STORE])
def add_new_partner_route():
    """
    Страница для добавления нового клиента
    """

    if request.method == EMethod.POST:

        if not validate_phone(request.form['phone']):
            return render_template('user/add_partner_page.html', error="Неверный номер телефона")
        
        if not validate_password(request.form['password']):
            return render_template('user/add_partner_page.html', error="Неверный пароль")
        
        if not validate_role(request.form['role']):
            return render_template('user/add_partner_page.html', error="Неверная роль")
        
        
        

        user = add_new_partner_service(
            phone=request.form['phone'],
            password=request.form["password"],
            role=request.form['role'],
            name=request.form['name'],
            company=request.form['company'],
            location=request.form['location']
        )

        print("id нового клиента", user)

        return redirect(url_for('user.partner_added_successfully_route', id=user.id))
     

    
    return render_template(userConf.r.get_temp("Добавление нового партнёра"))

@user_bp.route(
    userConf.r.get_path("Страница с успешной регистрацией"), 
    methods = userConf.r.get_methods("Страница с успешной регистрацией")
)
@role_required_middleware([ERoleUser.ADMIN, ERoleUser.STORE])
def partner_added_successfully_route(id: int):
    """
    Страница с успешной регистрацией
    """

    user = get_partner_by_id_service(id)

    return render_template(userConf.r.get_temp("Страница с успешной регистрацией"), user=user)


@user_bp.route(
    userConf.r.get_path("Удаление партнёра"), 
    methods = userConf.r.get_methods("Удаление партнёра")
)
@role_required_middleware([ERoleUser.ADMIN, ERoleUser.STORE])
def delete_partner_route(id: int):
    """
    Удаление клиента
    """

    if request.method == EMethod.POST:
        deleted_user = delete_partner_service(id)
        print("Удаленный пользователь", deleted_user)

        return redirect(url_for('user.all_partners_route'))

    user = get_partner_by_id_service(id)



    return render_template(userConf.r.get_temp("Удаление партнёра"), user=user)
    


@user_bp.route(
    userConf.r.get_path("Получение всех партнёра"), 
    methods = userConf.r.get_methods("Получение всех партнёра")
)
@role_required_middleware([ERoleUser.ADMIN, ERoleUser.STORE])
def all_partners_route(): 
    """
    Получение всех клиентов
    """

    users = get_all_partners_service()
    return render_template(userConf.r.get_temp("Получение всех партнёра"), users=users, ERoleUser=ERoleUser)


@user_bp.route(
    userConf.r.get_path("Изменения партнёра"), 
    methods = userConf.r.get_methods("Изменения партнёра")
)
@role_required_middleware([ERoleUser.ADMIN, ERoleUser.STORE])
def edit_partner_route(id: int):
    """
    Страница для редактирования партнёра
    """

    if request.method == EMethod.POST:
        
        user = edit_partner_service(id, request.form['name'], request.form['phone'], request.form['role'], request.form['company'], request.form['location'])
        
        return redirect(url_for('user.partner_added_successfully_route', id=user.id))

    user = get_partner_by_id_service(id)
   

    return render_template(userConf.r.get_temp("Изменения партнёра"), user=user, ERoleUser=ERoleUser)