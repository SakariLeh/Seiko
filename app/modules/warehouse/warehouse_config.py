# config это базовые классы для создания конфигурации самого модуля и его роутов
from app.config import ModuleConfig
from app.config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict


class WarehouseRouterConfig(RouterConfig):
    """
    Класс для работы с путями в модуле
    """
    def __init__(self, routers: Dict[str, TRouter]):
        super(WarehouseRouterConfig, self).__init__(routers)


class WarehouseModuleConfig(ModuleConfig):
    """
    Класс для работы с конфигурацией модуля
    """
    def __init__(self, 
        title: str, 
        description: str, 
        r: WarehouseRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(WarehouseModuleConfig, self).__init__(
            title=title,
            description=description,
            r=r,
            is_logging=is_logging
        )



routers = {

    "Все товары на складе": TRouter(
        path = "/storage", 
        methods = [EMethod.GET], 
        template = "warehouse/warehouse_page.html"
    ),
    "Подробнее о товаре на складе": TRouter(
        path = "/storage/detailed_product/<int:id>", 
        methods = [EMethod.GET], 
        template = "warehouse/product_page.html"
    )

}


# Создаём конфигурацию для модуля
warehouseConf = WarehouseModuleConfig(
    title = "Модуль: app.modules.Warehouse", 
    description = """
    Модуль для работы с логикой Warehouse. 
    Основные функции:
    - Бронирование товаров со склада
    - Просмотр информации о существующих товаров со склада
    ...

    Тесты модуля:
    python3.12 -m unittest app/modules/warehouse/warehouse_test.py
    """,
    r = WarehouseRouterConfig(routers), 
    is_logging = True 
)