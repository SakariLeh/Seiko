
from app.infrastructure import db


# models
from app.modules.product import ProductModel, ProductQuantityModel
from app.modules.reservation import ReservationModel
from app.modules.user import UserModel

# types 
from app.types import EStatus


class MigrationDB:
    def __init__(self):
        pass
    

    def init_table_data(self):
        # === Продукты ===
        if not ProductModel.query.first():
            product1 = ProductModel(
                name="Товар 1",
                description_intro="Краткое описание 1",
                description_text="<p>Полное описание 1</p>"
            )
            product2 = ProductModel(
                name="Товар 2",
                description_intro="Краткое описание 2",
                description_text="""
                <div>
                    <h2>Подзаголовок</h2>
                    <p>Полное описание 2</p>
                </div>
                """
            )
            product3 = ProductModel(
                name="Товар 3",
                description_intro="Краткое описание 3",
                description_text="""
                <div>
                    <h2>Подзаголовок</h2>
                    <p>Полное описание 2</p>
                </div>
                """
            )
            db.session.add_all([product1, product2, product3])
            db.session.commit()
       
            # === Количество ===
            quantity1 = ProductQuantityModel(product_id=product1.id, quantity=10, is_available=True)
            quantity2 = ProductQuantityModel(product_id=product2.id, quantity=20, is_available=False)
            quantity3 = ProductQuantityModel(product_id=product3.id, quantity=50, is_available=True)
            db.session.add_all([quantity1, quantity2, quantity3])
            db.session.commit()

        # === Пользователи ===
        user = UserModel.query.first()
        if not user:
            user = UserModel(
                phone="123456789",
                password="123456789",
                role="admin",
                name="admin",
                company="company",
                location="location"
            )
            db.session.add(user)
            db.session.commit()
        

        # === Бронирование (WarehouseOrder) ===
        if not ReservationModel.query.first():
            product = ProductModel.query.first()

            order1 = ReservationModel(
                product_id=product.id,
                user_id=user.id,
                quantity=5,
                status=EStatus.IN_REVIEW,
                location="location",
                company="Оптика Плюс",
            )
            order2 = ReservationModel(
                product_id=product.id,
                user_id=user.id,
                quantity=15,
                status=EStatus.APPROVED,
                location="location",
                company="Линзы и очки",
            )

            order3 = ReservationModel(
                product_id=product.id,
                user_id=user.id,
                quantity=15,
                status=EStatus.REJECTED,
                location="location",
                company="Очки Маркет",
            )
            db.session.add_all([order1, order2, order3])
            db.session.commit()

migrationDB = MigrationDB()