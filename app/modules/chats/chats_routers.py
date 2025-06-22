
from flask_socketio import send

from app.infrastructure import web_socket

from flask import Blueprint, render_template

from app.modules.chats.chats_config import chatsConf

from .chats_services import get_chats_service, find_by_id_chat_service, get_or_create_chat
from .chats_services import save_message_at_chat_service, delete_message_service

from app.modules.user import get_user_name_service

from flask_socketio import join_room

from app.types import ESessionUser

from flask import session


from flask import copy_current_request_context
from flask_socketio import disconnect


chat_bp = Blueprint('chats', __name__)

socketio = web_socket.get_socketio()

@chat_bp.route(
    chatsConf.r.get_path("Отображение чатов"),
    methods = chatsConf.r.get_methods("Отображение чатов")
)
def communication_route():
    user_id = session.get(ESessionUser.USER_ID)
    chat_data = get_chats_service(user_id)
    return render_template(
        chatsConf.r.get_temp("Отображение чатов"), 
        chats=chat_data,
        current_user_id=user_id,
        found_user=None,
        searched=False
    )

@chat_bp.route(
    chatsConf.r.get_path("Отображение чата"),
    methods = chatsConf.r.get_methods("Отображение чата")
)
def single_chat(chat_id: int):

    chat, messages = find_by_id_chat_service(chat_id)
    user_id = session.get(ESessionUser.USER_ID)
    
   

    return render_template(
        chatsConf.r.get_temp("Отображение чата"), 
        chat=chat, 
        messages=messages,
        current_user_id=user_id,
        get_user_name_service=get_user_name_service
    )





@socketio.on('join')
def handle_join(data):
    chat_id = data['chat_id']
    join_room(str(chat_id))




@socketio.on('chat_message')
def handle_chat_message(data):
    chat_id = data['chat_id']
    text = data['text']
    sender_id = data['sender_id']  # 👍 теперь это будет актуальный пользователь



    save_message_at_chat_service(chat_id, sender_id=sender_id, text=text)

    sender_name = get_user_name_service(sender_id)
    
    socketio.emit('message', {
        'sender_id': sender_id,
        'text': text,
        'sender_name': sender_name
    }, to=str(chat_id))


@socketio.on('delete_message')
def handle_delete_message(data):
    message_id = data['message_id']
    chat_id = data['chat_id']
    user_id = data['user_id']

    delete_message_service(message_id)

    socketio.emit('message_deleted', {
        'message_id': message_id,
    }, to=str(chat_id))

    





from flask import request, redirect, url_for

@chat_bp.route("/chats/search", methods=["POST"])
def search_user_by_phone():
    from app.modules.user import UserModel
    phone = request.form.get("phone")
    found_user = UserModel.query.filter_by(phone=phone).first()
    user_id = session.get(ESessionUser.USER_ID)
    return render_template(
        chatsConf.r.get_temp("Отображение чатов"),
        chats=get_chats_service(user_id),
        current_user_id=user_id,
        found_user=found_user,
        searched=True
    )


@chat_bp.route("/chats/start", methods=["POST"])
def start_chat_with_user():
    other_user_id = int(request.form.get("user_id"))
    current_user_id = session.get(ESessionUser.USER_ID)
    chat = get_or_create_chat(current_user_id, other_user_id)
    return redirect(url_for("chats.single_chat", chat_id=chat.id))




