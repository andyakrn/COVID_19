from imports import *

country_dropdown2 = dcc.Dropdown(id='country_dropdown2',
                                 options=[{'label': i, 'value': i}
                                          for i in countries],
                                 value='United States',
                                 placeholder='Select a Country',
                                 style={'font-family': font['font']})

hardest_hit_countries = list(grouped_df.groupby('Country/Region').agg('max')['Confirmed'].sort_values(ascending=False)[0:7].index)

new_log_cases = grouped_df.loc[grouped_df['Country/Region'].isin(hardest_hit_countries)]

new_cases_fig1 = px.line(new_log_cases,
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

new_cases_fig1.update_xaxes(range=[1,6])
new_cases_fig1.update_yaxes(range=[1,6])
new_cases_fig1.update_yaxes(tickvals=[10, 100, 1000, 10000, 100000, 1000000])

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

def new_cases(app):
    @app.callback(
    Output('new_graph2', 'figure'),
    [Input('country_dropdown2', 'value')])
    def new_cases_by_country(country):
        country_df = grouped_df.loc[grouped_df['Country/Region']==country]
        country_df['Yesterday_Cases'] = country_df['Confirmed'].shift(1)
        country_df['New_Cases'] = country_df['Confirmed'] - country_df['Yesterday_Cases']
        fig = px.bar(country_df,
                            x='Date',
                            y='New_Cases',
                            template='plotly_dark',
                            title='New Cases by Day in {}'.format(country),
                            color_discrete_sequence = ['red'])
        fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                        paper_bgcolor=colors['graph_background'],
                        plot_bgcolor=colors['graph_background'])
        fig.update_xaxes(tickangle=45, dtick=7)
        return fig