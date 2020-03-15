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

        html.Div([map_states], style = {'width': '48%', 'display': 'inline-block'}),


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


@app.callback(Output('Worldmap2', 'figure'), [Input('map-states', 'value')])
def update_map(selected_state):
    filtered_map = df[df['state'] == selected_state]
    return{ 
        'data' : [dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = filtered_map['long'],
        lat = filtered_map['lat'],
        text = filtered_map['text'],
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
        ))],
'layout': dict(
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
    )}

if __name__ == '__main__':
    app.run_server(debug=True)
