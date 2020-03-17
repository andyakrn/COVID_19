from imports import *

app = dash.Dash(__name__, )

app.layout = html.Main(
    style={
        'backgroundColor': colors['body_background'],
        'width': '97%',
        'padding': '10px',
        'display': 'flex',
        'flex-direction': 'column',
    },
    children=[
        headers,
        world_map,
        graph_figures,
        big_graph,
        all_buttons],
)

# @app.callback(Output('Worldmap2', 'figure'), [Input('map-states', 'value')])
# def update_map(selected_state):
#     filtered_map = df[df['state'] == selected_state]
#     return{ 
#         'data' : [dict(
#         type = 'scattergeo',
#         locationmode = 'USA-states',
#         lon = filtered_map['long'],
#         lat = filtered_map['lat'],
#         text = filtered_map['text'],
#         mode = 'markers',
#         marker = dict(
#             size = 8,
#             opacity = 0.8,
#             reversescale = True,
#             autocolorscale = False,
#             symbol = 'square',
#             line = dict(
#                 width=1,
#                 color='rgba(102, 102, 102)'
#             ),
#             colorscale = scl,
#             cmin = 0,
#             color = df['cnt'],
#             cmax = df['cnt'].max(),
#             colorbar=dict(
#                 title="Incoming flightsFebruary 2011"
#             )
#         ))],
# 'layout': dict(
#         title = 'Most trafficked US airports<br>(Hover for airport names)',
#         colorbar = True,
#         geo = dict(
#             scope='usa',
#             projection=dict( type='albers usa' ),
#             showland = True,
#             landcolor = "rgb(250, 250, 250)",
#             subunitcolor = "rgb(217, 217, 217)",
#             countrycolor = "rgb(217, 217, 217)",
#             countrywidth = 0.5,
#             subunitwidth = 0.5
#         ),
#     )}

# @app.callback(
#     Output('user-output', 'children'),
#     [Input('age', 'value'),
#      Input('gender', 'value'),
#      Input('pre_cond', 'value')])
# def return_inputs(age, gender, pre_cond):
#     return 'I am a {a} year old {g}, with {h} pre-existing health conditions.'.format(a = age, g = gender, h = pre_cond)


if __name__ == '__main__':
    app.run_server(debug=True)
