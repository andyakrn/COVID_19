import dash
import dash_core_components as dcc
import dash_html_components as html
from colors import colors

summary_style = {
    'textAlign': 'left',
    'backgroundColor': colors['header_background'],
    'color': colors['text'],
    'font-family': 'Verdana',
    'font-size': '14px',
    'padding-left': '2%',
    'padding-right': '2%',
    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
    'margin-bottom': '10px',
    'width': '96%',
    'line-height': '1.7'
}
header1 = html.H1(
    children='COVID-19 Coronavirus',
    style={
        'backgroundColor': colors['header_background'],
        'textAlign': 'center',
        'color': colors['text'],
        'font-family': 'Verdana',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'margin-top': '5px',
        'width': '100%',
    }
)

header2 = html.Div(
    children='Brian Kosiadi, BS | Andrei Zholud PhD | Christy Liner MBA | Chinwe Egwim, BA',
    style={
        'textAlign': 'center',
        'color': colors['text'],
        'backgroundColor': colors['header_background'],
        'font-family': 'Verdana',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'margin-top': '0px',
        'margin-bottom': '5px',
        'width': '100%',

    })
summary1 = html.Div(
    children='Coronaviruses are a large family of viruses that are common in people and many different species of animals, including camels, cattle, cats, and bats. Rarely, animal coronaviruses can infect people and then spread between people such as with MERS-CoV, SARS-CoV, and now with this new virus (named SARS-CoV-2).',
    style=summary_style
)
summary2 = html.Div(
    children='The SARS-CoV-2 virus is a betacoronavirus, like MERS-CoV and SARS-CoV.  All three of these viruses have their origins in bats. The sequences from U.S. patients are similar to the one that China initially posted, suggesting a likely single, recent emergence of this virus from an animal reservoir. (Source: CDC)',
    style=summary_style
)
