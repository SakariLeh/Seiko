
from app.infrastructure import db


# models
from app.modules.product import ProductModel, ProductQuantityModel
from app.modules.reservation import ReservationModel
from app.modules.user import UserModel
from app.modules.chats import ChatModel, MessageModel

from datetime import datetime

# types 
from app.types import EStatus

from werkzeug.security import generate_password_hash


class UserData:
    """
    Класс для инициализации таблицы users базы данных
    """

    def __init__(self):
        user = UserModel.query.first()
        if not user:
            user = UserModel(
                phone="998907654321",
                password=generate_password_hash("5678"),
                role="support",
                name="Ivan Petrov",
                company="NabievOptics",
                location="location"
            )
            db.session.add(user)
            db.session.commit()
        
        user2 = UserModel.query.get(2)
        if not user2:
            user2 = UserModel(
                phone="998901234567",
                password=generate_password_hash("1234"),
                role="admin",
                name="Adam Lumberg",
                company="NabievOptics",
                location="location"
            )
            db.session.add(user2)
            db.session.commit()

        user3 = UserModel.query.get(3)
        if not user3:
            user3 = UserModel(
                phone="998903216547",
                password=generate_password_hash("5555"),
                role="store",
                name="Adam Lumberg",
                company="NabievOptics",
                location="location"
            )
            db.session.add(user3)
            db.session.commit()
        
        user4 = UserModel.query.get(4)
        if not user4:
            user4 = UserModel(
                phone="998903456789",
                password=generate_password_hash("9876"),
                role="branch",
                name="Sergey Sidorov",
                company="Оптика+",
                location="ТЦ Галерея"
            )
            db.session.add(user4)
            db.session.commit()


class ProductData:
    def __init__(self):
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


class ChatData:
    def __init__(self):
        user = UserModel.query.first()
        user2 = UserModel.query.get(2)

        if not ChatModel.query.first():
            chat1 = ChatModel(user1_id=user.id, user2_id=user2.id)
            
            db.session.add_all([chat1])
            db.session.commit()

class MessageData:
    def __init__(self):
        user = UserModel.query.first()
        user2 = UserModel.query.get(2)

        if not MessageModel.query.first():
            message = MessageModel(
                chat_id=1,
                sender_id=user.id,
                text="Hello i'm Ivan Petrov"
            )
            db.session.add(message)
            db.session.commit()
        
        if not MessageModel.query.get(2):
            message = MessageModel(
                chat_id=1,
                sender_id=user2.id,
                text="Hello i'm Adam Lumberg"
            )
            db.session.add(message)
            db.session.commit()


class ReservationData:
    def __init__(self):
        user = UserModel.query.first()


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

class MigrationDB:
    def __init__(self):
        pass
    

    def init_table_data(self):
        # === Продукты ===
        ProductData()

        # === Пользователи ===
        UserData()

        # === Чаты ===

        ChatData()

        # === Бронирование (WarehouseOrder) ===

        ReservationData()
        
        # == Сообщения ===

        MessageData()

        # # === Чаты ===
        # if not ChatModel.query.first():
        #     chat = ChatModel(
        #         user1_id=user.id,
        #         user2_id=user2.id,
        #         messages=[]
        #     )
        #     db.session.add(chat)
        #     db.session.commit()

migrationDB = MigrationDB()