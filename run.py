from app import create_app
from typing import List


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)