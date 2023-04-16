from flask import Flask

from blog.articles.views import article
from blog.user.views import user


# создаем в функции приложение Flask (передав имя выполняемого модуля)  и возвращаем его экземпляр
# используем паттерн "Фабрика по созданию приложений"
def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

# создаем функцию для регистрации блюпринтов (эскизов), на вход - приложение (экземпляр Flask)
def register_blueprints(app: Flask):
    # вызываем для переданного приложения станд. функцию регистрации блюпринт, передав в нее имя блюпринта
    app.register_blueprint(user)
    app.register_blueprint(article)
