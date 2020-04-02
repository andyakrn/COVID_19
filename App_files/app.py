from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(
    style=main_app_style,
    children=[
        headers,
        world_map,
        confirmed_active_graphs,
        interactive_graph,
        graphs4_5,
        country_comparison_figure,
        new_cases_figure])

#Callbacks
update_world_map(app)
total_and_cases_per_million_country(app)
total_and_cases_per_million_highest_cases(app)
status_comparison_graph(app)
new_cases(app)

if __name__ == '__main__':
    app.run_server(debug=True)
