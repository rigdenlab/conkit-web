import dash_html_components as html
import dash_bootstrap_components as dbc
from utils import UrlIndex


def SwampJumbotron():
    return dbc.Jumbotron(
        [
            html.H1([html.Img(src=UrlIndex.SWAMP_LOGO.value), "Swamp"], className="display-3"),
            html.P(
                "Solving structures With Alpha Helical Membrane Pairs ",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Unconventional molecular replacement pipeline that exploits covariance information to "
                "determine the most suitable search models for transmembrane proteins."
            ),
            html.P(dbc.Button("Learn more", color="primary", href=UrlIndex.SWAMP_READDOCS.value,
                              style={'background': '#545f13ee', 'color': 'white'}), className="lead"),
        ], style={'border-style': 'solid', 'border-color': '#545f13ff', 'border-radius': '10px'}
    )


def SimbadJumbotron():
    return dbc.Jumbotron(
        [
            html.H1([html.Img(src=UrlIndex.SIMBAD_LOGO.value), "Simbad"], className="display-3"),
            html.P(
                "Sequence Independent Molecular Replacement Based on Available Database",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "A sequence independent molecular replacement pipeline that provides an alternate strategy "
                "to identify search models in a sequence-independent manner."
            ),
            html.P(dbc.Button("Learn more", href=UrlIndex.SIMBAD_READDOCS.value,
                              style={'background': '#5a4b96ed', 'color': 'white'}),
                   className="lead"),
        ], style={'border-style': 'solid', 'border-color': '#5a4b96ff', 'border-radius': '10px'}
    )


def AmpleJumbotron():
    return dbc.Jumbotron(
        [
            html.H1([html.Img(src=UrlIndex.AMPLE_LOGO.value), "Ample"], className="display-3"),
            html.P(
                "Ab Initio Modelling of Proteins for Molecular Replacement",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "AMPLE is a pipeline for unconventional molecular replacement that exploits advances in protein "
                "bioinformatics to generate search models from structure predictions or available crystal structures."
            ),
            html.P(dbc.Button("Learn more", href=UrlIndex.AMPLE_READDOCS.value,
                              style={'background': '#3572c1ee', 'color': 'white'}),
                   className="lead"),
        ], style={'border-style': 'solid', 'border-color': '#3572c1ff', 'border-radius': '10px'}
    )


def ConkitJumbotron():
    return dbc.Jumbotron(
        [
            html.H1([html.Img(src=UrlIndex.CONKIT_LOGO.value), "Conkit"], className="display-3"),
            html.P(
                "Contact Prediction ToolKit",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Python library to provide a data object hierarchy and associated routine operations to work and "
                "manipulate residue-residue contact prediction data."
            ),
            html.P(dbc.Button("Learn more", href=UrlIndex.CONKIT_READDOCS.value,
                              style={'background': '#6ed0eaec', 'color': 'white'}),
                   className="lead"),
        ], style={'border-style': 'solid', 'border-color': '#6ed0eaff', 'border-radius': '10px'}
    )
