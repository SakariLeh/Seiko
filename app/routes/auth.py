from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from app.models.user import User
from app.utils.validators import validate_phone, validate_password

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET'])
def index():
    # Если пользователь уже аутентифицирован, перенаправляем на панель управления
    if 'user_id' in session:
        return redirect(url_for('dashboard.index'))
    return render_template('index.html')


@auth_bp.route('/phone_validation', methods=['POST'])
def phone_validation():
    phone = request.form.get('phone', '').strip()

    # Удаляем возможные пробелы, скобки, дефисы и плюсы
    phone = phone.replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('+', '')

    if not validate_phone(phone):
        return render_template('index.html', error='Введите корректный номер телефона в формате 998XXXXXXXXX',
                               phone=phone)

    # Сохраняем телефон в сессии
    session['phone'] = phone

    # Перенаправляем на страницу ввода пароля
    return render_template('password.html', phone=phone)


@auth_bp.route('/password_validation', methods=['POST'])
def password_validation():
    phone = request.form.get('phone', '')
    password = request.form.get('password', '')

    if not validate_password(password):
        return render_template('password.html', error='Введите корректный 4-значный пароль', phone=phone)

    # Аутентификация пользователя
    user = User.authenticate(phone, password)

    if not user:
        return render_template('password.html', error='Неверный номер телефона или пароль', phone=phone)

    # Сохраняем информацию о пользователе в сессии
    session['user_id'] = user.id
    session['role'] = user.role

    # Перенаправляем на панель управления
    return redirect(url_for('dashboard.index'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))