from imports import *

status = ['Confirmed', 'Active', 'Recovered', 'Deaths']

map_status_radio_items = dcc.RadioItems(
    id='map_status_radio',
    options=[{'label': i, 'value': i} for i in status],
    value='Confirmed',
    style=radio_item_style)

world_map_by_status = dcc.Graph(id='world_map_by_status')

# max_cases = grouped_df['Confirmed'].max()

# fig = px.choropleth(
#     grouped_df,
#     locations=grouped_df['Country/Region'],
#     locationmode='country names',
#     color=grouped_df['Confirmed'],
#     hover_name='Country/Region',
#     title='Confirmed Cases by Country Over Time (2020) <br>(Hover for Country Names)',
#     color_continuous_scale=['green', 'yellow', 'orange', 'orangered', 'red'],
#     projection='natural earth',
#     animation_frame='Date',
#     range_color=[0, max_cases],
#     template='plotly_dark')
# fig.update_layout(paper_bgcolor=colors['graph_background'],
#                   font={'family': font['font'], 'color': colors['text']},
#                   )

world_map = html.Figure(
    style=large_viz_container_style,
    children=[map_status_radio_items, world_map_by_status])

