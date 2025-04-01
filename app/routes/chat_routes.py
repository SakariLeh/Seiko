from flask import Blueprint, render_template, session, redirect, url_for, request, abort, flash
from datetime import datetime

from functools import wraps

chat_bp = Blueprint('chat', __name__)


# Функция-декоратор для проверки авторизации
def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.index'))
        return view_func(*args, **kwargs)

    return wrapped_view


@chat_bp.route('/chats')
@login_required
def index():
    """Главная страница коммуникаций - список доступных чатов"""
    role = session.get('role')
    user_id = session.get('user_id')

    # Получаем данные пользователя
    user_data = get_user_data(user_id)

    # Получаем доступные группы чатов в зависимости от роли
    chat_groups = get_available_chat_groups(role, user_data)

    # Получаем доступные прямые чаты в зависимости от роли
    direct_chats = get_available_direct_chats(role, user_data)

    return render_template(
        'communication_page.html',
        role=role,
        chat_groups=chat_groups,
        direct_chats=direct_chats,
        current_user_id=user_id,
        user_data=user_data
    )


@chat_bp.route('/support_chat/<chat_id>')
@login_required
def support_chat(chat_id):
    """Страница группового чата поддержки"""
    user_id = session.get('user_id')
    role = session.get('role')

    # Проверяем, имеет ли пользователь доступ к этому чату
    if not can_access_support_chat(user_id, role, chat_id):
        abort(403)  # Доступ запрещен

    # Получаем информацию о чате
    chat_info = get_chat_info(chat_id)

    # Получаем сообщения чата
    messages = get_chat_messages(chat_id)

    return render_template(
        'vision_trend_support_chat.html',
        chat_id=chat_id,
        chat_title=chat_info['title'],
        chat_type=chat_info['type'],
        chat_avatar_initials=chat_info['avatar_initials'],
        messages=messages,
        current_user_id=user_id
    )


@chat_bp.route('/partner_chat/<partner_id>')
@login_required
def partner_chat(partner_id):
    """Страница группового чата компании-партнера"""
    user_id = session.get('user_id')
    role = session.get('role')

    # Проверяем, имеет ли пользователь доступ к этому чату
    if not can_access_partner_chat(user_id, role, partner_id):
        abort(403)  # Доступ запрещен

    # Получаем информацию о чате
    chat_info = get_partner_chat_info(partner_id)

    # Получаем сообщения чата
    messages = get_partner_chat_messages(partner_id)

    return render_template(
        'vision_trend_support_chat.html',  # Используем тот же шаблон
        chat_id=f"partner_{partner_id}",
        chat_title=chat_info['title'],
        chat_type=chat_info['type'],
        chat_avatar_initials=chat_info['avatar_initials'],
        messages=messages,
        current_user_id=user_id
    )


@chat_bp.route('/direct_chat/<user_id>')
@login_required
def direct_chat(user_id):
    """Страница прямого чата с пользователем"""
    current_user_id = session.get('user_id')
    role = session.get('role')

    # Проверяем, имеет ли пользователь доступ к этому чату
    if not can_access_direct_chat(current_user_id, role, user_id):
        abort(403)  # Доступ запрещен

    # Получаем информацию о пользователе
    user_info = get_user_info(user_id)

    # Получаем сообщения чата
    messages = get_direct_chat_messages(current_user_id, user_id)

    return render_template(
        'vision_trend_support_chat.html',  # Используем тот же шаблон
        chat_id=f"direct_{user_id}",
        chat_title=user_info['name'],
        chat_type=user_info['role_display'],
        chat_avatar_initials=user_info['avatar_initials'],
        messages=messages,
        current_user_id=current_user_id
    )


