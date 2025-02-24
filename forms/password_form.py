from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, Length

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Пароль должен быть не менее 8 символов")
    ])
