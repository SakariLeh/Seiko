
from enum import Enum

class EStatus(Enum):
    """
    Статусы
    """

    IN_REVIEW = 'IN_REVIEW' # В рассмотрении
    APPROVED = 'APPROVED' # Одобрен
    REJECTED = 'REJECTED' # Отклонен 
    SEND = "SEND" # Отправлен