@chat_bp.route('/send_message/<chat_id>', methods=['POST'])
@login_required
def send_message(chat_id):
    """Обработка отправки сообщения"""
    message_text = request.form.get('message')
    user_id = session.get('user_id')

    if not message_text:
        flash('Сообщение не может быть пустым', 'error')
        # Определяем правильный маршрут возврата
        if chat_id.startswith('vt_support'):
            return redirect(url_for('chat.support_chat', chat_id=chat_id))
        elif chat_id.startswith('partner_'):
            partner_id = chat_id.split('_')[1]
            return redirect(url_for('chat.partner_chat', partner_id=partner_id))
        elif chat_id.startswith('direct_'):
            recipient_id = chat_id.split('_')[1]
            return redirect(url_for('chat.direct_chat', user_id=recipient_id))
        else:
            return redirect(url_for('chat.index'))

    # Определяем тип чата
    if chat_id.startswith('vt_support'):
        # Групповой чат поддержки
        save_support_chat_message(user_id, chat_id, message_text)
        return redirect(url_for('chat.support_chat', chat_id=chat_id))

    elif chat_id.startswith('partner_'):
        # Групповой чат партнера
        partner_id = chat_id.split('_')[1]
        save_partner_chat_message(user_id, partner_id, message_text)
        return redirect(url_for('chat.partner_chat', partner_id=partner_id))

    elif chat_id.startswith('direct_'):
        # Прямой чат с пользователем
        recipient_id = chat_id.split('_')[1]
        save_direct_message(user_id, recipient_id, message_text)
        return redirect(url_for('chat.direct_chat', user_id=recipient_id))

    else:
        abort(404)  # Неизвестный тип чата


# Вспомогательные функции

def get_user_data(user_id):
    """
    Получает данные пользователя из базы данных.
    В демонстрационных целях возвращает тестовые данные.
    """
    test_data = {
        'admin': {
            'id': '1',
            'name': 'Адам Ламберг',
            'company': 'NabievOptics',
            'phone': '998901234567',
            'role': 'admin'
        },
        'support': {
            'id': '2',
            'name': 'Иван Петров',
            'company': 'NabievOptics',
            'phone': '998907654321',
            'role': 'support'
        },
        'store': {
            'id': '3',
            'name': 'Марина Волкова',
            'company': 'Оптика+',
            'phone': '998909876543',
            'role': 'store'
        },
        'branch': {
            'id': '4',
            'name': 'Сергей Сидоров',
            'company': 'Оптика+',
            'location': 'ТЦ Галерея',
            'phone': '998903456789',
            'role': 'branch'
        }
    }

    role = session.get('role')
    return test_data.get(role, {})


def get_available_chat_groups(role, user_data):
    """
    Возвращает список доступных групповых чатов в зависимости от роли.
    """
    groups = []

    # Чат поддержки доступен всем ролям
    support_group = {
        'id': 'vt_support_main',
        'name': 'VisionTrend Support',
        'type': 'support',
        'avatar_initials': 'VT',
        'description': 'Основной чат поддержки'
    }
    groups.append(support_group)

    # Для ролей admin и support добавляем все группы компаний-партнеров
    if role in ['admin', 'support']:
        partner_companies = [
            {'id': '1', 'name': 'Оптика+', 'avatar_initials': 'О+'},
            {'id': '2', 'name': 'Линзы и очки', 'avatar_initials': 'ЛО'},
            {'id': '3', 'name': 'ОчкиМаркет', 'avatar_initials': 'ОМ'}
        ]

        for company in partner_companies:
            groups.append({
                'id': f"partner_{company['id']}",
                'name': f"{company['name']} Staff",
                'type': 'partner',
                'avatar_initials': company['avatar_initials'],
                'description': f"Групповой чат компании {company['name']}"
            })

    # Для роли store добавляем только группу его компании
    elif role == 'store':
        company_name = user_data['company']
        company_id = get_company_id(company_name)

        if company_id:
            initials = ''.join([word[0] for word in company_name.split()]) if ' ' in company_name else company_name[:2]
            groups.append({
                'id': f"partner_{company_id}",
                'name': f"{company_name} Staff",
                'type': 'partner',
                'avatar_initials': initials,
                'description': f"Групповой чат компании {company_name}"
            })

    # Для роли branch добавляем только группу его компании
    elif role == 'branch':
        company_name = user_data['company']
        company_id = get_company_id(company_name)

        if company_id:
            initials = ''.join([word[0] for word in company_name.split()]) if ' ' in company_name else company_name[:2]
            groups.append({
                'id': f"partner_{company_id}",
                'name': f"{company_name} Staff",
                'type': 'partner',
                'avatar_initials': initials,
                'description': f"Групповой чат компании {company_name}"
            })

    return groups


