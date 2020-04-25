from App_files.imports import *

death_types = ['Observed case-fatality ratio', 'Deaths per 1M population']

death_radio_items = dcc.RadioItems(
    id='death_radio_items',
    options=[{'label': i, 'value': i} for i in death_types],
    value='Observed case-fatality ratio',
    style=radio_item_style
)

mortality_graph = dcc.Graph(id='mortality_graph',
                            style={'height': '95%'})

mortality_figure = html.Figure(children=[death_radio_items, mortality_graph],
                               style={'width': '50%',
                                               'margin': '0px',
                                               'margin-bottom': '0px',
                                               'border': '.5pt solid #a6a6a6',
                                               'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',

                                               'color': colors['text'],
                                      'backgroundcolor': colors['header_background'],
                                      'font-family': font['font']})


def mortality_graph(app):
    @app.callback(
        Output('mortality_graph', 'figure'),
        [Input('death_radio_items', 'value')])
    def new_cases_by_state(death_type):
        deaths_df = grouped_df.groupby(
            'Country/Region').agg('max').sort_values('Deaths', ascending=False).head(10)
        deaths_df['Observed case-fatality ratio'] = (
            deaths_df['Deaths'] / deaths_df['Confirmed']).round(2)
        deaths_df = deaths_df.sort_values('Observed case-fatality ratio')
        if death_type == 'Observed case-fatality ratio':
            fig = px.bar(deaths_df, y=deaths_df.index, x='Observed case-fatality ratio', orientation='h',
                         text='Observed case-fatality ratio', color_discrete_sequence=['red'], template='plotly_dark')
        elif death_type == 'Deaths per 1M population':
            deaths_df['Deaths per 100,000 population'] = (
                deaths_df['Deaths'] * 1000 / (deaths_df['PopTotal'])).round(2)
            deaths_df = deaths_df.sort_values('Deaths per 100,000 population')
            fig = px.bar(deaths_df, y=deaths_df.index, x='Deaths per 100,000 population', orientation='h',
                         text='Deaths per 100,000 population', color_discrete_sequence=['red'], template='plotly_dark')
        fig.update_layout(yaxis_title='', paper_bgcolor=colors['graph_background'],
                          plot_bgcolor=colors['graph_background'], title='Mortality', font={'family': font['font'], 'color': colors['text']})

        return fig
