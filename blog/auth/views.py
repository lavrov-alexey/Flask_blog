from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, static_folder='../static')


# регистрируем функции входа и выхода как роуты нашего приложения аутентификации
@auth.route('/login', methods=['POST', 'GET'])
def login():
    # если ГЕТ - просто отрисовываем шаблон, если ПОСТ - работаем с переданными данными
    if request.method == 'GET':
        return render_template('auth/login.html')

    # получаем данные из отправленной формы авторизации
    email = request.form.get('email')
    password = request.form.get('password')

    # пробуем найти пользователя по полученному email
    from blog.models import User

    user_from_db = User.query.filter_by(email=email).first()
    # если пользователь не нашелся или если хеш хранимого пароля не совпал с хешем введенного
    if not user_from_db or not check_password_hash(user_from_db.password, password):
        # через функцию flash можно пробросить сообщение во фронт и там обработать нужным образом
        flash('Введённые данные авторизации некорректны!')
        return redirect(url_for('.login'))

    login_user(user_from_db)
    return redirect(url_for('user.profile', pk=user_from_db.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
