from imports import *

countries = grouped_df['Country/Region'].unique()

graph4 = dcc.Graph(id='plot_by_country', style=small_viz_style)

graph5 = dcc.Graph(id='global_plot', style=small_viz_style)

country_dropdown = dcc.Dropdown(id='country_dropdown',
                                options=[{'label': i, 'value': i}
                                         for i in countries],
                                value='China',
                                placeholder='Select a Country',
                                style={'font-family': font['font'],
                                       })

type_of_cases = ['Total', 'Confirmed Cases Per 1M']

type_of_cases_radio_items = dcc.RadioItems(id='type_of_cases_radio',
                                           options=[{'label': i, 'value': i}
                                                    for i in type_of_cases],
                                           value='Total',
                                           style=radio_item_style)

interactive_graph = html.Figure(style={'display': 'flex',
                                       'flex-direction': 'column',
                                       'margin-left': '0px',
                                       'margin-right': '0px',
                                       'margin-bottom': '0px'},
                                children=[type_of_cases_radio_items, country_dropdown])

graphs4_5 = html.Figure(style={'display': 'flex',
                               'margin-left': '0px',
                               'margin-right': '0px',
                               'margin-top': '0px'},
                        children=[graph4, graph5])

all_graphs = html.Figure(children=[interactive_graph, graphs4_5])