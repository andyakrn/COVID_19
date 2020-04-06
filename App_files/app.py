from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(
    style=main_app_style,
    children=[
        headers,
        dcc.Tabs([
            dcc.Tab(label='World Data',
                    children=[world_map, country_comparison_figure,
                              new_cases_figure],
                    style={'border': '.5pt solid #a6a6a6',
                           'font-family': font['font'],
                           'backgroundcolor': colors['body_background'],
                           'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                           'font-color': colors['text'],
                           'border-radius': '10px',
                           'borderTop': '1px solid #d6d6d6'
                           },
                    selected_style={'border': '.5pt solid #a6a6a6',
                                    'font-family': font['font'],
                                    'backgroundcolor': colors['body_background'],
                                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                                    'font-color': colors['text'],
                                    'border-radius': '10px',
                                    'fontWeight': 'bold',
                                    'borderTop': '1px solid #d6d6d6'}
                    ),
            dcc.Tab(label='U.S. Data',
                    style={'border': '.5pt solid #a6a6a6',
                           'font-family': font['font'],
                           'backgroundcolor': colors['body_background'],
                           'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                           'font-color': colors['text'],
                           'border-radius': '10px',
                           'borderTop': '1px solid #d6d6d6'
                           },
                    selected_style={'border': '.5pt solid #a6a6a6',
                                    'font-family': font['font'],
                                    'backgroundcolor': colors['body_background'],
                                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                                    'font-color': colors['text'],
                                    'border-radius': '10px',
                                    'fontWeight': 'bold',
                                    'borderTop': '1px solid #d6d6d6'}
                    )
        ]
        ),
        # world_map,
        # # confirmed_active_graphs,
        # # interactive_graph,
        # # graphs4_5,
        # country_comparison_figure,
        # new_cases_figure,

        all_buttons])

# Callbacks
update_world_map(app)
# total_and_cases_per_million_country(app)
# total_and_cases_per_million_highest_cases(app)
status_comparison_graph(app)
new_cases(app)

if __name__ == '__main__':
    app.run_server(debug=True)
