
from colors import colors
from imports import *

DATA_PATH1 = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH1 + '/COVID_Hopkins_df.pickle', 'rb')
grouped_df = pickle.load(pickle_in)

DATES = list(set(pd.to_datetime(grouped_df['Date']).unique()))

slider_text = html.P(
    id="slider-text",
    style={'color': colors['text']},
    children="Drag the slider to change the date:",
)
slider = dcc.Slider(
    id="years-slider",
    min=min(DATES),
    max=max(DATES),
    value=min(DATES),
    marks={
        str(date): {
            'label': str(date),
            'style': {'color': colors['text']},
        }
        for date in DATES
    },
)
#test