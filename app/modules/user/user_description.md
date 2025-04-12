Description:

Модуль для работы с логикой пользователя.
Основные функции:
- добавление нового клиента
- удаление клиента
- получение всех клиентов


Paths:

/user/add_new_partner (GET, POST) - добавление нового партнёра
/user/partner_added_successfully/<int:id> (GET) - страница с успешной регистрацией
/user/delete_partner/<int:id> (GET, POST) - удаление партнёра
/user (GET) - получение всех партнёров
/user/edit_partner/<int:id> (GET, POST) - редактирование партнёра

Templates:




Tests:

python3.12 -m unittest app/modules/user/user_test.py


Structure:

app/modules/user/
    __init__.py
    user_model.py - модель пользователя (может в этом модуле будет не нужной)
    user_service.py - логика пользователя
    user_routes.py - маршруты пользователя
    user_test.py - тесты только для проверки работы модуля
    user_config.py - конфигурация модуля
    Description.txt - Описание модуля

