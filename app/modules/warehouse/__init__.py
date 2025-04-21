from .warehouse_routes import warehouse_bp # Импортируем warehouse_bp из warehouse_routes

__export__ = [
    warehouse_bp    # warehouse_bp в дальнейшем экспортируется наружу
]