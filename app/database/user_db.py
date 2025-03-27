
#types
from typing import List

#models
from app.models.user import User

#types
from app.types import ERoleUser

"""
Временная база данных для пользователей
"""

users_db: List[User] = [
    User(
        id=1,
        phone='998901234567',
        password='1234',
        role=ERoleUser.ADMIN,
        name='Adam Lumberg',
        company='NabievOptics',
        location=None
    ),
    User(
        id=2,
        phone='998907654321',
        password='5678',
        role=ERoleUser.SUPPORT,
        name='Ivan Petrov',
        company='NabievOptics',
        location=None
    ),
    User(
        id=3,
        phone='998909876543',
        password='4321',
        role=ERoleUser.STORE,
        name='Marina Volkova',
        company='Оптика+',
        location=None
    ),
    User(
        id=4,
        phone='998903456789',
        password='9876',
        role=ERoleUser.BRANCH,
        name='Sergey Sidorov',
        company='Оптика+',
        location='ТЦ Галерея'
    )
]


def delete_user(id: int) -> User:


    for i, user in enumerate(users_db):
        if user.id == id:
            users_db.remove(user)
            return user
    return None