from enum import Enum

class EReservationStatus(str, Enum):
    PENDING: str = 'pending'   # Ожидает подтверждения
    APPROVED: str = 'approved' # Подтверждено
    REJECTED: str = 'rejected' # Отклонено
