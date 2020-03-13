import dash
import dash_core_components as dcc
import dash_html_components as html
from colors import colors
import pandas as pd
import pickle

# load in data file
DATA_PATH = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH + '/df_patient.pickle', 'rb')
df_patient = pickle.load(pickle_in)

world_map = dcc.Graph(
    id='Worldmap1',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '100%',
       
    },
    figure={
        'data': [
            {'x': df_patient['region'],
             'y': df_patient['age'],
             'type': 'bar'
             },
        ],
        'layout': {
            'title': 'Test Title',
            'plot_bgcolor': colors['graph_background'],
            'paper_bgcolor': colors['graph_background'],
            'font':
            {'color': colors['text']
             },


        }
    },
)

graph1 = dcc.Graph(
    id='Graph1',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '50%'
    },
    figure={
        'data': [
            {'x': df_patient['region'],
             'y': df_patient['age'],
             'type': 'bar'
             },
        ],
        'layout': {
            'title': 'Test Title',
            'plot_bgcolor': colors['graph_background'],
            'paper_bgcolor': colors['graph_background'],
            'font':
            {'color': colors['text']
             },


        }
    },
)
graph2 = dcc.Graph(
    id='Graph2',
    style={
        'margin-left': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '50%',
        'padding': '0'
    },
    figure={
        'data': [
            {'x': df_patient['region'],
             'y': df_patient['age'],
             'type': 'bar'
             },
        ],
        'layout': {
            'title': 'Test Title',
            'plot_bgcolor': colors['graph_background'],
            'paper_bgcolor': colors['graph_background'],
            'font':
            {'color': colors['text']
             },

        }
    }
)
