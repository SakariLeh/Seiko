# config 
from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict

# Класс для работы с путями в модуле 
class NewsRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(NewsRouterConfig, self).__init__(routers)
       
# Основной конфигурационный класс всего модуля
class NewsModuleConfig(ModuleConfig):

    def __init__(self, 
        title: str, 
        description: str, 
        r: NewsRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(NewsModuleConfig, self).__init__(
            title = title,
            description = description,
            r = r,
            is_logging = is_logging
        )

        if is_logging: self._print_description_module()
    

routers = {
    "Добавление новой новости": TRouter(
        path = "/news/add_news",
        methods = [EMethod.GET, EMethod.POST],
        template = "news/add_news.html"
    ),
    "Удаление новости": TRouter(
        path = "/news/delete_news/<int:id>",
        methods = [EMethod.GET, EMethod.POST],
        template = "news/delete_news.html"
    ),
    "Получение всех новостей": TRouter(
        path = "/news",
        methods = [EMethod.GET],
        template = "news/all_news.html"
    ),
    "Изменения новости": TRouter(
        path = "/news/edit_news/<int:id>",
        methods = [EMethod.GET, EMethod.POST],
        template = "news/edit_news.html"
    ),
    "Подробная новость": TRouter(
        path = "/news/detailed_news/<int:id>",
        methods = [EMethod.GET],
        template = "news/detailed_news.html"
    ),
}



newsConf = NewsModuleConfig(
    title = "Модуль: app.modules.news",
    description = """
    Модуль для работы с логикой новостей.
    Основные функции:
    - Добавление новостей 
    - Удаление новостей
    - Получение всех новостей
    - Изменения новости
    Тесты модуля:
    python3.12 -m unittest app/modules/news/news_test.py
    """,
    r = NewsRouterConfig(routers),
    is_logging = False
)