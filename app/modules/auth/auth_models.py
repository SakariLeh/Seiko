# # models
# from app.models import User


# # types
# from app.types import ESessionUser
# COUNT_AUTH = 0

# class AuthModel(User):
    


#     def __init__(self, id=None, phone=None, password=None, role=None, name=None, company=None, location=None):
#         super().__init__(id, phone, password, role, name, company, location)

#     @staticmethod
#     def authenticate(phone: str, password: str) -> User | None:
#         """
#         Проверяет валидность телефона и пароля.
#         В реальном приложении здесь будет проверка в базе данных.

#         Для примера используем тестовые учетные данные:
#         - Владелец: 998901234567 / 1234
#         - Сотрудник: 998907654321 / 5678
#         - Партнёр: 998909876543 / 4321
#         - Отдел партнёра: 998903456789 / 9876
#         """
#         test_users = {
#             '998901234567': {
#                 'password': '1234',
#                 'role': 'admin',    # Владелец
#                 'name': 'Adam Lumberg',
#                 'company': 'NabievOptics',
#                 'location': None
#             },
#             '998907654321': {
#                 'password': '5678',
#                 'role': 'support',  # Сотрудники владельца
#                 'name': 'Ivan Petrov',
#                 'company': 'NabievOptics',
#                 'location': None
#             },
#             # '998909876543': {
#             #     'password': '4321',
#             #     'role': 'store',    # Владелец компании-партнёра
#             #     'name': 'Marina Volkova',
#             #     'company': 'Оптика+',
#             #     'location': None
#             # },
#             '998903456789': {
#                 'password': '9876',
#                 'role': 'branch',   # Сотрудник(филиал) компании-партнёра
#                 'name': 'Sergey Sidorov',
#                 'company': 'Оптика+',
#                 'location': 'ТЦ Галерея'
#             },

#             "998909876543": {
#                 'password': '4321',
#                 'role': 'admin',    # Владелец
#                 'name': 'User 2',
#                 'company': 'NabievOptics',
#                 'location': None
#             }
#         }

#         if phone in test_users and test_users[phone]['password'] == password:
#             user_data = test_users[phone]
#             global COUNT_AUTH
#             COUNT_AUTH += 1
#             user = User(
#                 id=COUNT_AUTH,  # В реальном приложении будет ID из базы данных
#                 phone=phone,
#                 password=password,
#                 role=user_data[ESessionUser.ROLE],
#                 name=user_data[ESessionUser.NAME],
#                 company=user_data[ESessionUser.COMPANY],
#                 location=user_data[ESessionUser.LOCATION]
#             )
#             return user
        

      

#         return None

from app.modules.user import UserModel  
from werkzeug.security import check_password_hash

class AuthModel:
    @staticmethod
    def authenticate_user(phone: str, password: str) -> UserModel | None:
        user = UserModel.query.filter_by(phone=phone).first()
        if user and check_password_hash(user.password, password):  # если пароли хэшируются
            return user
        return None
