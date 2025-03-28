
from flask import Blueprint, render_template, request, redirect, url_for

# types 
from app.types import ERoleUser

# services
from .admin_service import add_new_client_service
from .admin_service import get_all_clients_service
from .admin_service import delete_client_service

# middlewares
from app.middlewares import role_required_middleware




admin_bp = Blueprint('admin', __name__)

"""
Пути только для администратора(Владелец)
"""

@admin_bp.route('/admin/add_new_client', methods=['GET', 'POST'])
@role_required_middleware(ERoleUser.ADMIN)
def add_new_client_route():
    """
    Страница для добавления нового клиента
    """

    if request.method == 'POST':
        user = add_new_client_service(
            phone=request.form['phone'],
            password=request.form['password'],
            role=ERoleUser.BRANCH,
            name=request.form['name'],
            company=request.form['company'],
            location=request.form['location']
        )

        print("id нового клиента", user.id)

        # return redirect(url_for('admin.all_client'))
        return f"It's add new client {user.id}"

    
    # return render_template('admin/add_new_client.html')
    return "It's add new client"


@admin_bp.delete('/admin/remove_client/<int:id>')
@role_required_middleware(ERoleUser.ADMIN)
def delete_client_route(id: int):
    """
    Удаление клиента
    """

    deleted_user = delete_client_service(id)
    print("Удаленный пользователь", deleted_user)


    # return render_template('admin/remove_client.html')
    return "It's remove client"


@admin_bp.get("/admin/all_client")
@role_required_middleware(ERoleUser.ADMIN)
def all_client_route(): 
    """
    Получение всех клиентов
    """


    users = get_all_clients_service()
    # return render_template('admin/all_client.html', users=users)
    return "It's all client"
