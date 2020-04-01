from imports import *

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
                  template='plotly_dark').update_layout(font={'family': font['font'], 'color': colors['text']},
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
        
def updated_country_confirmed_million(app):
    @app.callback(
        Output('plot_by_country', 'figure'),
        [Input('country_dropdown', 'value'),
        Input('type_of_cases_radio', 'value')])
    def update_graph(selected_country, type_of_cases):
        filtered_df = grouped_df.loc[grouped_df['Country/Region']
                                    == selected_country]
        melted_df = pd.melt(filtered_df, id_vars=['Date', 'PopTotal'], value_vars=[
                            'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
        date = pd.to_datetime(grouped_df['Date']).dt.date.sort_values(
            ascending=False).reset_index(drop=True)[0].strftime('%m/%d/%Y')

        if type_of_cases == 'Total':
            y = 'value'
        else:
            melted_df['Per Capita'] = melted_df['value'] / melted_df['PopTotal']
            y = 'Per Capita'
        fig = px.line(melted_df,
                    x='Date',
                    y=y,
                    title='Cases in {} through {}'.format(
                        selected_country, date),
                    template='plotly_dark',
                    color='Status',
                    color_discrete_map={'Recovered': 'Green',
                                        'Confirmed': 'Yellow',
                                        'Active': 'Orange',
                                        'Deaths': 'Red'},
                    height=350)
        fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                        paper_bgcolor=colors['graph_background'],
                        plot_bgcolor=colors['graph_background'],
                        yaxis_title='Total Cases')
        fig.update_xaxes(tickangle=45)
        return fig

def update_countries_highest_confirmed_cases(app):
    @app.callback(
    Output('global_plot', 'figure'),
    [Input('type_of_cases_radio', 'value')])
    def update_graph(type_of_cases):
        filtered_df = grouped_df.loc[grouped_df['Country/Region'] != 'Cruise Ship']
        filtered_df = filtered_df.loc[filtered_df['PopTotal'] > 10000]
        filtered_df = filtered_df.groupby('Country/Region').agg('max')
        if type_of_cases == 'Total':
            df = filtered_df.sort_values('Confirmed', ascending=False).iloc[:8]
            df.sort_values('Confirmed', inplace=True)
            x = df['Confirmed']
            y = df.index
        else:
            df = filtered_df.sort_values(
                'Confirmed Cases Per 1M', ascending=False).iloc[:8]
            df.sort_values('Confirmed Cases Per 1M', inplace=True)
            x = df['Confirmed Cases Per 1M']
            y = df.index
        fig = px.bar(data_frame=df,
                    x=x,
                    y=y,
                    title='Countries with Highest Confirmed Cases',
                    template='plotly_dark',
                    orientation='h',
                    height=350)
        fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                        paper_bgcolor=colors['graph_background'],
                        plot_bgcolor=colors['graph_background'],
                        yaxis_title='')

        return fig

