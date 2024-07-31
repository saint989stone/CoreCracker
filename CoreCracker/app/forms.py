"""
Модуль хранения классов веб-форм

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
example(str)
    функция перебирает ключи
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
import app.regular as regr
import app.zabxmax as zabx
import unicodedata

class LoginForm(FlaskForm):
    """
    Класс определяющий форму авторизации пользователя. Наследуется от класса FlaskForm модуля flask_wtf
    Attributes
    ----------
    username : str
        атрибут формы "Username", определяемый методом StringField с валидатором непустого значения ataRequired
    password : str
        атрибут формы "Password", определяемый методом PasswordField с валидатором непустого значения DataRequired
    remember_me : bool
        атрибут чек-бокса "Remember Me", определяемый методом BooleanField с валидатором непустого значения DataRequired
    submit :
        атрибут кнопки "Sign In"
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    """
    Класс определяющий форму регистрации пользователя. Наследуется от класса FlaskForm
    Attributes
    ----------
    username : str
        атрибут формы "Username", определяемый методом StringField с валидатором непустого значения DataRequired
    password : str
        атрибут формы "Password", определяемый методом PasswordField с валидатором непустого значения DataRequired, Email
    password2 : bool
        атрибут формы "Repeat Password" определяемый методом PasswordField  с валидатором непустого значения DataRequired, EqualTo (проверяющий на идентичность)
    submit :
        атрибут кнопки "Sign In"

    Methods
    -------
    validate_username(str)
        функция-валидатор проверки существования пользователя в базе данных

    validate_email(str)
        функция-валидатор проверки существования email в базе данных
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self, username):
        """
        Функция-валидатор проверки существования пользователя в базе данных
        :param username: str
        :return: raise
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """
        Функция-валидатор проверки существования email в базе данных
        :param email: str
        :return: raise
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PostForm(FlaskForm):
    """
    Класс определяющий форму post
    """
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    """
        Класс определяющий форму сброса пароля. Наследуется от класса FlaskForm
        Attributes
        ----------
        email : str
            атрибут формы "Username", определяемый методом StringField с валидатором непустого значения DataRequired, и Email()
        submit :
            атрибут кнопки "Sign In"

        Methods
        -------
        exam(str)
            функция-валидатор проверки существования пользователя в базе данных

        """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    """
    Класс определяющий форму сброса просмотра страницы запроса на сброс пароля по email
    """
    password = PasswordField('Password', validators=[DataRequired])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Password Reset')

class UtilizationForm(FlaskForm):
    """
    Класс определяющий форму для отправки строки триггеров из Zabbix
    """
    string = TextAreaField('Строка триггеров Zabbix: ', validators=[DataRequired()], default='')
    instance = SelectField('Экземпляр Zabbix: ', choices=[('mpls', 'mpls'), ('west', 'west')])
    submit = SubmitField('ПУСК')
    def validate_string (self, string):
        listContErrr = list()
        trgrErrr = False
        string = str(string)[45:]
        tempList = string.split('\n')
        for cont, strg in enumerate(tempList):
            if 'Link change state' in strg:
                listHost = list()
                strgList = strg.split(' ')
                for elem in strgList:
                    host = regr.serhHost(elem)
                    if host: listHost.append(host)
                if len(listHost) != 2:
                    trgrErrr = True
                    listContErrr.append(cont + 1)

        if trgrErrr:
            strgErrr = str()
            if len(listContErrr) == 1:
                strgErrr = 'Строка {} не содержит необходимого количества (2) имен хостов'.format(' '.join(map(str, listContErrr)))
            elif len(listContErrr) > 1:
                strgErrr = 'Строки {} не содержит необходимого количества (2) имен хостов'.format(' '.join(map(str, listContErrr)))
            raise ValidationError(strgErrr)

class UtilizationFormHost(UtilizationForm):
    """
    Класс определющий форму для отправки направления Точки A - Точки. Наследуется от UtilizationForm
    """
    string = TextAreaField('Имя хоста(ов)<br>Точка А - Точка Б (Точка А - Соседи)', validators=[DataRequired()], default='')
    def validate_string(self, string):
        trgrErrrPatn = False   #Триггер связанный с определением количества указанных хостов в соотвествии с шаблонами
        trgrErrrLimt = False   #Триггер связанный с определением лимита по хостам
        string = str(string)[45:-11]
        listSymlExcn = ['\x20', '\xa0', '\n', '.', ';', '!', '?', ':', ' - ', '&lt;', '&gt;', '*']
        listHost = list()
        for syml in listSymlExcn:   #Блок проверки на недопустимые символы
            if syml in string:
                raise ValidationError('Cимвол' + ' [ ' + unicodedata.name(syml) + ' ] ' + 'в позиции ' + str(string.index(syml)) + ' явлется недопустимым')

        if ',' in string:   #Блок проверки на соответствие шаблонам для нескольких направлений
            contSymlDirn = string.count(',') + 1
            tempList = string.split(',')
            trgrChekDirn = False   #Тригер включается когда идет проверка по Точка А - Точка Б
            trgrChekHost = False   #Триггер включается когда идет проверка по Точка А - Соседи
            if '_' in string:
                trgrChekDirn = True
                for elem in tempList:
                    if '_' in elem:  #проверка Точка А - Точка Б
                        listTempHost = elem.split('_')
                        for hostTemp in listTempHost:
                            host = regr.serhHost(hostTemp)
                            if host: listHost.append(host)

            else:   #проверка Точка A - Соседи
                trgrChekHost = True
                for elem in tempList:
                    host = regr.serhHost(elem)
                    if host: listHost.append(host)

            if trgrChekDirn:  #Блок включения триггеров Точка А - Точка Б
                if len(listHost) > 6: trgrErrrLimt = True  #включение триггера на привышение лимита количества напралвения > 3
                if len(listHost)/contSymlDirn % 2 != 0: trgrErrrPatn = True  #проверка на количество указанных хостов, вычесляется по остатку от деления количества хостов на кол-во знаков '_' + 1, в случае верного == 0

            if trgrChekHost:  #Блок включения триггеров Точка A - Соседи
                if len(listHost) > 1: trgrErrrLimt = True
                if len(listHost) != contSymlDirn: trgrErrrPatn = True


        else:   #Блок проверки на соответствие шаблонам для одного направления
            if '_' in string:   #Блок проверки Точка А - Точка Б
                tempList = string.split('_')
                for strg in tempList:
                    host = regr.serhHost(strg)
                    if host: listHost.append(host)
                if len(listHost) > 2: trgrErrrLimt = True
                if len(listHost) != 2: trgrErrrPatn = True

            else:   #Блок проверки Точка А - соседи
                host = regr.serhHost(string)
                listHost.append(host)
                if len(listHost) > 1: trgrErrrLimt = True
                if len(listHost) < 1: trgrErrrPatn = True

        if trgrErrrLimt:
            raise ValidationError('Превышен лимит количества указанных имен хостов')

        if trgrErrrPatn:  #Вывод сообщения о несоответствии шаблонам
            raise ValidationError('Количество имен хостов не соотвествует шаблону')

        else:   #Вывод сообщения о не найденных именах хостов в экземплярах Zabbix
            listHostErrr = zabx.chekHostID(listHost)
            if listHostErrr != []:
                if len(listHostErrr) == 1:
                    raise ValidationError('В экзеплярах Zabbix не обнаружено имя хоста' + ' ' + str(listHostErrr))
                else:
                    raise ValidationError('В экзеплярах Zabbix не обнаружено следующих именов хостов:' + ' ' + str(listHostErrr))
