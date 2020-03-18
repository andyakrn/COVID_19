from imports import *

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

graph_figures = html.Figure(
    style={'display': 'flex',
           'flex-direction': 'row',
           'margin-left': '0px',
           'margin-right': '0px'
           },
    children=[graph1, graph2])

countries = grouped_df['Country/Region'].unique()

graph4 = dcc.Graph(id='plot_by_country')


country_dropdown = dcc.Dropdown(
    id='country_dropdown',
    options=[{'label': i, 'value': i} for i in countries],
    value='China',
    placeholder='Select a Country'
    )

status = ['Confirmed', 'Active', 'Recovered', 'Deaths']

status_radio_items = dcc.RadioItems(
    id='status_radio',
    options=[{'label': i, 'value': i} for i in status],
    value='Confirmed',
    style={'border': '.5pt solid #a6a6a6',
           'fontsize': 20,
           'color': colors['text']})

interactive_graph = html.Figure(
    style={'display': 'flex',
           'flex-direction': 'column',
           'margin-left': '0px',
           'margin-right': '0px',
           'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
           'border': '.5pt solid #a6a6a6'},
    children=[status_radio_items, country_dropdown, graph4])
