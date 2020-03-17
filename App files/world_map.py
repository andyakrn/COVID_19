from imports import *

max_cases = grouped_df['Confirmed'].max()

fig = px.choropleth(
    grouped_df,
    locations=grouped_df['Country/Region'],
    locationmode='country names',
    color=grouped_df['Confirmed'],
    hover_name='Country/Region',
    title='Confirmed Cases by Country Over Time<br>(Hover for Country Names)',
    color_continuous_scale=['green', 'yellow', 'orange', 'orangered', 'red'],
    projection='natural earth',
    animation_frame='Date',
    range_color=[0, max_cases],
    template='plotly_dark',

)
fig.update_layout(paper_bgcolor=colors['graph_background'])

style = {'margin-right': '5px',
         'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
         'width': '100%',
         'padding': '0',
         'border': '.5pt solid #a6a6a6',
         }

world_map = html.Figure(
    style={'display': 'flex',
           'flex-direction': 'column',
           'margin-left': '0px',
           'margin-right': '0px'

           },
    children=[dcc.Graph(figure=fig, style=style)])
