from imports import *

countries = grouped_df['Country/Region'].unique()

graph4 = dcc.Graph(id='plot_by_country')

country_dropdown = dcc.Dropdown(
    id='country_dropdown',
    options=[{'label': i, 'value': i} for i in countries],
    value='China',
    placeholder='Select a Country',
    style={'font-family': font['font']})

interactive_graph = html.Figure(
    style=large_viz_container_style,
    children=[graph4, country_dropdown])
