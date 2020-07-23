from wtforms import PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField


class RegistrationForm(BaseForm):
    name = StringField("Usuário", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired()])
    password = PasswordField("Senha", validators=[InputRequired()])
    submit = SubmitField("Enviar")


class LoginForm(BaseForm):
    name = StringField("Usuário ou Email", validators=[InputRequired()])
    password = PasswordField("Senha", validators=[InputRequired()])
    submit = SubmitField("Enviar")


class ConfirmForm(BaseForm):
    submit = SubmitField("Reenviar")


class ResetPasswordRequestForm(BaseForm):
    email = EmailField("Email", validators=[InputRequired()])
    submit = SubmitField("Enviar")


class ResetPasswordForm(BaseForm):
    password = PasswordField("Senha", validators=[InputRequired()])
    submit = SubmitField("Enviar")
