from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(
    style=main_app_style,
    children=[
        headers,
        dcc.Tabs([
            world_tab,
            us_tab
            ]),
        all_buttons])

# Callbacks
update_world_map(app)
status_comparison_graph(app)
update_us_map(app)
new_state_cases(app)
new_cases(app)

if __name__ == '__main__':
    app.run_server(debug=True)
