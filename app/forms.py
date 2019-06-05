from flask_wtf import FlaskForm
from wtforms import StringField, \
    PasswordField, BooleanField, \
    SubmitField, SelectField, RadioField, \
    SelectMultipleField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    dialect = SelectField("", choices=[("0", 'Все диалекты'),('1', "Тантынский"), ("2", "Муиринский"), ("3", "Литературный даргинский")])
    searched_word = StringField("", validators=[DataRequired()])
    prochoice = SelectField("", choices=[("1", "Искать слово/перевод"), ("2", "Искать синонимы"), ("3", "Искать когнаты"), ("4", "Искать однокоренные слова")], validators=[DataRequired()])
    prodialect = SelectMultipleField("Диалект", choices=[("1", 'Тантынский'), ("2", 'Муиринский')], default=["1", "2"])
    pos = SelectField("Часть речи", choices=[("0", "не выбрано"), ("1", "глагол"), ("2", "существительное"), ("3", "прилагательное"), ("4", "наречие"), ("5", "местоимение")])
    nounclass = SelectMultipleField("Класс", choices=[("1", "w"), ("2", "r"), ("3", "b"), ("4", "d")])
    verbframe = SelectMultipleField("Управление", choices=[("1", "tr"), ("2", "itr"), ("3", "aff"), ("4", "tr/itr"), ("5", "tr/aff"), ("6", "itr/aff")])
    grammeme = SelectMultipleField("Грамматическая форма", choices=[])
    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


