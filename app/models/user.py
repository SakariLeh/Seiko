class User:
    def __init__(self, id=None, phone=None, password=None, role=None, name=None, company=None, location=None):
        self.id = id
        self.phone = phone
        self.password = password
        self.role = role  # 'admin', 'support', 'store', 'branch'
        self.name = name
        self.company = company
        self.location = location

    # @staticmethod
    # def authenticate(phone, password):
    #     """
    #     Проверяет валидность телефона и пароля.
    #     В реальном приложении здесь будет проверка в базе данных.

    #     Для примера используем тестовые учетные данные:
    #     - Владелец: 998901234567 / 1234
    #     - Сотрудник: 998907654321 / 5678
    #     - Партнёр: 998909876543 / 4321
    #     - Отдел партнёра: 998903456789 / 9876
    #     """
    #     test_users = {
    #         '998901234567': {
    #             'password': '1234',
    #             'role': 'admin',    # Владелец
    #             'name': 'Adam Lumberg',
    #             'company': 'NabievOptics',
    #             'location': None
    #         },
    #         '998907654321': {
    #             'password': '5678',
    #             'role': 'support',  # Сотрудники владельца
    #             'name': 'Ivan Petrov',
    #             'company': 'NabievOptics',
    #             'location': None
    #         },
    #         '998909876543': {
    #             'password': '4321',
    #             'role': 'store',    # Владелец компании-партнёра
    #             'name': 'Marina Volkova',
    #             'company': 'Оптика+',
    #             'location': None
    #         },
    #         '998903456789': {
    #             'password': '9876',
    #             'role': 'branch',   # Сотрудник(филиал) компании-партнёра
    #             'name': 'Sergey Sidorov',
    #             'company': 'Оптика+',
    #             'location': 'ТЦ Галерея'
    #         }
    #     }

    #     if phone in test_users and test_users[phone]['password'] == password:
    #         user_data = test_users[phone]
    #         user = User(
    #             id=1,  # В реальном приложении будет ID из базы данных
    #             phone=phone,
    #             password=password,
    #             role=user_data['role'],
    #             name=user_data['name'],
    #             company=user_data['company'],
    #             location=user_data['location']
    #         )
    #         return user
    #     return None

    def get_role_display(self):
        """Возвращает отображаемое название роли на русском"""
        role_map = {
            'admin': 'владелец',
            'support': 'сотрудник',
            'store': 'партнёр',
            'branch': f'отдел партнёра {self.location}' if self.location else 'отдел партнёра'
        }
        return role_map.get(self.role, self.role)