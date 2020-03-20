from imports import *

status = ['Confirmed', 'Active', 'Recovered', 'Deaths']

map_status_radio_items = dcc.RadioItems(
    id='map_status_radio',
    options=[{'label': i, 'value': i} for i in status],
    value='Confirmed',
    style=radio_item_style)

world_map_by_status = dcc.Graph(id='world_map_by_status')

world_map = html.Figure(
    style=large_viz_container_style,
    children=[map_status_radio_items, world_map_by_status])

