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
        html.Div(
            style={'display': 'flex',
                   'flex-direction': 'column'
                   },
            children=[header1, header2, summary1, summary2]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'column',
                   'margin-left': '0px',
                   'margin-right': '0px'

                   },
            children=[world_map]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'row',
                   'margin-left': '0px',
                   'margin-right': '0px'

                   },
            children=[graph1, graph2]),

        html.Div(
            id="slider-container",
            children=[slider_text, slider]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'column',
                   'margin-left': '0px',
                   'margin-right': '0px'
                   },
            children=[world_map3]),

        html.Figure(
            style={'display': 'flex',
                   'flex-direction': 'row',
                   'justify-content': 'space-between'
                   },
            children=[brian_button, andrei_button, christy_button, chinwe_button]),


    ],

)

if __name__ == '__main__':
    app.run_server(debug=True)
