# # общая конфигурация
# class Config:
#     FLASK_DEBUG = False
#
#
# # конфигурация для разработки (наслед. от общего конфига)
# class Development(Config):
#     FLASK_DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

# или без разбивки на разные конфиги - просто единый конфиг
FLASK_DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
TESTING = True
SECRET_KEY = ''
