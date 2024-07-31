"""
Модуль хранения конфигураций приложения, где переменные определяются как ключи словаря

Attibutes
---------
example : str
    путь к основному каталогу приложений

basedir :
    путь на основной каталог приложения

Class
-----
Config : class
    класс предназначен для хранения конфигураций в виде словаря

Methods
-------
example(str)
    функция перебирает ключи
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Класс Config используется для хранения переменных в виде словаря
    Attibutes
    ---------
    SECRET_KEY : str
        значение секретного ключа используемого расширениями 1-ый ищет значение перменной среды, 2-ой жестко закодированная строка

    SQLALCHEMY_DATABASE_URI : path
        местоположение базы данных приложения app.db

    SQLALCHEMY_TRACK_MODIFICATIONS :
        включает тригер приложению о внесенние изменений в базу данных

    POSTS_PER_PAGE :
        указывает на количество отображаемых сообщений на странице
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
