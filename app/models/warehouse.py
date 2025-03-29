from datetime import datetime
from typing import List, Dict, Any, Optional


class Product:
    def __init__(self, id=None, name=None, description=None, quantity=None, available=True,
                 manufacturer=None, type=None, category=None):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.available = available
        self.manufacturer = manufacturer
        self.type = type
        self.category = category


class Reservation:
    def __init__(self, id=None, product_id=None, quantity=None, user_id=None, company=None,
                 location=None, timestamp=None, status='pending'):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.user_id = user_id
        self.company = company
        self.location = location
        self.timestamp = timestamp or datetime.now()
        self.status = status  # 'pending', 'approved', 'rejected'