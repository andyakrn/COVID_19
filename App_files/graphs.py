from imports import *

graph1 = dcc.Graph(
    id='Graph1',
    style=small_viz_style,
    figure={
        'data': [
            {'x': grouped_df['Date'],
             'y': grouped_df['Confirmed'],
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
    style=small_viz_style,
    figure={
        'data': [
            {'x': grouped_df['Date'],
             'y': grouped_df['Confirmed'],
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
    style=small_viz_container_style,
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
    style=radio_item_style)

interactive_graph = html.Figure(
    style=large_viz_container_style,
    children=[status_radio_items, country_dropdown, graph4])
