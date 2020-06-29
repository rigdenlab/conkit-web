import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import UrlIndex


def NavBar(pathname=None):
    return dbc.Nav([
        dbc.NavItem(
            dbc.NavLink(
                html.H4("Home", className='mt-1', style={'color': (
                    'white' if pathname == UrlIndex.HOME.value or pathname == UrlIndex.ROOT.value else 'black')}),
                active=(pathname == UrlIndex.HOME.value or pathname == UrlIndex.ROOT.value),
                href=UrlIndex.HOME.value
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                html.H4("Plot", className='mt-1',
                        style={'color': ('white' if pathname == UrlIndex.PLOT.value else 'black')}),
                active=(pathname == UrlIndex.PLOT.value),
                href=UrlIndex.PLOT.value
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                html.H4("Get in touch", className='mt-1',
                        style={'color': ('white' if pathname == UrlIndex.CONTACT.value else 'black')}),
                active=(pathname == UrlIndex.CONTACT.value),
                href=UrlIndex.CONTACT.value
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                html.H4("Help", className='mt-1',
                        style={'color': ('white' if pathname == UrlIndex.HELP.value else 'black')}),
                active=(pathname == UrlIndex.HELP.value),
                href=UrlIndex.HELP.value
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                html.H4("Rigden Lab", className='mt-1',
                        style={'color': ('white' if pathname == UrlIndex.RIGDEN.value else 'black')}),
                active=(pathname == UrlIndex.RIGDEN.value),
                href=UrlIndex.RIGDEN.value
            )
        )
    ], pills=True, fill=True, justified=True
    )
