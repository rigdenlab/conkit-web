import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def ErrorAlert(is_open=False):
    return dbc.Alert([
        html.H4('ERROR', className="alert-heading"),
        html.P([
            "If you suspect a bug, please ",
            html.A(html.U('get in touch'), href=UrlIndex.CONTACT.value),
            " and report this to us, or create an issue on our ",
            html.A(html.U("Github repository"), href=UrlIndex.GITHUB.value, className="alert-link")
        ]),
    ], color='danger', fade=True, is_open=is_open, id='error-alert')


def FilenameAlert(filename, dataset):
    return dbc.Alert(filename, dismissable=True, color="success", is_open=True,
                     id={'type': 'filename-alert', 'index': '["{}", "{}"]'.format(filename, dataset)})


def SuccessChangePasswordAlert(username):
    return dbc.Alert([
        html.H4('Success', className="alert-heading", style={'text-align': "center"}),
        html.P("You have successfully changed %s's password!" % username, style={'text-align': "center"}),
    ],
        dismissable=False,
        color='success',
        fade=True,
        is_open=True,
        id='success-change-password-alert'
    )


def FailChangePasswordAlert(username):
    return dbc.Alert([
        html.H4('Error', className="alert-heading", style={'text-align': "center"}),
        html.P("Something went wrong and we couldn't change %s's password!" % username, style={'text-align': "center"}),
    ],
        dismissable=False,
        color='danger',
        fade=True,
        is_open=True,
        id='fail-change-password-alert'
    )


def SuccessLoginAlert(username):
    return dbc.Alert([
        html.H4('Success', className="alert-heading", style={'text-align': "center"}),
        html.P([
            "You have successfully logged in as '%s'." % username
        ], style={'text-align': "center"}),
    ],
        dismissable=False,
        color='success',
        fade=True,
        is_open=True,
        id='success-login-alert'
    )


def SuccessCreateUserAlert(username):
    return dbc.Alert([
        html.H4('Success', className="alert-heading", style={'text-align': "center"}),
        html.P([
            "You have successfully created a new user. You are now logged in as '%s'." % username
        ], style={'text-align': "center"}),
    ],
        dismissable=False,
        color='success',
        fade=True,
        is_open=True,
        id='success-create-user-alert'
    )


def SuccessLogoutAlert():
    return dbc.Alert([
        html.H4('Success', className="alert-heading", style={'text-align': "center"}),
        html.P([
            "You have successfully logged out"
        ], style={'text-align': "center"}),
    ],
        dismissable=False,
        color='danger',
        fade=True,
        is_open=True,
        id='success-logout-alert'
    )


def ContactBugAlert():
    return dbc.Alert([
        html.H4('Info', className="alert-heading"),
        html.P([
            "If you suspect a bug, you can also create an issue on the our ",
            html.A(html.U("Github repository"), href=UrlIndex.GITHUB.value, className="alert-link")
        ]),
    ],
        dismissable=False,
        color='danger',
        fade=True,
        is_open=True,
        id='bug-alert'
    )


def ContactForgotPsswrdAlert():
    return dbc.Alert([
        html.H4('Info', className="alert-heading"),
        html.P(
            "If you forgot your password, make sure to fill in with your registered username on the 'Name' input field "
            "and the same email address you provided when registering on the 'Email' input field. If we find this "
            "username and email address registered in our site, we will send you an email with further instructions to "
            "recover your password."
        ),
    ],
        dismissable=False,
        color='danger',
        fade=True,
        is_open=True,
        id='forgot-psswrd-alert'
    )


def GdprPolicyAlert(dismissable=True):
    return dbc.Alert([
        'This website requires cookies & limited processing of your personal data in order to function properly. '
        'By making use of ConPlot you are giving your consent to this as outlined in our Privacy Policy.',
        html.Hr(),
        dbc.Button('Read more', color='secondary', size='md', id='gdpr-policy-button')
    ], color='primary', dismissable=dismissable, style={'text-align': "center"})
