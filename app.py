import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle

app = dash.Dash()

#load in data file
DATA_PATH = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH + '/df_patient.pickle', 'rb')
df_patient = pickle.load(pickle_in)
    
colors = {
    'header_background': '#111111',
    'text': '#7FDBFF',
    'graph_background': '#FFFFFF',
    'page_background': '#FFFFFF'
}
app.layout = html.Div(style={'backgroundColor': colors['header_background']}, children=[
    html.H1(
        children='COVID-19 Coronavirus',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Subtitle', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': df_patient['region'], 'y': df_patient['age'], 'type': 'bar'},
            ],
            'layout': {
                'plot_bgcolor': colors['graph_background'],
                'paper_bgcolor': colors['page_background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    
])



if __name__ == '__main__':
    app.run_server(debug=True)