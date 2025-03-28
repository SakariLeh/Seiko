
# models
from app.models.user import User

# types 
from typing import List
from app.types import ERoleUser

# test database
from app.database import users_db
from app.database import delete_user


def add_new_partner_service(
    phone: str,
    password: str,
    role: str,
    name: str,
    company: str,
    location: str
) -> User:
    """
    Добавление нового клиента в базу данных 
    """

    new_user = User(
        id = len(users_db) + 1,
        phone = phone,
        password = password,
        role = role,
        name = name,
        company = company,
        location = location
    )

    users_db.append(new_user)
    

    return new_user




def delete_partner_service(id: int) -> User:
    """
    Удаление клиента из базы данных
    """ 



    
    
    # Временная функция для удаления клиента
    deleted_user = delete_user(id)

    print("Осталось пользователей", users_db)


    return deleted_user


def get_all_partners_service() -> List[User]:
    """
    Получение всех клиентов из базы данных
    """


    for user in users_db:
        print(user.id, user.phone, user.role, user.name, user.company, user.location)

    

    return users_db


def get_partner_by_id_service(id: int) -> User:
    """
    Получение пользователя по id
    """

    for user in users_db:
        if user.id == id:
            return user

    return None


def edit_partner_service(id: int, name: str, phone: str, role: str, company: str, location: str) -> User:
    """
    Редактирование партнёра
    """

    pass
