"""
Модуль определяет структуру базы данных

Class
-----
Config : class
    класс предназначен для хранения конфигураций в виде словаря

Methods
-------
load_user(str)
    функция пользовательского загрузчика

Attibutes
---------
followers :
    таблица ассоциаций отношений многие ко многим
"""

from datetime import datetime
from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from time import time
import jwt

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                     )

class User(UserMixin, db.Model):
    """
    Класс User наследуется от:
        db.Model - базового класса Flask-SQLAlchemy, реализует ORM баз данных
        UserMixin - класс Flask-Login

    Attibutes
    ---------
    id : int
        определяет первичный ключ
    username : str
        определяет имя пользователя строкой с длиной 64
    email : str
        определяет e-mail строкой с длиной 120
    password_hash : str
        определяет hash пароля пользователя строкой с длиной 128
    posts :
        взаимотношение между users и posts. Аргумент backref определяет имя поля, которое будет добавлено к объектам класса
        "много", который указывает на "один"

    Methods
    -------
    set_password()
        создает hash пароля

    check_password()
        осуществляет проверку hash пароля

    follow()
        функция осуществляющая подписку использует метод append()

    unfollow()
        функция осуществляющая отписку использует метод remove()

    is_following()
        функция осуществляющая проверку отношений

    __repr__()
        представление объекта класса через print()

    get_reset_password_token()
        функция генерирует токе JWT в виде строки.

    verivy_reset_password_token(token)
        функция проверки токена
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    followed = db.relationship(
        'User',   #самореферентное отношение. должен использоваться один класс с двух сторон
        secondary=followers,   #конфигурирует таблицу ассоциаций, которая используется для этой связи
        primaryjoin=(followers.c.follower_id == id),   #указывает условие, которое связывает объект follower user с таблицей ассоциаций. followers.c.follower_id - это атрибуты таблиц которые не определены как модели.
        secondaryjoin=(followers.c.followed_id == id),   #определяет условие, которое связывает объект правой стороны (followed user) с таблицей ассоциаций.
        backref=db.backref('followers', lazy='dynamic'),   #определяет как эта связь будет доступна из правой части объекта. С левой стороны отношений followed, поэтому с правой стороны будем использовать followers
        lazy='dynamic'
    )
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        """
        Функция генерирует токе JWT в виде строки. Decode приобразует последовательность байтов в строку
        :param expires_in:
        :return:
        """
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
                            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod   #статический метод может быть вызван из Класса
    def verivy_reset_password_token(token):
        """
        Функция проверки токена. Функция принимает токен и декодирует его.
        Токен неверный или истек срок вызывается исключение, и возвращается None
        Токен верный тогда значение ключа reset_password из полезной нагрузки токена является идентификаторомпользователя
        :param token:
        :return:
        """
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def __repr__(self):
        return '<User {}'.format(self.username)

class Post(db.Model):
    """
        Класс Post наследуется от db.Model, базового класса Flask-SQLAlchemy
        Attibutes
        ---------
        id : int
            определяет первичный ключ
        body : str
            определяет post строкой с длиной 64
        timestamp : str
            индексация по времени
        user_id : str
            ссылка на значения id из таблицы users

        Methods
        -------
        __repr__()
            представление объекта класса через print()
        """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login.user_loader
def load_user(id):
    """
    функция пользовательского загрузчика зарегистрирован в Flask-login c помощью декоратора
    принимает первичный ключ пользователя
    :param id:
    :return:
    """
    return User.query.get(int(id))

