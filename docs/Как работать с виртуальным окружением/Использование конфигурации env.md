# ИСПОЛЬЗОВАНИЕ КОНФИГУРАЦИИ ENV:

----------------------------------------------------------------------

1. Импортируйте конфигурацию env в файл run.py:

```python
from app.env import env_config
```

2. Используйте конфигурацию env в файле run.py:

```python
app.run(debug=env_config.get("IS_DEBUG", True))
```