colors = {
    'body_background': '#181A1C',
    'header_background': '#232629',
    'text': '#d6d9dc',
    'graph_background': '#232629',
    'page_background': '#181A1C',
    'bar_color': '#b30000'}

font = {'font': 'Optima'}

main_app_style = {'backgroundColor': colors['body_background'],
                  'width': '97%',
                  'padding': '10px',
                  'display': 'flex',
                  'flex-direction': 'column',
                  }

large_viz_container_style = {'display': 'flex',
                             'flex-direction': 'column',
                             'margin-left': '0px',
                             'margin-right': '0px',
                             'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                             'border': '.5pt solid #a6a6a6'}

large_viz_style = {'margin-right': '5px',
                   'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                   'width': '100%',
                   'padding': '0',
                   'border': '.5pt solid #a6a6a6'}

small_viz_container_style = {'display': 'flex',
                             'flex-direction': 'row',
                             'margin-left': '0px',
                             'margin-right': '0px',
                             }

small_viz_style = {'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                   'width': '50%',
                   'padding': '0',
                   'border': '.5pt solid #a6a6a6',
                   'font-color': colors['text']}

radio_item_style = {'border': '.5pt solid #a6a6a6',
                    'fontsize': 20,
                    'color': colors['text'],
                    'backgroundColor': colors['header_background'],
                    'font-family': font['font'],
                    }

button_style = {'color': colors['text'],
                'font-size': '11px',
                'border-radius': '10px',
                'border': '.5pt solid #a6a6a6',
                'height': '40px',
                'width': '130px',
                'max-width': '200px',
                'background-color': colors['header_background'],
                'box-shadow': '0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)',
                'font-family': font['font'],
                'cursor': 'pointer'}

summary_style = {'textAlign': 'left',
                 'backgroundColor': colors['header_background'],
                 'color': colors['text'],
                 'font-size': '14px',
                 'padding-left': '2%',
                 'padding-right': '2%',
                 'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                 'margin-bottom': '5px',
                 'margin-top': '0px',
                 'width': '96%',
                 'line-height': '1.7',
                 'font-family': font['font']}

header_1_style = {'backgroundColor': colors['header_background'],
                  'textAlign': 'center',
                  'color': colors['text'],
                  'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                  'margin-top': '0px',
                  'margin-bottom': '0px',
                  'width': '100%',
                  'font-family': font['font']}

prediction_style = {'textAlign': 'left',
                    'backgroundColor': colors['header_background'],
                    'color': colors['text'],
                    'font-size': '14px',
                    'padding-left': '2%',
                    'padding-right': '2%',
                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                    'margin-bottom': '5px',
                    'width': '96%',
                    'line-height': '1.7',
                    'font-family': font['font'],
                    'border': '.5pt solid #a6a6a6'}

interactive_graph_style = {'display': 'flex',
                           'flex-direction': 'column',
                           'margin-left': '0px',
                           'margin-right': '0px',
                           'margin-bottom': '0px'}

button_container_style = {'display': 'flex',
                          'flex-direction': 'row',
                          'justify-content': 'space-between'}
