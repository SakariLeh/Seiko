
# models
from app.models.user import User

# types 
from typing import List
from app.types import ERoleUser

# test database
from app.database import users_db
from app.database import delete_user


def add_new_client_service(
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




def delete_client_service(id: int) -> User:
    """
    Удаление клиента из базы данных
    """ 



    
    

    deleted_user = delete_user(id)

    print("Осталось пользователей", users_db)


    return deleted_user


def get_all_clients_service() -> List[User]:
    """
    Получение всех клиентов из базы данных
    """


    for user in users_db:
        print(user.id, user.phone, user.role, user.name, user.company, user.location)

    

    return users_db
