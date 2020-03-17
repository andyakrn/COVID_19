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
#test
)
if __name__ == '__main__':
    app.run_server(debug=True)
