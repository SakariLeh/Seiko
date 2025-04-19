from app.config import EnvConfig

# Настройка виртуального окружения
env_config = EnvConfig(
    schema = {
        "IS_LOGGING": bool,
        "IS_DEBUG": bool,
        "FLASK_APP": str,
        "FLASK_ENV": str,
        "FLASK_RUN_HOST": str,
        "FLASK_RUN_PORT": int,
    },
    path = ".env"
)


