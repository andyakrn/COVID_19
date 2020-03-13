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
#bubble map with animation 
#https://plot.ly/python/bubble-maps/
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df.head()

df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [ dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df['long'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = df['cnt'],
            cmax = df['cnt'].max(),
            colorbar=dict(
                title="Incoming flightsFebruary 2011"
            )
        ))]
layout = dict(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        colorbar = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
fig = dict( data=data, layout=layout )    

world_map2 = dcc.Graph(id = 'Worldmap2', figure = fig)