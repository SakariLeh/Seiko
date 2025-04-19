from typing import Dict
from .router_config import RouterConfig

class ModuleConfig:
    title: str 
    description: str 
    r: Dict[str, RouterConfig]
    is_logging: bool

    def __init__(self, 
        title: str, 
        description: str, 
        r: Dict[str, RouterConfig],
        is_logging: bool = True
    ) -> None:
        self.title = title
        self.description = description
        self.r = r
        self.is_logging = is_logging
        
    def _print_description_module(self) -> None: 
        print(f"----{self.title}---")

        print("Если логи не нужны, то установите is_logging в False в конфигурации модуля")

        print(self.description)
        self.r.print_routers_module()

        print("--------------------------------")