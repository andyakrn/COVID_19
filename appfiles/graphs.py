from appfiles.imports import *

graph1 = dcc.Graph(
    id='Graph1',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '50%',
        'border': '.5pt solid #a6a6a6',
    },
    figure={
        'data': [
            {'x': df_patient['Date'],
             'y': df_patient['Confirmed'],
             'type': 'bar'
             },
        ],
        'layout': {
            'title': 'Test Title',
            'plot_bgcolor': colors['graph_background'],
            'paper_bgcolor': colors['graph_background'],
            'color': colors['text'],
            'font':
            {'color': colors['text']},
        }
    },
)
graph2 = dcc.Graph(
    id='Graph2',
    style={
        'margin-left': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '50%',
        'padding': '0',
        'border': '.5pt solid #a6a6a6',
    },
    figure={
        'data': [
            {'x': df_patient['Date'],
             'y': df_patient['Confirmed'],
             'type': 'bar'
             },
        ],
        'layout': {
            'title': 'Test Title',
            'plot_bgcolor': colors['graph_background'],
            'paper_bgcolor': colors['graph_background'],
            'color': colors['text'],
            'font': {'color': colors['text']}
        }
    }
)

graph3 = dcc.Graph(
    id='Worldmap1',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '100%',
        'border': '.5pt solid #a6a6a6',
    },
    figure={
        'data': [
            {'x': df_patient['Date'],
             'y': df_patient['Confirmed'],
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

graph_figures = html.Figure(
    style={'display': 'flex',
           'flex-direction': 'row',
           'margin-left': '0px',
           'margin-right': '0px'
           },
    children=[graph1, graph2])

big_graph = html.Figure(
    style={'display': 'flex',
           'flex-direction': 'column',
           'margin-left': '0px',
           'margin-right': '0px'
           },
    children=[graph3])
#border