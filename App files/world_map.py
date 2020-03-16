from imports import *

world_map3 = dcc.Graph(
    id='Graph3',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '100%',
        'padding': '0'
    },
    figure={
        'data': [
           {'type': 'scattergeo',
            # 'data_frame': grouped_df,
            'locations': 'Country/Region',
            'locationmode': 'country names',
            'size': grouped_df['Confirmed'],

            },
        ],
    }
)