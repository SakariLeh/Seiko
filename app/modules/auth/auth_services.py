# flask 
from flask import session

# types
from app.types import ESessionUser

def is_logged_in_service() -> bool:
    if ESessionUser.USER_ID in session:
        return True
    return False

def login_service() -> None:
    return None

def logout_service() -> None:
    session.clear()
    return None



