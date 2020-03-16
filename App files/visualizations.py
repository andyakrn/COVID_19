
from imports import *


# load in data file
DATA_PATH = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH + '/df_patient.pickle', 'rb')
df_patient = pickle.load(pickle_in)

world_map = dcc.Graph(
    id='Worldmap1',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '100%'},
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
           
            'color': colors['text']
             ,
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

            'color': colors['text']

        }
    }
)
# bubble map with animation
# https://plot.ly/python/bubble-maps/

scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
       [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]

DATA_PATH1 = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH1 + '/COVID_Hopkins_df.pickle', 'rb')
grouped_df = pickle.load(pickle_in)


data = [ dict(
        type = 'scattergeo',
        locationmode = 'country names',
        locations = grouped_df['Country/Region'],
        
      
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = grouped_df['Confirmed'],
            cmax = grouped_df['Confirmed'].max(),
            colorbar=dict(
                title="Test"
            )
        ))]

layout = dict(
        title = 'Test Title<br>(Hover for Country Names)',
        colorbar = True,
        geo = dict(
            scope='world',
            projection=dict(type='natural earth'),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ))

    # 'plot_bgcolor': colors['graph_background'],
    # 'paper_bgcolor': colors['graph_background'],
    # 'color': colors['text']

