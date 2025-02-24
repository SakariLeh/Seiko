from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms.phone_form import PhoneForm

phone_bp = Blueprint('phone', __name__)

@phone_bp.route('/phone', methods=['GET', 'POST'])
def phone():
    form = PhoneForm()
    if form.validate_on_submit():
        phone_number = form.phone.data
        return redirect(url_for('password.password'))
    return render_template('phone.html', form=form)
