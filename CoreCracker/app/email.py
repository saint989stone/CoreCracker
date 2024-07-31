"""
Модуль по работе с электрнной почтой
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
send_async_email(app, msg):
    функция работает из контекта приложения.
send_mail(str)
    функция отправки электронных сообщений
send_password_reset_email(user):
    функция отправки электронных сообщений в фонофом режиме Thread


"""

from flask_mail import Message
from flask import render_template
from app import app, mail
from threading import Thread

def send_async_email(app, msg):
    """
    Функция работает из контекта приложения.
    :param app:
    :param msg:
    :return:
    """
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    """
    Функция отправки электронных сообщений в фонофом режиме Thread
    :param subject:
    :param sender:
    :param recipients:
    :param text_body:
    :param html_body:
    :return:
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start() #функция send_async_email вызывается через класс Thread() и работает в фоновом режиме

def send_password_reset_email(user):
    """
    Функция генерации и отравки сообщения на сброс пароля
    :param user:
    :return:
    """
    token = user.get_reset_password_token()
    send_email('[CoreCracker] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user, token=token),
               html_body=render_template('email/reset_password.html', user=user, token=token))
