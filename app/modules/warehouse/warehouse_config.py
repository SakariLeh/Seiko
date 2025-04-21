# config это базовые классы для создания конфигурации самого модуля и его роутов
from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict

# Класс для работы с путями в модуле 
class WarehouseRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(WarehouseRouterConfig, self).__init__(routers)

# Основной конфигурационный класс всего модуля
class WarehouseModuleConfig(ModuleConfig):
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


# Дальше идёт hashMap роутов для модуля
routers = {
    "Зарезервировать продукт": TRouter(
        path = "/reserve_product", # путь по которому будет доступен роут
        methods = [EMethod.POST], # методы, которые будут доступны для этого роута
        template = "" # путь к шаблону, который будет использоваться для этого роута
    ),

}


# Создаём конфигурацию для модуля
warehouseConf = WarehouseModuleConfig(
    title = "Модуль: app.modules.Warehouse", # название модуля и можно указать путь к модулю, чтобы улучшить логирование
    description = """
    Модуль для работы с логикой Warehouse. 
    Основные функции:
    - Бронирование товаров со склада
    - Просмотр информации о существующих товаров со склада
    ...

    Тесты модуля:
    python3.12 -m unittest app/modules/Warehouse/Warehouse_test.py
    """,
    r = WarehouseRouterConfig(routers), # конфигурация роутов для модуля
    is_logging = True # логирование для модуля
)