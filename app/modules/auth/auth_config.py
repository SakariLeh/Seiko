# config 
from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict


class AuthRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(AuthRouterConfig, self).__init__(routers)


class AuthModuleConfig(ModuleConfig):
    def __init__(self, 
        title: str, 
        description: str, 
        r: AuthRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(AuthModuleConfig, self).__init__(
            title=title,
            description=description,
            r=r,
            is_logging=is_logging
        )



routers = {
    "Проверка авторизации пользователя": TRouter(
        path = "/",
        methods = [EMethod.GET, EMethod.POST], 
        template = "index.html" 
    ),
    "Выход из системы": TRouter(
        path = "/logout",
        methods = [EMethod.GET], 
        template = "auth/login_page.html" 
    ),
    "Вход в систему(номер телефона)": TRouter(
        path = "auth/phone.html",
        methods = [EMethod.GET, EMethod.POST], 
        template = "auth/phone.html" 
    ),
    "Вход в систему(пароль)": TRouter(
        path = "auth/password.html",
        methods = [EMethod.GET, EMethod.POST], 
        template = "auth/password.html" 
    ),
    
}



authConf = AuthModuleConfig(
    title = "Модуль: app.modules.auth", 
    description = """
    Модуль для работы с логикой auth. 
    Основные функции:
    - вход в систему
    - выход из системы
    - Проверка авторизации пользователя

    Тесты модуля:
    python3.12 -m unittest app/modules/auth/auth_test.py
    """,
    r = AuthRouterConfig(routers), 
    is_logging = True 
)