def get_available_direct_chats(role, user_data):
    """
    Возвращает список доступных прямых чатов в зависимости от роли.
    """
    # Все пользователи в системе (для демонстрации)
    all_users = [
        {
            'id': '1',
            'name': 'Адам Ламберг',
            'role': 'admin',
            'role_display': 'владелец',
            'company': 'NabievOptics',
            'location': None,
            'avatar_initials': 'АЛ'
        },
        {
            'id': '2',
            'name': 'Иван Петров',
            'role': 'support',
            'role_display': 'сотрудник',
            'company': 'NabievOptics',
            'location': None,
            'avatar_initials': 'ИП'
        },
        {
            'id': '3',
            'name': 'Марина Волкова',
            'role': 'store',
            'role_display': 'партнёр',
            'company': 'Оптика+',
            'location': None,
            'avatar_initials': 'МВ'
        },
        {
            'id': '4',
            'name': 'Сергей Сидоров',
            'role': 'branch',
            'role_display': 'отдел партнёра ТЦ Галерея',
            'company': 'Оптика+',
            'location': 'ТЦ Галерея',
            'avatar_initials': 'СС'
        },
        {
            'id': '5',
            'name': 'Анна Иванова',
            'role': 'branch',
            'role_display': 'отдел партнёра ТЦ Мега',
            'company': 'Оптика+',
            'location': 'ТЦ Мега',
            'avatar_initials': 'АИ'
        }
    ]

    available_users = []

    # Исключаем текущего пользователя из списка
    current_user_id = user_data['id']

    if role in ['admin', 'support']:
        # Админ и поддержка могут писать всем пользователям
        available_users = [user for user in all_users if user['id'] != current_user_id]

    elif role == 'store':
        # Компания-партнер может писать:
        # 1. Поддержке и владельцу
        # 2. Своим филиалам
        for user in all_users:
            if user['id'] == current_user_id:
                continue

            if user['role'] in ['admin', 'support']:
                # Сотрудники NabievOptics
                available_users.append(user)
            elif user['role'] == 'branch' and user['company'] == user_data['company']:
                # Филиалы той же компании
                available_users.append(user)

    elif role == 'branch':
        # Филиал может писать:
        # 1. Поддержке и владельцу
        # 2. Владельцу своей компании
        # 3. Другим филиалам своей компании
        for user in all_users:
            if user['id'] == current_user_id:
                continue

            if user['role'] in ['admin', 'support']:
                # Сотрудники NabievOptics
                available_users.append(user)
            elif user['role'] == 'store' and user['company'] == user_data['company']:
                # Владелец компании
                available_users.append(user)
            elif user['role'] == 'branch' and user['company'] == user_data['company'] and user[
                'location'] != user_data.get('location'):
                # Другие филиалы той же компании
                available_users.append(user)

    return available_users


def get_company_id(company_name):
    """Возвращает ID компании по её названию"""
    company_map = {
        'Оптика+': '1',
        'Линзы и очки': '2',
        'ОчкиМаркет': '3',
        'NabievOptics': '0'  # Компания-владелец
    }
    return company_map.get(company_name)


def can_access_support_chat(user_id, role, chat_id):
    """Проверяет, имеет ли пользователь доступ к чату поддержки"""
    # Все пользователи имеют доступ к общему чату поддержки
    return True


def can_access_partner_chat(user_id, role, partner_id):
    """Проверяет, имеет ли пользователь доступ к групповому чату партнера"""
    if role in ['admin', 'support']:
        # Админ и поддержка имеют доступ ко всем чатам
        return True

    user_data = get_user_data(user_id)
    company_id = get_company_id(user_data.get('company'))

    # Проверяем, является ли пользователь частью этой компании
    return company_id == partner_id


def can_access_direct_chat(current_user_id, role, target_user_id):
    """Проверяет, имеет ли пользователь доступ к прямому чату с другим пользователем"""
    # Получаем данные текущего пользователя
    current_user_data = get_user_data(current_user_id)

    # Получаем данные о доступных пользователях
    available_users = get_available_direct_chats(role, current_user_data)

    # Проверяем, есть ли целевой пользователь в списке доступных
    for user in available_users:
        if user['id'] == target_user_id:
            return True

    return False


