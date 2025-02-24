from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms.password_form import PasswordForm
from models import create_user

password_bp = Blueprint('password', __name__)

@password_bp.route('/password', methods=['GET', 'POST'])
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        phone = request.args.get('phone')  # Получаем номер из URL (на реальном проекте лучше хранить в сессии)
        password = form.password.data
        create_user(phone, password)
        flash("Вы успешно зарегистрированы!", "success")
        return redirect(url_for('phone.phone'))
    return render_template('password.html', form=form)
