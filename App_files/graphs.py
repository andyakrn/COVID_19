from imports import *

countries = grouped_df['Country/Region'].unique()

graph4 = dcc.Graph(id='plot_by_country', style=small_viz_style)

graph5 = dcc.Graph(id='global_plot', style=small_viz_style)

country_dropdown = dcc.Dropdown(id='country_dropdown',
                                options=[{'label': i, 'value': i}
                                         for i in countries],
                                value='United States',
                                placeholder='Select a Country',
                                style={'font-family': font['font']})

type_of_cases = ['Total', 'Confirmed Cases Per 1M']

type_of_cases_radio_items = dcc.RadioItems(id='type_of_cases_radio',
                                           options=[{'label': i, 'value': i}
                                                    for i in type_of_cases],
                                           value='Total',
                                           style=radio_item_style)

interactive_graph = html.Figure(style=interactive_graph_style,
                                children=[type_of_cases_radio_items, country_dropdown])

graphs4_5 = html.Figure(style={'display': 'flex',
                               'margin-left': '0px',
                               'margin-right': '0px',
                               'margin-top': '0px'},
                        children=[graph4, graph5])

all_graphs = html.Figure(children=[interactive_graph, graphs4_5])

types_of_cases1 = ['Confirmed', 'Active', 'Recovered', 'Deaths']

type_of_cases_radio_items1 = dcc.RadioItems(id='type_of_cases_radio1',
                                            options=[{'label': i, 'value': i}
                                                     for i in types_of_cases1],
                                            value='Confirmed',
                                            style=radio_item_style)

hardest_hit_countries = list(grouped_df.groupby('Country/Region').agg('max')['Confirmed'].sort_values(ascending=False)[0:3].index)

country_choices = dcc.Dropdown(id='country_dropdown1',
                               options=[{'label': i, 'value': i}
                                        for i in countries],
                               value=hardest_hit_countries,
                               placeholder='Select Countries',
                               style={'font-family': font['font']},
                               multi=True)

country_comparison_graph = dcc.Graph(id='country_comparison_graph')

country_comparison_figure = html.Figure(style=large_viz_container_style,
                                        children=[type_of_cases_radio_items1, country_choices, country_comparison_graph])
