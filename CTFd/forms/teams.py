from wtforms import BooleanField, PasswordField, SelectField, StringField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.countries import SELECT_COUNTRIES_LIST


class TeamJoinForm(BaseForm):
    name = StringField("Nome do Time", validators=[InputRequired()])
    password = PasswordField("Senha do Time", validators=[InputRequired()])
    submit = SubmitField("Participar")


class TeamRegisterForm(BaseForm):
    name = StringField("Nome do Time", validators=[InputRequired()])
    password = PasswordField("Senha do Time", validators=[InputRequired()])
    submit = SubmitField("Criar")


class TeamSettingsForm(BaseForm):
    name = StringField("Nome do time")
    confirm = PasswordField("Senha atual")
    password = PasswordField("Senha do Time")
    affiliation = StringField("Afiliação")
    website = URLField("Website")
    country = SelectField("País", choices=SELECT_COUNTRIES_LIST)
    submit = SubmitField("Enviar")


class TeamCaptainForm(BaseForm):
    # Choices are populated dynamically at form creation time
    captain_id = SelectField("Capitão do Time", choices=[], validators=[InputRequired()])
    submit = SubmitField("Enviar")


class TeamSearchForm(BaseForm):
    field = SelectField(
        "Buscar por campo",
        choices=[
            ("name", "Nome"),
            ("id", "ID"),
            ("affiliation", "Afiliação"),
            ("website", "Website"),
        ],
        default="name",
        validators=[InputRequired()],
    )
    q = StringField("Parâmetro", validators=[InputRequired()])
    submit = SubmitField("Buscar")


class PublicTeamSearchForm(BaseForm):
    field = SelectField(
        "Buscar por campo",
        choices=[
            ("name", "Nome"),
            ("affiliation", "Afiliação"),
            ("website", "Website"),
        ],
        default="name",
        validators=[InputRequired()],
    )
    q = StringField("Parâmetro", validators=[InputRequired()])
    submit = SubmitField("Buscar")


class TeamCreateForm(BaseForm):
    name = StringField("Nome do Time", validators=[InputRequired()])
    email = EmailField("Email")
    password = PasswordField("Senha")
    website = URLField("Website")
    affiliation = StringField("Afiliação")
    country = SelectField("País", choices=SELECT_COUNTRIES_LIST)
    hidden = BooleanField("Escondido")
    banned = BooleanField("Banido")
    submit = SubmitField("Enviar")


class TeamEditForm(TeamCreateForm):
    pass
