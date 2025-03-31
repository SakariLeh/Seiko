
# types
from app.types import TRouter, EMethod
from typing import Dict, List

class RouterConfig:
    routers: Dict[str, TRouter]

    def __init__(self, routers: Dict[str, TRouter]) -> None:
        self.routers = routers

    def get_path(self, key: str) -> str:
        return self.routers[key].path

    def get_methods(self, key: str) -> List[EMethod]:
        return self.routers[key].methods
    
    def get_temp(self, key: str) -> str:
        return self.routers[key].template
    
    def print_routers_module(self) -> None:
        for k, v in self.routers.items():
            print(
                "Название:", k, "\n",
                "Путь:", v.path, "\n",
                "Методы:", v.methods, "\n", 
                "Шаблон:", v.template, "\n"
            )