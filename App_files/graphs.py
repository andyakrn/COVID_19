from imports import *

countries = grouped_df['Country/Region'].unique()

graph4 = dcc.Graph(id='plot_by_country', style=small_viz_style)

graph5 = dcc.Graph(id='global_plot', style=small_viz_style)

country_dropdown = dcc.Dropdown(id='country_dropdown',
                                options=[{'label': i, 'value': i}
                                         for i in countries],
                                value='China',
                                placeholder='Select a Country',
                                style={'font-family': font['font']})

type_of_cases = ['Total', 'Confirmed Cases Per 1M']

type_of_cases_radio_items = dcc.RadioItems(id='type_of_cases_radio',
                                           options=[{'label': i, 'value': i}
                                                    for i in type_of_cases],
                                           value='Total',
                                           style=radio_item_style)


interactive_graph = html.Figure(style=small_viz_container_style,
                                children=[graph4, graph5])

interactive_graph_inputs = html.Figure(children=[type_of_cases_radio_items, country_dropdown],
                                       style={'display': 'flex',
                                              'flex-direction': 'column',
                                              'width': '100%',
                                              'margin-left': '0px',
                                              'margin-right': '0px'})
