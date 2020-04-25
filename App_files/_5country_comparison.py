from App_files.imports import *

types_of_cases1 = ['Confirmed', 'Active', 'Recovered', 'Deaths']

type_of_cases_radio_items1 = dcc.RadioItems(id='type_of_cases_radio1',
                                            options=[{'label': i, 'value': i}
                                                     for i in types_of_cases1],
                                            value='Confirmed',
                                            style=radio_item_style)

hardest_hit_countries = list(grouped_df.groupby(
    'Country/Region').agg('max')['Confirmed'].sort_values(ascending=False)[0:3].index)

countries = grouped_df['Country/Region'].unique()

country_choices = dcc.Dropdown(id='country_dropdown1',
                               options=[{'label': i, 'value': i}
                                        for i in countries],
                               value=hardest_hit_countries,
                               placeholder='Select Countries',
                               style={'font-family': font['font']},
                               multi=True)

country_comparison_graph = dcc.Graph(id='country_comparison_graph')

country_comparison_figure = html.Figure(style=large_viz_container_style,
                                        children=[type_of_cases_radio_items1, country_choices, country_comparison_graph])

types_of_cases1 = ['Confirmed', 'Active', 'Recovered', 'Deaths']

type_of_cases_radio_items1 = dcc.RadioItems(id='type_of_cases_radio1',
                                            options=[{'label': i, 'value': i}
                                                     for i in types_of_cases1],
                                            value='Confirmed',
                                            style=radio_item_style)

hardest_hit_countries = list(grouped_df.groupby(
    'Country/Region').agg('max')['Confirmed'].sort_values(ascending=False)[0:3].index)

country_choices = dcc.Dropdown(id='country_dropdown1',
                               options=[{'label': i, 'value': i}
                                        for i in countries],
                               value=hardest_hit_countries,
                               placeholder='Select Countries',
                               style={'font-family': font['font'],
                                      },
                               multi=True)


type_of_cases = ['Total', 'Cases Per 1M']

type_of_cases_radio_items = dcc.RadioItems(id='type_of_cases_radio',
                                           options=[{'label': i, 'value': i}
                                                    for i in type_of_cases],
                                           value='Total',
                                           style=radio_item_style)

radio_and_dropdown = html.Figure(style=interactive_graph_style,
                                 children=[type_of_cases_radio_items])


country_comparison_graph = dcc.Graph(id='country_comparison_graph')

country_comparison_figure = html.Figure(style={'width': '50%',
                                               'margin': '0px',
                                               'margin-bottom': '0px',
                                               'border': '.5pt solid #a6a6a6',
                                               'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                                               'height': '100%'
                                               },
                                        children=[type_of_cases_radio_items1,
                                                  country_choices,
                                                  radio_and_dropdown,
                                                  country_comparison_graph])

# additional_graph = dcc.Graph(style={'border': '.5pt solid #a6a6a6',
#                                     'width': '50%'})

large_figure = html.Figure(children=[country_comparison_figure,
                                     mortality_figure],
                           style={'display': 'flex',
                                  'flex-direction': 'row',
                                  'margin-left': '0px',
                                  'margin-right': '0px'})


def status_comparison_graph(app):
    @app.callback(
        Output('country_comparison_graph', 'figure'),
        [Input('type_of_cases_radio1', 'value'),
         Input('country_dropdown1', 'value'),
         Input('type_of_cases_radio', 'value')])
    def update_country_comparison(status, selected_countries, type_of_cases):
        filtered_df = pd.DataFrame()
        for country in selected_countries:
            filtered_df = filtered_df.append(
                grouped_df.loc[grouped_df['Country/Region'] == country])
        melted_df = pd.melt(filtered_df, id_vars=['Date', 'Country/Region', 'PopTotal'], value_vars=[
                            'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
        melted_df = melted_df.loc[melted_df['Status'] == status]
        date = pd.to_datetime(grouped_df['Date']).dt.date.sort_values(
            ascending=False).reset_index(drop=True)[0].strftime('%m/%d/%Y')
        if type_of_cases == 'Total':
            y = 'value'
        else:
            melted_df['Per Capita'] = melted_df['value'] / \
                melted_df['PopTotal']
            y = 'Per Capita'
        fig = px.line(melted_df,
                      x='Date',
                      y=y,
                      title='Cases through {}. Choose different countries for comparison.'.format(
                          date),
                      template='plotly_dark',
                      color='Country/Region',
                      height=400
                      )
        fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                          paper_bgcolor=colors['graph_background'],
                          plot_bgcolor=colors['graph_background'],
                          yaxis_title='Total Cases')
        fig.update_xaxes(tickangle=45, dtick=7)
        return fig
