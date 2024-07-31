"""
Модуль обработки ошибок

Methods
-------
index()
    функция просмотра главной страницы.
login()

"""
from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    """
    Функция обработки ошибки 404
    :param error:
    :return:
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Функция обработки ошибки 500
    :param error:
    :return:
    """
    db.session.rollback()
    return render_template('500.html'), 500