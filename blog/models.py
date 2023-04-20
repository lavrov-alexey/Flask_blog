from blog.app import db


# импортируем экземпляр Алхимии из осн. нашего приложения и наследуясь от ее базовой модели - описываем свою модель
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60), nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
