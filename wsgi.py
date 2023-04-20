# Запуск тренировочного приложения к уроку 1
# from blog.app import app
#
# if __name__ == '__main__':
#     app.run(
#         host='0.0.0.0',
#         port=5005,  # по-умолчанию если не указывать - порт 5000
#         debug=True
#     )
from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()


# регистрируем команды команд. строки в нашем экземпляре приложения Flask
# создаем команду инициализации БД и создания всех таблиц (запуск в ком. строке: flask init-db)
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB created!')

# заводим команду создания нескольких пользователей
@app.cli.command('create-users')
def create_users():
    from blog.models import User

    # создаем хеш пароля для создания потом пользователя встроенной в веб-серв. функцией
    hash_password = generate_password_hash('1qaz2wsx')
    # создаем экземпляр пользователя
    test_user = User(email='test@email.com', password=hash_password)
    db.session.add(test_user)  # добавляем нашего пользователя
    db.session.commit()  # и применяем изменения в нашей сессии

    print('Created test_user!')
