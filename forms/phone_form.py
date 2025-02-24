from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

class PhoneForm(FlaskForm):
    phone = StringField('Phone', validators=[
        DataRequired(),
        Regexp(r'^\+?[1-9]\d{1,14}$', message="Введите корректный номер телефона")
    ])
