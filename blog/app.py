from time import time

from flask import Flask, g
from flask import request

# создаем экземпляр приложения и в качестве параметра нужно передать название текущего модуля
app = Flask(__name__)

# в декораторе регистрируем базовую (стартовую) точку входа к нашему приложению index
# @app.route('/')
# def index():
#     return 'Hello!'
    # return 'Hello!', 201  # если нужно - можно передать возвращаемый код ответа сервера, напр. 201, вместо станд. 200
    # return Response('Hello!')  # можно также возвращать экземпляр объекта Response со множ. своих параметров

# передаем в пути параметр (напр. - "город")
# @app.route('/<city>')
# def index(city: str):
#     return f'Hello {city}!'

# указание типа переменной в роуте (при другом типе - будет 404 ошибка)
# @app.route('/<int:some_id>')
# def index(some_id: int):
#     return f'Идентификатор {some_id}!'


# добавление query-параметров в пути (например http://127.0.0.1:5005/123 или http://127.0.0.1:5005/123?name=Alex)
# также опционально - можно указать доступные методы для этого эндпоинта
@app.route('/<string:some_str>', methods=['GET', 'POST'])
def index(some_str: str):
    # из словаря query-параметров запроса (request.args) можем получить по имени нужный параметр станд. методом словаря
    test_param = request.args.get('test_param', None)
    return f'Строка в url {some_str}, переданный параметр (test_param): {test_param}, метод запроса: {request.method=}'


# декараторы before_request и after_request - позволяют выполнять опред. логику до и/или после работы flask
@app.before_request
def fix_time_start_app():
    # в рамках каждого запроса есть свой "глобальный" объект g, в кот. можно хранить необходимые данные
    g.start_time = time()


@app.after_request
def calc_time_app(response):
    # получаем из g время начала вып. запроса, вычисляем время выполнения запроса flask и возвр. его в заголовках
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time
    return response


# создаем свой обработчик для кода ошибки 404
@app.errorhandler(404)
def handler_404(curr_error):
    # регистрируем ошибку во встроенном логгере приложения (уровень - error)
    app.logger.error(curr_error)
    return '404'
