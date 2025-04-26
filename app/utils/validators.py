import re

# types
from app.types import ERoleUser

def validate_phone(phone):
    """
    Проверяет корректность номера телефона.
    Ожидается формат: 7XXXXXXXXXX (11 цифр, начиная с 7)
    """
    pattern = r'^998\d{9}$'
    return re.match(pattern, phone) is not None

def validate_password(password):
    """
    Проверяет корректность 4-значного PIN-кода.
    """
    pattern = r'^\d{4}$'
    return re.match(pattern, password) is not None


def validate_role(role: str) -> bool:
    """
    Проверяет корректность роли.
    """
    return role.strip().lower() in [ERoleUser.ADMIN, ERoleUser.STORE, ERoleUser.BRANCH, ERoleUser.SUPPORT]

