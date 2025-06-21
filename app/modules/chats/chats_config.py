# config это базовые классы для создания конфигурации самого модуля и его роутов
from app.config.module_config import ModuleConfig
from app.config.router_config import RouterConfig

# types 
from app.types import EMethod, TRouter
from typing import Dict


class ChatsRouterConfig(RouterConfig):
    def __init__(self, routers: Dict[str, TRouter]):
        super(ChatsRouterConfig, self).__init__(routers)

#
class ChatsModuleConfig(ModuleConfig):
    def __init__(self, 
        title: str, 
        description: str, 
        r: ChatsRouterConfig,
        is_logging: bool = True 
    ) -> None:
        super(ChatsModuleConfig, self).__init__(
            title=title,
            description=description,
            r=r,
            is_logging=is_logging
        )

# 998901234567, 1234 - user1
# 998907654321, 4321 - user2 

routers = {
    "Отображение чатов": TRouter(
        path = "/chats", 
        methods = [EMethod.GET, EMethod.POST], 
        template = "chats/communication.html"
    ),
    "Отображение чата": TRouter(
        path = "/chat/<int:chat_id>", 
        methods = [EMethod.GET, EMethod.POST], 
        template = "chats/chat.html"
    )
}


# Создаём конфигурацию для модуля
chatsConf = ChatsModuleConfig(
    title = "Модуль: app.modules.Chats", 
    description = """
    Модуль для работы с логикой Chats с чатами. 
    Основные функции:
    - Отображение чатов
    - ...
    ...

    Тесты модуля:
    python3.12 -m unittest app/modules/chats/chats_test.py
    """,
    r = ChatsRouterConfig(routers),
    is_logging = True 
)