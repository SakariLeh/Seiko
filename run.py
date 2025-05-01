from app import create_app
from app.infrastructure import env_config



app = create_app()



if __name__ == '__main__':
    app.run(
        debug=env_config.get('IS_DEBUG', True), 
        port=env_config.get("FLASK_RUN_PORT", 5000)
    )

