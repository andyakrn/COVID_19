from imports import *

user_age = dcc.Input(id="age",
                     type="number",
                     min=0,
                     max=120,
                     debounce=True,
                     placeholder='Age',
                     style={
                         'margin-left': '5px',
                         'width': '95%',
                         'padding': '0',
                         'font-family': font['font'],
                         'font-size': '14px',
                         'font-color': 'red',
                         'border-radius': '10px', })

user_gender = dcc.Dropdown(id='gender',
                           options=[
                               {'label': 'Male', 'value': 'male'},
                               {'label': 'Female', 'value': 'female'}],
                           placeholder='Gender',
                           style={
                               'margin-left': '5px',
                               'width': '95%',
                               'padding': '0',
                               'border-radius': '10px',
                               'font-family': font['font'],
                               'font-size': '14px',
                               'font-color': 'red'})

submit_button = html.Button(id='submit-button',
                            n_clicks=0,
                            children='Submit',
                            style={'border-radius': '10px',
                            'font-family': font['font']})

user_input = html.Div(id='user-input',
                      children=[user_age, user_gender, submit_button],
                      style={'display': 'flex',
                             'flex-direction': 'row',
                             'width': '100%',
                             'margin-left': '0px',
                             'margin-right': '0px'})

user_output = html.Div(id='user-output',
                       style={'color': colors['text'],
                              'border': '.5pt solid #a6a6a6',
                              'margin-top': '5px',
                              'font-family': font['font']})

graph1 = dcc.Graph(
    id='Graph1',
    style=small_viz_style,
    figure=px.bar(grouped_df,
                  x='Date',
                  y='Confirmed',
                  title='Global Confirmed Cases',
                  color_discrete_sequence=['red'],
                  template='plotly_dark').update_layout(font={'family': font['font'], 'color': colors['text']},
                                                        paper_bgcolor=colors['graph_background'],
                                                        plot_bgcolor=colors['graph_background']))
graph2 = dcc.Graph(
    id='Graph2',
    style=small_viz_style,
    figure=px.bar(grouped_df,
                  x='Date',
                  y='Active',
                  title='Global Active Cases',
                  color_discrete_sequence=['yellow'],
                  template='plotly_dark').update_layout(font={'family': font['font'], 'color': colors['text']},
                                                        paper_bgcolor=colors['graph_background'],
                                                        plot_bgcolor=colors['graph_background']))

graph_figures = html.Figure(
    style=small_viz_container_style,
    children=[graph1, graph2])
