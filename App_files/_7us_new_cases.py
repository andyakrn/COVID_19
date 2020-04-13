from imports import *

states = us_df['State'].unique()
states.sort()

hardest_hit_states = list(us_df.groupby(
    'State').agg('max')['Confirmed'].sort_values(ascending=False)[0:7].index)


state_dropdown = dcc.Dropdown(id='state_dropdown',
                                 options=[{'label': i, 'value': i}
                                          for i in states],
                                 value=hardest_hit_states[0],
                                 placeholder='Select a State',
                                 style={'font-family': font['font'],
                                        })

new_us_log_cases = us_df.loc[us_df['State'].isin(
    hardest_hit_states)]

new_state_cases_fig = px.line(new_us_log_cases,
                              x='Confirmed',
                              y='New_Weekly_Cases',
                              log_x='True',
                              log_y='True',
                              template='plotly_dark',
                              color='State',
                              title='New Cases to Confirmed Cases (Log Scale)'
                              )

new_state_cases_fig.update_layout(font={'family': font['font'],
                                        'color': colors['text']},
                                  paper_bgcolor=colors['graph_background'],
                                  plot_bgcolor=colors['graph_background'],
                                  yaxis_title='New Weekly Cases'
                                  )

new_state_cases_fig.update_xaxes(range=[1, 6])
new_state_cases_fig.update_yaxes(range=[1, 6])
new_state_cases_fig.update_yaxes(tickvals=[10, 100, 1000, 10000, 100000])

new_state_cases_figure = dcc.Graph(id='new_state_cases_figure',
                                   style=small_viz_style,
                                   figure=new_state_cases_fig)

new_state_cases_bar_figure = dcc.Graph(id='new_state_cases_bar_figure',
                                       style={'border': '.5pt solid #a6a6a6',
                                              'width': '99.5%'})

new_state_cases_fig_and_dropdown_container = html.Figure(children=[state_dropdown,
                                                             new_state_cases_bar_figure],
                                                   style={'width': '50%',
                                                          'margin': '0px',
                                                          'border': '.5pt solid #a6a6a6', })

new_state_cases_figure = html.Figure(
    style=small_viz_container_style,
    children=[new_state_cases_fig_and_dropdown_container,
              new_state_cases_figure])


def new_state_cases(app):
    @app.callback(
        Output('new_state_cases_bar_figure', 'figure'),
        [Input('state_dropdown', 'value')])
    def new_cases_by_state(state):
        state_df = us_df.loc[us_df['State'] == state]
        state_df['Yesterday_Cases'] = state_df['Confirmed'].shift(1)
        state_df['New Cases'] = state_df['Confirmed'] - \
            state_df['Yesterday_Cases']
        fig = px.bar(state_df,
                     x='Date',
                     y='New Cases',
                     template='plotly_dark',
                     title='New Cases by Day in {}'.format(state),
                     color_discrete_sequence=['red'])
        fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                          paper_bgcolor=colors['graph_background'],
                          plot_bgcolor=colors['graph_background'])
        fig.update_xaxes(tickangle=45, dtick=7)
        return fig