def get_chat_info(chat_id):
    """Возвращает информацию о чате поддержки"""
    return {
        'title': 'VisionTrend Support',
        'type': 'Группа',
        'avatar_initials': 'VT'
    }


def get_partner_chat_info(partner_id):
    """Возвращает информацию о групповом чате партнера"""
    partners = {
        '1': {'name': 'Оптика+', 'initials': 'О+'},
        '2': {'name': 'Линзы и очки', 'initials': 'ЛО'},
        '3': {'name': 'ОчкиМаркет', 'initials': 'ОМ'}
    }

    partner = partners.get(partner_id, {'name': 'Неизвестный партнер', 'initials': 'НП'})

    return {
        'title': f"{partner['name']} Staff",
        'type': 'Группа',
        'avatar_initials': partner['initials']
    }


def get_user_info(user_id):
    """Возвращает информацию о пользователе для чата"""
    users = {
        '1': {'name': 'Адам Ламберг', 'role_display': 'владелец', 'avatar_initials': 'АЛ'},
        '2': {'name': 'Иван Петров', 'role_display': 'сотрудник', 'avatar_initials': 'ИП'},
        '3': {'name': 'Марина Волкова', 'role_display': 'партнёр', 'avatar_initials': 'МВ'},
        '4': {'name': 'Сергей Сидоров', 'role_display': 'отдел партнёра ТЦ Галерея', 'avatar_initials': 'СС'},
        '5': {'name': 'Анна Иванова', 'role_display': 'отдел партнёра ТЦ Мега', 'avatar_initials': 'АИ'}
    }

    return users.get(user_id, {'name': 'Неизвестный пользователь', 'role_display': '', 'avatar_initials': 'НП'})


def get_chat_messages(chat_id):
    """Возвращает сообщения из чата поддержки"""
    # Демонстрационные сообщения
    return [
        {
            'user_id': '1',
            'user_name': 'Адам Ламберг',
            'user_avatar_initials': 'АЛ',
            'text': 'Всем привет! У кого-то есть обновления по поставкам линз Johnson?',
            'timestamp': datetime.now().replace(hour=10, minute=15)
        },
        {
            'user_id': '2',
            'user_name': 'Иван Петров',
            'user_avatar_initials': 'ИП',
            'text': 'Да, поставка ожидается через неделю. Уже подтвердили со склада.',
            'timestamp': datetime.now().replace(hour=10, minute=18)
        },
        {
            'user_id': '3',
            'user_name': 'Марина Волкова',
            'user_avatar_initials': 'МВ',
            'text': 'Отлично! Мы как раз ждем эту партию для крупного заказа.',
            'timestamp': datetime.now().replace(hour=10, minute=25)
        }
    ]


def get_partner_chat_messages(partner_id):
    """Возвращает сообщения из группового чата партнера"""
    # Демонстрационные сообщения для партнера Оптика+
    if partner_id == '1':
        return [
            {
                'user_id': '3',
                'user_name': 'Марина Волкова',
                'user_avatar_initials': 'МВ',
                'text': 'Коллеги, скоро поступят новые линзы Johnson. Подготовьтесь к приему товара.',
                'timestamp': datetime.now().replace(hour=11, minute=30)
            },
            {
                'user_id': '4',
                'user_name': 'Сергей Сидоров',
                'user_avatar_initials': 'СС',
                'text': 'Понял, у нас в ТЦ Галерея уже есть предзаказы на эту модель.',
                'timestamp': datetime.now().replace(hour=11, minute=35)
            },
            {
                'user_id': '5',
                'user_name': 'Анна Иванова',
                'user_avatar_initials': 'АИ',
                'text': 'В ТЦ Мега тоже ждем. Клиенты спрашивают о сроках.',
                'timestamp': datetime.now().replace(hour=11, minute=42)
            }
        ]
    # Для других партнеров возвращаем пустой список или создаем демо сообщения
    elif partner_id == '2':
        return [
            {
                'user_id': '1',
                'user_name': 'Адам Ламберг',
                'user_avatar_initials': 'АЛ',
                'text': 'Добрый день! Как идут продажи новой линейки продукции?',
                'timestamp': datetime.now().replace(hour=9, minute=15)
            }
        ]
    elif partner_id == '3':
        return [
            {
                'user_id': '2',
                'user_name': 'Иван Петров',
                'user_avatar_initials': 'ИП',
                'text': 'Здравствуйте! Есть ли вопросы по последней поставке?',
                'timestamp': datetime.now().replace(hour=14, minute=30)
            }
        ]
    return []


