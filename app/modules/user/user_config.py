
# config 
from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict

# Класс для работы с путями в модуле 
class UserRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(UserRouterConfig, self).__init__(routers)
       
# Основной конфигурационный класс всего модуля
class UserModuleConfig(ModuleConfig):

    def __init__(self, 
        title: str, 
        description: str, 
        r: UserRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(UserModuleConfig, self).__init__(
            title = title,
            description = description,
            r = r,
            is_logging = is_logging
        )

        if is_logging: self._print_description_module()
    

routers = {
    "Добавление нового партнёра": TRouter(
        path = "/user/add_new_partner",
        methods = [EMethod.GET, EMethod.POST],
        template = "user/add_partner_page.html"
    ),
    "Страница с успешной регистрацией": TRouter(
        path = "/user/partner_added_successfully/<int:id>",
        methods = [EMethod.GET],
        template = "user/partner_added_successfully.html"
    ),
    "Удаление партнёра": TRouter(
        path = "/user/delete_partner/<int:id>",
        methods = [EMethod.GET, EMethod.POST],
        template = "user/delete_partner.html"
    ),
    "Получение всех партнёра": TRouter(
        path = "/user",
        methods = [EMethod.GET],
        template = "user/all_partner.html"
    ),
    "Изменения партнёра": TRouter(
        path = "/user/edit_partner/<int:id>",
        methods = [EMethod.GET, EMethod.POST],
        template = "user/edit_partner.html"
    ),
}



userConf = UserModuleConfig(
    title = "Модуль: app.modules.user",
    description = """
    Модуль для работы с логикой пользователя.
    Основные функции:
    - Добавление нового партнёра
    - Удаление партнёра
    - Получение всех партнёра
    - Изменения партнёра
    Тесты модуля:
    python3.12 -m unittest app/modules/user/user_test.py
    """,
    r = UserRouterConfig(routers),
    is_logging = False
)


