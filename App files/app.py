import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle
from colors import *
from buttons import *
from header_summary import *
from visualizations import *
from dash.dependencies import Input, Output

app = dash.Dash(__name__, )

# load in data file
DATA_PATH = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH + '/df_patient.pickle', 'rb')
df_patient = pickle.load(pickle_in)

app.layout = html.Div(
    style={
        'backgroundColor': colors['body_background'],
        'width': '97%',
        'padding': '10px',
        'display': 'flex',
        'flex-direction': 'column',
    },
    children=[
        html.Div(
            style={'display': 'flex',
                   'flex-direction': 'column'
                   },
            children=[header1, header2, summary1, summary2]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'column',
                   'margin-left': '0px',
                   'margin-right': '0px'

                   },
            children=[world_map]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'row',
                   'margin-left': '0px',
                   'margin-right': '0px'

                   },
            children=[graph1, graph2]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'column',
                   'margin-left': '0px',
                   'margin-right': '0px'

                   },
            children=[world_map2]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'row',
                   'justify-content': 'space-between'
                   },
            children=[brian_button, andrei_button, christy_button, chinwe_button]),
        
     
    ],

)

if __name__ == '__main__':
    app.run_server(debug=True)