def get_direct_chat_messages(user_id, recipient_id):
    """Возвращает сообщения из прямого чата между пользователями"""
    # Создаем уникальный ключ для идентификации чата (сортируем ID, чтобы был одинаковый для обоих пользователей)
    chat_key = '_'.join(sorted([user_id, recipient_id]))

    # Демонстрационные сообщения для чатов между разными пользователями
    demo_chats = {
        '1_3': [  # Чат между владельцем (1) и партнером (3)
            {
                'user_id': '1',
                'user_name': 'Адам Ламберг',
                'user_avatar_initials': 'АЛ',
                'text': 'Марина, как идут продажи новой коллекции?',
                'timestamp': datetime.now().replace(hour=9, minute=10)
            },
            {
                'user_id': '3',
                'user_name': 'Марина Волкова',
                'user_avatar_initials': 'МВ',
                'text': 'Отлично! Уже продали 60% товара. Клиенты очень довольны качеством.',
                'timestamp': datetime.now().replace(hour=9, minute=15)
            },
            {
                'user_id': '1',
                'user_name': 'Адам Ламберг',
                'user_avatar_initials': 'АЛ',
                'text': 'Супер! Готовим для вас специальные условия на следующий заказ.',
                'timestamp': datetime.now().replace(hour=9, minute=20)
            }
        ],
        '1_4': [  # Чат между владельцем (1) и филиалом (4)
            {
                'user_id': '1',
                'user_name': 'Адам Ламберг',
                'user_avatar_initials': 'АЛ',
                'text': 'Добрый день, Сергей! Как дела в торговом центре?',
                'timestamp': datetime.now().replace(hour=11, minute=5)
            },
            {
                'user_id': '4',
                'user_name': 'Сергей Сидоров',
                'user_avatar_initials': 'СС',
                'text': 'Здравствуйте! Всё отлично, высокая проходимость.',
                'timestamp': datetime.now().replace(hour=11, minute=10)
            }
        ],
        '3_4': [  # Чат между партнером (3) и филиалом (4)
            {
                'user_id': '3',
                'user_name': 'Марина Волкова',
                'user_avatar_initials': 'МВ',
                'text': 'Сергей, как там наши остатки по линзам?',
                'timestamp': datetime.now().replace(hour=10, minute=45)
            },
            {
                'user_id': '4',
                'user_name': 'Сергей Сидоров',
                'user_avatar_initials': 'СС',
                'text': 'Осталось около 30 штук, нужно будет заказать ещё.',
                'timestamp': datetime.now().replace(hour=10, minute=48)
            }
        ],
        '4_5': [  # Чат между филиалами (4 и 5)
            {
                'user_id': '4',
                'user_name': 'Сергей Сидоров',
                'user_avatar_initials': 'СС',
                'text': 'Анна, у вас есть оправы модели X15?',
                'timestamp': datetime.now().replace(hour=14, minute=20)
            },
            {
                'user_id': '5',
                'user_name': 'Анна Иванова',
                'user_avatar_initials': 'АИ',
                'text': 'Да, есть 5 штук. Нужны?',
                'timestamp': datetime.now().replace(hour=14, minute=25)
            }
        ]
    }

    return demo_chats.get(chat_key, [])


def save_support_chat_message(user_id, chat_id, message_text):
    """Сохраняет сообщение в чат поддержки"""
    # В реальном приложении здесь будет сохранение в базу данных
    print(f"Сообщение в чат поддержки от {user_id}: {message_text}")
    return True


def save_partner_chat_message(user_id, partner_id, message_text):
    """Сохраняет сообщение в групповой чат партнера"""
    # В реальном приложении здесь будет сохранение в базу данных
    print(f"Сообщение в чат партнера {partner_id} от {user_id}: {message_text}")
    return True


def save_direct_message(user_id, recipient_id, message_text):
    """Сохраняет прямое сообщение между пользователями"""
    # В реальном приложении здесь будет сохранение в базу данных
    print(f"Сообщение от {user_id} для {recipient_id}: {message_text}")
    return True