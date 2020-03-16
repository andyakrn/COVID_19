
from colors import colors
from imports import *

DATA_PATH1 = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH1 + '/COVID_Hopkins_df.pickle', 'rb')
grouped_df = pickle.load(pickle_in)

YEARS = grouped_df['Confirmed'].unique()

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
