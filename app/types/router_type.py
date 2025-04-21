# types
from typing import List 
from .method_enum import EMethod

class TRouter: 
    path: str 
    methods: List[EMethod]
    template: str 

    def __init__(self, path: str, methods: List[EMethod], template: str) -> None: 
        self.path = path 
        self.methods = methods
        self.template = template