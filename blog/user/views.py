from flask import Blueprint, render_template
from flask_login import login_required
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
@login_required
def profile(pk: int):
    from blog.models import User

    user_from_db = User.query.filter_by(id=pk).one_or_none()
    if not user_from_db:
        raise NotFound(f"Пользователя #{pk} не существует!")
    return render_template(
        'users/profile.html',
        user=user_from_db,
    )
