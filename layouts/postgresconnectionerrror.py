from utils import UrlIndex
import dash_html_components as html
from components import NavBar, Header, PostgresConnectionErrorModal
import dash_bootstrap_components as dbc


def Body():
    return html.Div(
        [
            PostgresConnectionErrorModal(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Container([
                dbc.Card([
                    dbc.CardBody([
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H1('Cannot establish connection with PostgreSQL database!', className="card-text",
                                style={'text-align': "center", 'color': 'red'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Div(html.I(className="fas fa-satellite-dish fa-7x", style={'color': 'red'}),
                                 style={'text-align': "center"}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br()
                    ])
                ])
            ]),
        ]
    )


def PostgresConnectionError():
    return html.Div([
        Header(),
        NavBar(UrlIndex.SESSION_TIMEOUT.value),
        Body(),
    ])
