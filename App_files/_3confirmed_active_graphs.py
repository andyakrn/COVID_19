from App_files.imports import *

graph_df = grouped_df.groupby('Date').agg('sum').reset_index()
graph_df['Date'] = pd.to_datetime(graph_df['Date'])
graph_df = graph_df.sort_values('Date')

confirmed_graph = dcc.Graph(
    id='Graph1',
    style=small_viz_style,
    figure=px.bar(graph_df,
                  x='Date',
                  y='Confirmed',
                  title='Global Confirmed Cases',
                  color_discrete_sequence=['red'],
                  template='plotly_dark').update_layout(font={'family': font['font'],
                                                              'color': colors['text']},
                                                        paper_bgcolor=colors['graph_background'],
                                                        plot_bgcolor=colors['graph_background']))
active_graph = dcc.Graph(
    id='Graph2',
    style=small_viz_style,
    figure=px.bar(graph_df,
                  x='Date',
                  y='Active',
                  title='Global Active Cases',
                  color_discrete_sequence=['yellow'],
                  template='plotly_dark').update_layout(font={'family': font['font'], 'color': colors['text']},
                                                        paper_bgcolor=colors['graph_background'],
                                                        plot_bgcolor=colors['graph_background']))

confirmed_active_graphs = html.Figure(
    style=small_viz_container_style,
    children=[confirmed_graph, active_graph])