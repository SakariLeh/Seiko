





from flask_socketio import SocketIO

_socketio = SocketIO()

def get_socketio():
    return _socketio