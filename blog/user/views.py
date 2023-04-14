from flask import Blueprint, render_template

# создаем эскиз user, параметр url_prefix позволит обратиться к url "localhost/users"
user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# Пока не работаем с БД - создадим глобальную константу с данными о пользователях
USERS = ['Иван', 'Мария', 'Владимир']


# регистрируем роут в созданном ранее блюпринте юзер, т.е. обращение будет к корню
# урла "localhost/users/"
@user.route('/')
def user_list():
    # вызываем функцию отрисовки шаблона и передаем в контекст наших пользователей, чтобы исп-вать в шаблоне
    return render_template(
        'users/list.html',
        users=USERS,
    )

@user.route('/<pk>')
def get_user(pk: int):
    return pk
