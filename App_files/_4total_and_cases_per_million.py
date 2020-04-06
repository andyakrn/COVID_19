# from imports import *

# countries = grouped_df['Country/Region'].unique()

# plot_by_country = dcc.Graph(id='plot_by_country', style=small_viz_style)

# global_plot = dcc.Graph(id='global_plot', style=small_viz_style)

# country_dropdown = dcc.Dropdown(id='country_dropdown',
#                                 options=[{'label': i, 'value': i}
#                                          for i in countries],
#                                 value='United States',
#                                 placeholder='Select a Country',
#                                 style={'font-family': font['font']})

# type_of_cases = ['Total', 'Confirmed Cases Per 1M']

# type_of_cases_radio_items = dcc.RadioItems(id='type_of_cases_radio',
#                                            options=[{'label': i, 'value': i}
#                                                     for i in type_of_cases],
#                                            value='Total',
#                                            style=radio_item_style)

# radio_and_dropdown = html.Figure(style=interactive_graph_style,
#                                 children=[type_of_cases_radio_items, country_dropdown])

# total_and_highest_graphs = html.Figure(style={'display': 'flex',
#                                'margin-left': '0px',
#                                'margin-right': '0px',
#                                'margin-top': '0px'},
#                         children=[plot_by_country, global_plot])

# countries = grouped_df['Country/Region'].unique()

# graph4 = dcc.Graph(id='plot_by_country', style=small_viz_style)

# graph5 = dcc.Graph(id='global_plot', style=small_viz_style)


# interactive_graph = html.Figure(style=interactive_graph_style,
#                                 children=[type_of_cases_radio_items, country_dropdown])

# graphs4_5 = html.Figure(style={'display': 'flex',
#                                'margin-left': '0px',
#                                'margin-right': '0px',
#                                'margin-top': '0px'},
#                         children=[graph4, graph5])

# all_graphs = html.Figure(children=[interactive_graph, graphs4_5])

# def total_and_cases_per_million_country(app):
#        @app.callback(
#        Output('plot_by_country', 'figure'),
#        [Input('country_dropdown', 'value'),
#        Input('type_of_cases_radio', 'value')])
#        def update_graph(selected_country, type_of_cases):
#               filtered_df = grouped_df.loc[grouped_df['Country/Region']
#                                           == selected_country]
#               melted_df = pd.melt(filtered_df, id_vars=['Date', 'PopTotal'], value_vars=[
#                                    'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
#               date = pd.to_datetime(grouped_df['Date']).dt.date.sort_values(
#                      ascending=False).reset_index(drop=True)[0].strftime('%m/%d/%Y')

#               if type_of_cases == 'Total':
#                      y = 'value'
#               else:
#                      melted_df['Per Capita'] = melted_df['value'] / melted_df['PopTotal']
#                      y = 'Per Capita'
#               fig = px.line(melted_df,
#                             x='Date',
#                             y=y,
#                             title='Cases in {} through {}'.format(
#                                    selected_country, date),
#                             template='plotly_dark',
#                             color='Status',
#                             color_discrete_map={'Recovered': 'Green',
#                                                  'Confirmed': 'Yellow',
#                                                  'Active': 'Orange',
#                                                  'Deaths': 'Red'},
#                             height=350)
#               fig.update_layout(font={'family': font['font'], 'color': colors['text']},
#                                    paper_bgcolor=colors['graph_background'],
#                                    plot_bgcolor=colors['graph_background'],
#                                    yaxis_title='Total Cases')
#               fig.update_xaxes(tickangle=45, dtick=7)
#               return fig

# def total_and_cases_per_million_highest_cases(app):
#        @app.callback(
#        Output('global_plot', 'figure'),
#        [Input('type_of_cases_radio', 'value')])
#        def update_graph(type_of_cases):
#               filtered_df = grouped_df.loc[grouped_df['Country/Region'] != 'Cruise Ship']
#               filtered_df = filtered_df.loc[filtered_df['PopTotal'] > 10000]
#               filtered_df = filtered_df.groupby('Country/Region').agg('max')
#               if type_of_cases == 'Total':
#                      df = filtered_df.sort_values('Confirmed', ascending=False).iloc[:8]
#                      df.sort_values('Confirmed', inplace=True)
#                      x = df['Confirmed']
#                      y = df.index
#               else:
#                      df = filtered_df.sort_values(
#                      'Confirmed Cases Per 1M', ascending=False).iloc[:8]
#                      df.sort_values('Confirmed Cases Per 1M', inplace=True)
#                      x = df['Confirmed Cases Per 1M']
#                      y = df.index
#               fig = px.bar(data_frame=df,
#                             x=x,
#                             y=y,
#                             title='Countries with Highest Confirmed Cases',
#                             template='plotly_dark',
#                             orientation='h',
#                             height=350,
#                             )
#               fig.update_layout(font={'family': font['font'], 'color': colors['text']},
#                                    paper_bgcolor=colors['graph_background'],
#                                    plot_bgcolor=colors['graph_background'],
#                                    yaxis_title='')

#               return fig 
