
import os 
from dotenv import load_dotenv


from typing import Dict, List



class EnvConfig:
    config: Dict[str, str] = {}

    def __init__(self, schema: Dict[str, type], path: str = ".env"):
        load_dotenv(path)
        self.schema = schema

        for key, value in schema.items():
            temp = os.getenv(key)
            if not temp:
                raise ValueError(f"app.config.env_config: В виртуальном окружении нет переменной {key}")
            
           


            self.config[key] = value(temp)

    def get_config(self) -> Dict[str, str]:
        return self.config


    def get(self, key: str, default: str = None) -> str | None:        
        if not key in self.config and not default:
            raise ValueError(f"app.config.env_config: В виртуальном окружении нет переменной {key} или нет синхронизации схемы и переменных окружения")

        return self.config[key] if key in self.config else default


    def get_schema(self) -> List[str]:
        return self.schema
