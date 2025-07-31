
from app.modules.user import get_all_users_service
from .chats_models import ChatModel, MessageModel

from typing import List, Tuple

from app.infrastructure import db

from app.modules.user import get_user_name_service

class ChatDTO:
    def __init__(self, id, user1_id, user2_id, user1_name, user2_name, last_message):
        self.id = id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.user1_name = user1_name
        self.user2_name = user2_name
        self.last_message = last_message


def get_chats_service(user_id: int) -> List[ChatDTO]:
    """
    Получение всех чатов

    param: None
    return: List[ChatModel] - список чатов
    """
    # Получаем все чаты, где участвует пользователь
    chats = ChatModel.query.filter(
        (ChatModel.user1_id == user_id) | (ChatModel.user2_id == user_id)
    ).all()

    chat_data: List[ChatDTO] = []

    for chat in chats:
        last_msg = chat.messages.order_by(MessageModel.created_at.desc()).first()
        
        chat_data.append(ChatDTO(
            id=chat.id,
            user1_id=chat.user1_id,
            user2_id=chat.user2_id,
            user1_name=get_user_name_service(chat.user1_id),
            user2_name=get_user_name_service(chat.user2_id),
            last_message=last_msg
        ))

    return chat_data


def get_or_create_chat(user1_id, user2_id):
    chat = ChatModel.query.filter(
        ((ChatModel.user1_id == user1_id) & (ChatModel.user2_id == user2_id)) |
        ((ChatModel.user1_id == user2_id) & (ChatModel.user2_id == user1_id))
    ).first()

    if chat:
        return chat

    # создать новый чат
    chat = ChatModel(user1_id=user1_id, user2_id=user2_id)
    db.session.add(chat)
    db.session.commit()
    return chat



def find_by_id_chat_service(chat_id: int) -> Tuple[ChatModel, List[MessageModel]]:
    """
    Поиск чата по id
    param: chat_id - id чата
    return: ChatModel
    """
    chat = ChatModel.query.get_or_404(chat_id)
    messages = chat.messages.order_by(MessageModel.created_at).all()
    return (chat, messages)


# ------

def save_message_at_chat_service(chat_id: int, sender_id: int, text: str) -> MessageModel:
    """
    Сохранение сообщения в чат
    param: chat_id - id чата, text - текст сообщения
    return: MessageModel
    """
    msg = MessageModel(chat_id=chat_id, sender_id=sender_id, text=text)
    db.session.add(msg)
    db.session.commit()
    return msg



def delete_message_service(message_id: int):
    msg = MessageModel.query.get_or_404(message_id)
    db.session.delete(msg)
    db.session.commit()