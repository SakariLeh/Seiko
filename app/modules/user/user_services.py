
# models
from .user_model import UserModel

# types 
from typing import List





def add_new_user_service(
    phone: str,
    password: str,
    role: str,
    name: str,
    company: str,
    location: str
) -> UserModel:
    """
    Добавление нового клиента в базу данных 
    """
    new_user = UserModel(
        phone=phone,
        password=password,
        role=role,
        name=name,
        company=company,
        location=location
    )  

    new_user.save()

    return new_user


def get_user_name_service(user_id: int) -> UserModel:
    user = UserModel.query.get(user_id)
    return user.name if user else "Неизвестно"


def delete_user_service(id: int) -> UserModel | None:
    """
    Удаление клиента из базы данных
    """ 
    deleted_user = UserModel.query.filter_by(id=id).first() 

    if not deleted_user:
        return None

    deleted_user.delete()

    return deleted_user
    
    





def get_all_users_service() -> List[UserModel]:
    """
    Получение всех клиентов из базы данных
    """

    return UserModel.query.all() 


def get_user_by_id_service(id: int) -> UserModel:
    """
    Получение пользователя по id
    """

    return UserModel.query.get(id) 


def edit_user_service(id: int, name: str, phone: str, role: str, company: str, location: str) -> UserModel:
    """
    Редактирование партнёра
    """

    user = get_user_by_id_service(id)

    user.name = name
    user.phone = phone
    user.role = role
    user.company = company
    user.location = location

    user.save()

    return user 
