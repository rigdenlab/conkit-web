import dash_bootstrap_components as dbc
import dash_html_components as html
from components import InvalidFormatCard
from utils import UrlIndex


def InvalidFileCollapse(dataset):
    return [
        dbc.Collapse(InvalidFormatCard(), id={'type': "invalid-collapse", 'index': dataset}, is_open=True),
        html.Br()
    ]


def InvalidAddTrackCollapse():
    return dbc.Collapse(InvalidFormatCard(), id='invalid-track-collapse', is_open=True)


def InvalidLoginCollapse():
    return dbc.Collapse(
        dbc.Card(
            dbc.CardBody([
                html.P("Invalid username or password, please try again."),
                html.U(dbc.NavLink('If you forgot your password, get in touch with us', href=UrlIndex.CONTACT.value))
            ],
                style={'text-align': "center"}
            ),
            color="danger",
            outline=True
        ),
        id='invalid-login-collapse', is_open=False
    )


def InvalidNewUserCollapse():
    return dbc.Collapse(
        dbc.Card(
            dbc.CardBody("Invalid username or email address! Either your username or the provided email address are "
                         "already used on ConPlot.", style={'text-align': "center"}),
            color="danger",
            outline=True
        ),
        id='invalid-create-user-collapse', is_open=False
    )
