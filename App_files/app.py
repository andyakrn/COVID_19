from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(

    style=main_app_style,
    children=[
        headers,
        world_map,
        graph_figures,
        interactive_graph,
        graphs4_5,
        country_comparison_figure,
        new_cases_figure])

update_world_map(app)
updated_country_confirmed_million(app)
update_countries_highest_confirmed_cases(app)
status_comparison_graph(app)
new_cases(app)


if __name__ == '__main__':
    app.run_server(debug=True)
