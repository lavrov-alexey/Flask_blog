from sqlalchemy.orm import relationship

from blog.app import db


# импортируем экземпляр Алхимии из осн. нашего приложения и наследуясь от ее базовой модели - описываем свою модель
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60), nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    articles = relationship("Article")

    def __repr__(self):
        return f"User #{self.id}, email: {self.email}"

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Article #{self.id}, tittle: {self.title[:20]} ... {self.title[-20:]}"
