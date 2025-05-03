



from app.config import ModuleConfig
from app.config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict


class ReservationRouterConfig(RouterConfig):
    """
    Класс для работы с путями в модуле
    """
    def __init__(self, routers: Dict[str, TRouter]):
        super(ReservationRouterConfig, self).__init__(routers)


class ReservationModuleConfig(ModuleConfig):
    """
    Класс для работы с конфигурацией модуля
    """
    def __init__(self, 
        title: str, 
        description: str, 
        r: ReservationRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(ReservationModuleConfig, self).__init__(
            title=title,
            description=description,
            r=r,
            is_logging=is_logging
        )



routers = {
    "Бронирование товара": TRouter(
        path = "/reserve_product", 
        methods = [EMethod.POST], 
        template = "reservation/reserve_product.html" 
    ),
}



reservationConf = ReservationModuleConfig(
    title = "Модуль: app.modules.Reservation", 
    description = """
    Модуль для работы с логикой Reservation. 
    Основные функции:
    - Бронирование товаров со склада
    - Просмотр информации о существующих товаров со склада
    ...

    Тесты модуля:
    python3.12 -m unittest app/modules/reservation/Reservation_test.py
    """,
    r = ReservationRouterConfig(routers), 
    is_logging = True 
)