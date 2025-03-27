# models
from app.models.user import User

# types
from app.types import ERoleUser

class AdminModel(User):
    def __init__(self, id=None, phone=None, password=None, role=None, name=None, company=None, location=None):
        role = ERoleUser.ADMIN
        super().__init__(id, phone, password, role, name, company, location)


