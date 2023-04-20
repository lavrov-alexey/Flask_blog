from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

# создаем эскиз user, параметр url_prefix позволит обратиться к url "localhost/users"
user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# регистрируем роут в созданном ранее блюпринте юзер, т.е. обращение будет к корню
# урла "localhost/users/"
@user.route('/')
def user_list():
    from blog.models import User

    users_from_db = User.query.all()
    # вызываем функцию отрисовки шаблона и передаем в контекст шаблона наших пользователей, чтобы исп-вать в шаблоне
    return render_template(
        'users/list.html',
        users=users_from_db,
    )

@user.route('/<int:pk>')
def get_user(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f"User id #{pk} doesn't exist!")
    return render_template(
        'users/details.html',
        user=_user,
    )
