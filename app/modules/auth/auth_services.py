# flask 
from flask import session

# types
from app.types import ESessionUser

# models
from app.models import User

# utils 
from app.utils import validate_phone, validate_password

# models
from .auth_models import AuthModel

def is_logged_in_service() -> bool:
    if ESessionUser.USER_ID in session:
        return True
    return False


def validate_phone_service(phone: str) -> bool:
    return validate_phone(phone)

def validate_password_service(password: str) -> bool:
    return validate_password(password)

def login_service(phone: str, password: str) -> User | None:
    # Аутентификация пользователя
    user = AuthModel.authenticate(phone, password)

    if not user:
        return None

    session[ESessionUser.USER_ID] = user.id
    session[ESessionUser.ROLE] = user.role
    session[ESessionUser.NAME] = user.name
    session[ESessionUser.COMPANY] = user.company
    session[ESessionUser.LOCATION] = user.location

    return user

def logout_service() -> None:
    session.clear()
    return None



