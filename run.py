from app import create_app
from app.env import env_config



app = create_app()

if __name__ == '__main__':
    app.run(
        host=env_config.get('FLASK_RUN_HOST', "localhost"),
        debug=env_config.get('IS_DEBUG', True), 
        port=env_config.get("FLASK_RUN_PORT", 8000), 
        
        load_dotenv=True
    )

