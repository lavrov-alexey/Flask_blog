from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()  # создаем экземпляр Алхимии
login_manager = LoginManager()  # создаем экземпляр логин-менеджера


# создаем в функции приложение Flask (передав имя выполняемого модуля)  и возвращаем его экземпляр
# используем паттерн "Фабрика по созданию приложений"
def create_app() -> Flask:
    app = Flask(__name__)
    # конфиги для прода, разработки и т.п. - можно выносить и подгружать из файлов разн. формата
    # app.config.from_pyfile('config.py')

    # либо можно задать конфигурацию непосредственно в коде:
    # в учебных целях - ключ будет здесь, для прода - должен лежать где-то секьюрно
    # SQLALCHEMY_TRACK_MODIFICATIONS: если вкл. - Flask-SQLAlchemy будет отслеживать изменения объектов и
    # отправлять сигналы. По умолчанию - None, которое включает отслеживание, но выдает предупреждение о том,
    # что в будущем оно будет отключено по умолчанию. Поэтому если нет необходимости - лучше отключить явно
    # SQLALCHEMY_DATABASE_URI - в учебных целях будем исп. БД sqlite
    app.config['SECRET_KEY'] = '@9&5#1eiu4x7ta$*hpbdiw0q&4ukc)nj06l5dy&abc5n3@s5_c'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # инициализируем в Алхимии наше приложение
    db.init_app(app)

    login_manager.login_view = 'auth.login'  # задаем вьюху для логина
    login_manager.init_app(app)

    from .models import User, Article

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    # @login_manager.unauthorized_handler
    # def unauthorized():
    #     return redirect(url_for('auth.login'))

    register_blueprints(app)
    return app


# создаем функцию для регистрации блюпринтов (эскизов), на вход - приложение (экземпляр Flask)
def register_blueprints(app: Flask):
    from blog.articles.views import article
    from blog.auth.views import auth
    from blog.user.views import user

    # вызываем для переданного приложения станд. функцию регистрации блюпринт, передав в нее имя блюпринта
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
