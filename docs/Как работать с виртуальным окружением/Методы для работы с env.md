# МЕТОДЫ ДЛЯ РАБОТЫ С ENV:

----------------------------------------------------------------------

1. get(key: str, default: str = None) -> str | None:
    - Получает значение переменной окружения по ключу
    - Если переменная окружения не найдена, возвращает значение по умолчанию
    - Если значение по умолчанию не указано, то выходит ошибка

2. get_schema() -> List[str]:
    - Получает схему переменных окружения
    {
        <Name>: <Type>
    }

3. get_config() -> Dict[str, str]:
    - Получает конфигурацию переменных окружения
    {
        <Name>: <Value>
    }

----------------------------------------------------------------------

Пример:

`app/env.py`
```python
from app.config import EnvConfig

env_config = EnvConfig(
    schema = {
        "PORT": int,
    },
    path = ".env"
)
```

`run.py`
```python
from app.env import env_config

env_config.get("PORT") # если есть в .env, то возвращает значение, иначе None
env_config.get("PORT", 8080) # если есть в .env, то возвращает значение, иначе 8080
env_config.get("HOST") # ValueError: app.config.env_config: В виртуальном окружении нет переменной HOST или нет синхронизации c схемой переменных окружения
env_config.get_schema() # { "PORT": int }
env_config.get_config() # { "PORT": 8080 }
```

