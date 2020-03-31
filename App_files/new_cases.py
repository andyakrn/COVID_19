from imports import *

country_dropdown2 = dcc.Dropdown(id='country_dropdown2',
                                 options=[{'label': i, 'value': i}
                                          for i in countries],
                                 value='United States',
                                 placeholder='Select a Country',
                                 style={'font-family': font['font']})

# grouped_df.sort_values('Datetime', inplace=True)
# global_total_df = grouped_df.groupby('Datetime').agg('sum')
# global_total_df['Yesterday_Cases'] = global_total_df['Confirmed'].shift(1)
# global_total_df['New_Cases'] = global_total_df['Confirmed'] - \
#     global_total_df['Yesterday_Cases']

# new_cases_fig1 = px.bar(global_total_df,
#                         x=global_total_df.index,
#                         y='New_Cases',
#                         template='plotly_dark',
#                         title='Global New Cases by Day',
#                         color_discrete_sequence = ['red'])

# new_cases_fig1.update_layout(font={'family': font['font'],
#                                    'color': colors['text']},
#                              paper_bgcolor=colors['graph_background'],
#                              plot_bgcolor=colors['graph_background'],
#                              yaxis_title='New Cases',
#                              xaxis_title='Date',
#                              )

# new_cases_figure1 = dcc.Graph(id='new_graph1',
#                               style=small_viz_style,
#                               figure=new_cases_fig1)

new_cases_fig1 = px.line(grouped_df,
                        x='Confirmed',
                        y='New Weekly Cases',
                        log_x='True',
                        log_y='True',
                        template='plotly_dark',
                        color='Country/Region',
                        title='New Cases to Confirmed Cases (Log Scale)',
                        )

new_cases_fig1.update_layout(font={'family': font['font'],
                                   'color': colors['text']},
                             paper_bgcolor=colors['graph_background'],
                             plot_bgcolor=colors['graph_background'],
                             )

new_cases_figure1 = dcc.Graph(id='new_graph1',
                              style=small_viz_style,
                              figure=new_cases_fig1)

new_cases_figure2 = dcc.Graph(id='new_graph2',
                              style=small_viz_style)

graph_figures2 = html.Figure(
    style=small_viz_container_style,
    children=[new_cases_figure1, new_cases_figure2])

new_cases_figure = html.Figure(style=large_viz_container_style,
                               children=[country_dropdown2,
                                         graph_figures2])
