from App_files.imports import *

world_tab = dcc.Tab(label='World Data',
                    children=[world_map,
                              new_cases_figure,
                              large_figure],
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