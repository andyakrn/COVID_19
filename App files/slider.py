import dash
import dash_core_components as dcc
import dash_html_components as html
from colors import colors

YEARS = [2003, 2004, 2005, 2006, 2007, 2008,
         2009, 2010, 2011, 2012, 2013, 2014, 2015]

slider_text = html.P(
    id="slider-text",
    style={'color': colors['text']},
    children="Drag the slider to change the year:",
)

slider = dcc.Slider(
    id="years-slider",
    min=min(YEARS),
    max=max(YEARS),
    value=min(YEARS),
    marks={
        str(year): {
            'label': str(year),
            'style': {'color': colors['text']},
        }
        for year in YEARS
    },
)
