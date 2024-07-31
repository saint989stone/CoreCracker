"""
Модуль функции просмотра
Attibutes
---------
example : str
    путь к основному каталогу приложений

Class
-----
LoginForm : class
    класс определяющий форму авторизации пользователя.

Methods
-------
@app.route над функцией — декораторы, уникальная особенность языка Python. Декоратор изменяет функцию, которая
следует за ней. Общий шаблон с декораторами — использовать их для регистрации функций как обратных вызовов для
определенных событий. В этом случае декоратор @app.route создает связь между URL-адресом, заданным как аргумент,
и функцией. В этом примере есть два декоратора, которые связывают URL-адреса / и /index с этой функцией.
Это означает, что когда веб-браузер запрашивает один из этих двух URL-адресов, Flask будет вызывать эту функцию
и передавать возвращаемое значение обратно в браузер в качестве ответа.
index()
    функция просмотра главной страницы.
login()
    функция просмотра страницы авторизации.
register()
    функция просмотра страницы регистрациии.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db  # экземпляр приложения Flask называется app и входит в пакет app. from app import app импортирует переменную app, входящую в пакет app.
from app.email import send_password_reset_email
from app.forms import LoginForm, RegistrationForm, PostForm, ResetPasswordRequestForm, UtilizationForm, UtilizationFormHost
from app.models import User, Post
from app import parser

@app.before_request
def before_request():
    """
    Функция выполняющая действия перед выполнение любой функции просмотра
    :return:
    """
    if current_user.is_authenticated:   #запись последнего запроса пользователем
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required   #защита страницы от анонимных пользователей
def index():
    """Функция просмотра главной страницы. Возврщает HTML сгенированный методом "render_template" flask
       Принимает шаблон "index.html" c заполнителем "PostForm" модуля "form" """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)   #добавляем новый пост в базу данных
        db.session.commit()
        flash('Post is ')
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)   #получение номера страницы из запроса GET
    posts = current_user.followed_posts().paginate(page, app.config['POSTS_PER_PAGE'], False)  #извлечение сообщений при помощи метода paginate()
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None   #url адрес,возвращаемый только в том случае если есть страница в этом направлении. Если объекты Pagination будут False, в этом случае ссылка будет установлена на None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Explore', form=form, posts=posts.items, next_url=next_url, prev_url=prev_url) #функция принимает имя файла шаблона и переменную список аргументов шаблона и возвращает один и тот же шаблон, но при этом все заполнители в нем заменяются фактическими значениями.

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Функция просмотра страницы авторизации. Возврщает HTML сгенированный методом "render_template" flask
       Принимает шаблон "login.html" c заполнителем "LoginForm" модуля "form"
    """
    if current_user.is_authenticated:   #проверка на регистрацию текущего пользователя
        return redirect(url_for('index'))   #перенаправление на главную страницу
    form = LoginForm()
    if form.validate_on_submit():   #в случае отправки запроса: GET метод validate возвращает False; POST метод в результате нажатия пользователем кнопки submit, validate собирает все данные, запускает валидаторы, прикрепленные к полям, и возвращает True
        user = User.query.filter_by(username=form.username.data).first()   #поиск пользователя в базе данных
        if user is None or not user.check_password(form.password.data):   #проверка на валидный имя пользователя и пароль
            flash('Invalid username or password')   #сообщение об ошибке
            return redirect(url_for('login'))   #перенаправление на страницу авторизации
        login_user(user, remember=form.remember_me.data)  #пользователь регистрируется устанавливается переменная current_user для этого пользователя
        next_page = request.args.get('next')    #получаем значение аргумента next из GET запроса
        if not next_page or url_parse(next_page).netloc != '':  #если next_page пустая или вставлен url другого ресурса
            next_page = url_for('index')  #перенабравлея на главную страницу
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    """
    Функция выхода из приложения пользователя
    :return:
    """
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Функция просмотра страницы регистрации. Возврщает HTML сгенированный методом "render_template" flask
       Принимает шаблон "register.html" c заполнителем "RegistrationForm" модуля "form"
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are a registred user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/explore')
@login_required
def explore():
    """
    Функция просмотра страницы постов. Принмает шаблон "index.html"
    :return:
    """
    page = request.args.get('page', 1, type=int)  # получение номера страницы из запроса GET
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)   #извлечение сообщений при помощи метода paginate()
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None   #url адрес,возвращаемый только в том случае если есть страница в этом направлении. Если объекты Pagination будут False, в этом случае ссылка будет установлена на None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Explore', posts=posts.items, next_url=next_url, prev_url=prev_url)

@app.route('/user/<username>')
@login_required
def user(username):
    """
    Функция просмотра страницы профиля. c постами пользователя
    :param username:
    :return:
    """
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page',1 , type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)   #запрос на получение постов пользователя order_by используется для получения новых постов
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None #url_for может передавать несколько аргументов в get запросе
    return render_template('user.html', user=user, posts=posts.items, next_url=next_url, prev_url=prev_url)

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    """
    Функция просмотра страницы сброса пароля
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """
    Функция просмотра страницы запроса на сброс пароля по email
    :param token:
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)   #метод возвражает объект пользователя по токену
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/utilization', methods=['GET', 'POST'])
@login_required
def utilization():
    util_strg_trgr = url_for('utilization_string_trigger')
    util_hosts = url_for('utilization_hosts')
    return render_template('utilization.html',  util_strg_trgr=util_strg_trgr, util_hosts=util_hosts)

@app.route('/utilization_string_trigger', methods=['GET', 'POST'])
@login_required
def utilization_string_trigger():
    form = UtilizationForm()
    content = None
    if form.validate_on_submit():
        trigger = form.string.data
        instance = form.instance.data
        zabxDirn = parser.uninUtilParsStrgTrgr(trigger, instance)
        return render_template('utilization_string_trigger.html', form=form, content=zabxDirn)
    return render_template('utilization_string_trigger.html', form=form, content=content)

@app.route('/utilization_hosts', methods=['GET', 'POST'])
@login_required
def utilization_hosts():
    form = UtilizationFormHost()
    content = None
    if form.validate_on_submit():
        hosts = form.string.data
        instance = form.instance.data
        zabxDirn = parser.parsHosts(hosts, instance)
        return render_template('utilization_hosts.html', form=form, content=zabxDirn)
    return render_template('utilization_hosts.html', form=form, cotent=content)

