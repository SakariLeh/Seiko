
from flask import Blueprint, render_template, request, redirect, url_for

# types 
from app.types import ERoleUser, EMethod

# services
from .admin_service import add_new_partner_service
from .admin_service import get_all_partners_service
from .admin_service import delete_partner_service
from .admin_service import get_partner_by_id_service
from .admin_service import edit_partner_service

# middlewares
from app.middlewares import role_required_middleware


# utils
from app.utils import validate_phone, validate_password, validate_role



admin_bp = Blueprint('admin', __name__)

"""
Пути только для администратора(Владелец)
"""



@admin_bp.route('/admin/add_new_partner', methods=[EMethod.GET, EMethod.POST])
@role_required_middleware(ERoleUser.ADMIN)
def add_new_partner_route():
    """
    Страница для добавления нового клиента
    """

    if request.method == EMethod.POST:

        if not validate_phone(request.form['phone']):
            return render_template('admin/add_partner_page.html', error="Неверный номер телефона")
        
        if not validate_password(request.form['password']):
            return render_template('admin/add_partner_page.html', error="Неверный пароль")
        
        if not validate_role(request.form['role']):
            return render_template('admin/add_partner_page.html', error="Неверная роль")
        
        
        

        user = add_new_partner_service(
            phone=request.form['phone'],
            password=request.form["password"],
            role=request.form['role'],
            name=request.form['name'],
            company=request.form['company'],
            location=request.form['location']
        )

        print("id нового клиента", user)

        return redirect(url_for('admin.partner_added_successfully_route', id=user.id))
     

    
    return render_template('admin/add_partner_page.html')

@admin_bp.route("/admin/partner_added_successfully/<int:id>")
@role_required_middleware(ERoleUser.ADMIN)
def partner_added_successfully_route(id: int):
    """
    Страница с успешной регистрацией
    """

    user = get_partner_by_id_service(id)

    return render_template('admin/partner_added_successfully.html', user=user)


@admin_bp.route('/admin/delete_partner/<int:id>', methods=[EMethod.GET, EMethod.POST])
@role_required_middleware(ERoleUser.ADMIN)
def delete_partner_route(id: int):
    """
    Удаление клиента
    """

    if request.method == EMethod.POST:
        deleted_user = delete_partner_service(id)
        print("Удаленный пользователь", deleted_user)

        return redirect(url_for('admin.all_partners_route'))

    user = get_partner_by_id_service(id)



    return render_template('admin/delete_partner.html', user=user)
    


@admin_bp.get("/admin/all_partner")
@role_required_middleware(ERoleUser.ADMIN)
def all_partners_route(): 
    """
    Получение всех клиентов
    """

    users = get_all_partners_service()
    return render_template('admin/all_partner.html', users=users)


@admin_bp.route('/admin/edit_partner/<int:id>', methods=[EMethod.GET, EMethod.POST])
@role_required_middleware(ERoleUser.ADMIN)
def edit_partner_route(id: int):
    """
    Страница для редактирования партнёра
    """

    if request.method == EMethod.POST:
        user = edit_partner_service(id, request.form['name'], request.form['phone'], request.form['role'], request.form['company'], request.form['location'])

        return redirect(url_for('admin.partner_added_successfully_route', id=user.id))

    user = get_partner_by_id_service(id)

    return render_template('admin/edit_partner.html', user=user)