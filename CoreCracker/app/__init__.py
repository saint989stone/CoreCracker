"""
Модуль инициализации приложения, содержит экземпляры всех установлнных раснирениий

Attibutes
---------
app : str
    переменная __name__, переданная в класс Flask, является предопределенной переменной Python, которая задается именем
    модуля, в котором она используется. Flask использует расположение модуля, переданного здесь как отправную точку.

app :
    cтроковый «config» — это имя модуля python config.py, и, очевидно, тот, который имеет верхний регистр «C», является
    фактическим классом.

db :
    представляет базу данных

migrate :
    представляет механизм миграции

login :
    представляет механизм регистрации пользователя в приложении

login.login_view:
    определяет конечную точку для входа в систему. "login" является именем функции, другими словами использоваться в вызове url_for(), чтобы получить URL

Class
-----
Config : class
    класс предназначен для хранения конфигураций в виде словаря

Methods
-------
example(str)
    функция перебирает ключи
"""
import os, logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
moment = Moment(app)
mail = Mail(app)
login.login_view = 'login'

if not app.debug:   #запуск логирования в режиме debug is False
    if app.config['MAIL_SERVER']:   #отправка по SMTP
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):   #запись в журнал Логов
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/corecracker.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))   #задает формат введения журнала
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Corecracker startup')

from app import routes, models, errors
"""
#существуют два объекта с именем app. Пакет приложения определяется каталогом приложения и сценарием __init__.py и
# указан в инструкции routes импорта приложения. Переменная app определяется как экземпляр класса Flask в сценарии
# __init__.py, что делает его частью пакета приложения. собенность заключается в том, что модуль routes импортируется
# внизу, а не наверху скрипта, как это всегда делается. Нижний импорт является обходным путем для циклического импорта,
# что является общей проблемой при использовании приложений Flask. Вы увидите, что модуль routes должен импортировать
# переменную приложения, определенную в этом скрипте, поэтому, поместив один из взаимных импортов внизу, вы избежите
# ошибки, которая возникает из взаимных ссылок между этими двумя файлами.
"""
