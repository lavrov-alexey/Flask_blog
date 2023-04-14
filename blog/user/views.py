from flask import Blueprint

# создаем эскиз user, параметр url_prefix позволит обратиться к url "localhost/users"
user = Blueprint('user', __name__, url_prefix='users', static_folder='../static')


# регистрируем роут в созданном ранее блюпринте юзер, т.е. обращение будет к корню
# урла "localhost/users/"
@user.route('/')
def user_list():
    return 'Hello user'
