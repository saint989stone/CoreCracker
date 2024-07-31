"""
Модуль запуска приложения верхнего уровяня. Импорт экземпляра приложения.
Создает сценарий Python на верхнем уровне, определяющий экземпляр приложения Flask.
Экземпляр приложения Flask называется app и входит в пакет app.
# from app import app импортирует переменную app, входящую в пакет app.
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    """
    Функция хранения контекста запуска в оболочке
    :return:
    """
    return {'db': db, 'User': User, 'Post': Post}

