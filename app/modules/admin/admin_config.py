
# config 
from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict

# Класс для работы с путями в модуле 
class AdminRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(AdminRouterConfig, self).__init__(routers)
       
# Основной конфигурационный класс всего модуля
class AdminModuleConfig(ModuleConfig):

    def __init__(self, 
        title: str, 
        description: str, 
        r: AdminRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(AdminModuleConfig, self).__init__(
            title = title,
            description = description,
            r = r,
            is_logging = is_logging
        )

        if is_logging: self._print_description_module()
    

routers = {
    "Добавление нового партнёра": TRouter(
        path = "/admin/add_new_partner",
        methods = [EMethod.GET, EMethod.POST],
        template = "admin/add_partner_page.html"
    ),
    "Страница с успешной регистрацией": TRouter(
        path = "/admin/partner_added_successfully/<int:id>",
        methods = [EMethod.GET],
        template = "admin/partner_added_successfully.html"
    ),
    "Удаление партнёра": TRouter(
        path = "/admin/delete_partner/<int:id>",
        methods = [EMethod.GET, EMethod.POST],
        template = "admin/delete_partner.html"
    ),
    "Получение всех партнёра": TRouter(
        path = "/admin/all_partner",
        methods = [EMethod.GET],
        template = "admin/all_partner.html"
    ),
    "Изменения партнёра": TRouter(
        path = "/admin/edit_partner/<int:id>",
        methods = [EMethod.GET, EMethod.POST],
        template = "admin/edit_partner.html"
    ),
}



adminConf = AdminModuleConfig(
    title = "Модуль: app.modules.admin",
    description = """
    Модуль для работы с логикой администратора.
    Основные функции:
    - Добавление нового партнёра
    - Удаление партнёра
    - Получение всех партнёра
    - Изменения партнёра
    Тесты модуля:
    python3.12 -m unittest app/modules/admin/admin_test.py
    """,
    r = AdminRouterConfig(routers),
    is_logging = True
)


