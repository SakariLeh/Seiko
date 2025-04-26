from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

from app.types import EMethod, TRouter
from typing import Dict


class DashboardRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(DashboardRouterConfig, self).__init__(routers)


class DashboardModuleConfig(ModuleConfig):
    def __init__(self, 
        title: str, 
        description: str, 
        r: DashboardRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(DashboardModuleConfig, self).__init__(
            title=title,
            description=description,
            r=r,
            is_logging=is_logging
        )

routers = {
    "Открытие дашборда": TRouter(
        path = "/dashboard",
        methods = [EMethod.GET],
        template="owner_main_page.html"
    ),
    "Перенаправление в хранилище": TRouter(
        path = "/storage",
        methods = [EMethod.GET],
        template = "warehouse_page.html"
    ),
    "Перенаправление в историю заказов": TRouter(
        path = "/order_history",
        methods = [EMethod.GET],
        template = "order_history_page.html"
    ),
    "Перенаправление в коммуникацию": TRouter(
        path = "/communication",
        methods = [EMethod.GET],
        template = "/communication"
    )
    # Возможно нужно дополнить!
}

dashboardConf = DashboardModuleConfig(
    title = "Модуль: app.modules.dashboard",
    description = """
    Модуль для работы дашборда.
    Основные функции:
    - Открытие дашборда
    - Переход к коммуникации
    - Переход в склад
    - Переход к новостям
    - Переход к истории заказов
    - Подгрузка недавних бронирований(и заказов)

    Тесты модуля:
    python3.11 -m unittest app/modules/auth/dashboard_test.py
    """,
    r = DashboardRouterConfig(routers),
    is_logging = True
)