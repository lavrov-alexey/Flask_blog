from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

# создаем эскиз user, параметр url_prefix позволит обратиться к url "localhost/users"
user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# Пока не работаем с БД - создадим глобальную константу с данными о пользователях
# USERS = ['Иван', 'Мария', 'Владимир']  # вариант простого списка
# вариант имитации объекта с id (pk)
USERS = {
    1: 'Иван',
    2: 'Мария',
    3: 'Владимир',
}


# регистрируем роут в созданном ранее блюпринте юзер, т.е. обращение будет к корню
# урла "localhost/users/"
@user.route('/')
def user_list():
    # вызываем функцию отрисовки шаблона и передаем в контекст шаблона наших пользователей, чтобы исп-вать в шаблоне
    return render_template(
        'users/list.html',
        users=USERS,
    )

@user.route('/<int:pk>')
def get_user(pk: int):
    # обработка варианта передачи несуществующего id
    try:
        user_name = USERS[pk]
    except KeyError:
        # вариант с обработкой и отображением ошибки
        # raise NotFound(f'User id {pk} not found!')
        # вариант с перенаправлением польвателя например на список пользователей
        return redirect('/users/')
    return render_template(
        'users/details.html',
        user_name=user_name,
    )
