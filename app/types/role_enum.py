from typing import List


class ERoleUser:
    ADMIN: str = "admin" # Владелец
    SUPPORT: str = "support" # Сотрудники владельца
    STORE: str = "store" # Владелец компании-партнёра
    BRANCH: str = "branch" # Сотрудник(филиал) компании-партнёра

    @staticmethod
    def get_all_roles() -> List[str]:
        return [ERoleUser.ADMIN, ERoleUser.SUPPORT, ERoleUser.STORE, ERoleUser.BRANCH]
