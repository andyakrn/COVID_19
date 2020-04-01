from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(

    style=main_app_style,
    children=[
        headers,
        world_map,
        graph_figures,
        interactive_graph,
        graphs4_5,
        country_comparison_figure,
        new_cases_figure,

    ])

@app.callback(
    Output('world_map_by_status', 'figure'),
    [Input('map_status_radio', 'value')])
def update_figure(radio_item):
    max_cases = grouped_df[radio_item].max()
    status_melt_df = pd.melt(grouped_df,
                             id_vars=['Date', 'Country/Region'],
                             value_vars=['Confirmed',
                                         'Recovered', 'Deaths', 'Active'],
                             var_name='Status')
    melted_df = status_melt_df.loc[status_melt_df['Status'] == radio_item]

    world_map_fig = px.choropleth(melted_df,
                                  locations='Country/Region',
                                  locationmode='country names',
                                  color='value',
                                  hover_name='Country/Region',
                                  title='{} by Country Over Time<br>(Hover for Country Names)'.format(
                                      radio_item),
                                  color_continuous_scale=['green', 'yellow',
                                                          'orange', 'orangered', 'red'],
                                  projection='natural earth',
                                  animation_frame='Date',
                                  range_color=[0, max_cases],
                                  template='plotly_dark',
                                  height=600)
    world_map_fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                                paper_bgcolor=colors['graph_background'],
                                plot_bgcolor=colors['graph_background'])
    return world_map_fig


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


@app.callback(
    Output('country_comparison_graph', 'figure'),
    [Input('type_of_cases_radio1', 'value'),
     Input('country_dropdown1', 'value')])
def update_country_comparison(status, selected_countries):
    filtered_df = pd.DataFrame()
    for country in selected_countries:
        filtered_df = filtered_df.append(
            grouped_df.loc[grouped_df['Country/Region'] == country])
    melted_df = pd.melt(filtered_df, id_vars=['Date', 'Country/Region'], value_vars=[
                        'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
    melted_df = melted_df.loc[melted_df['Status'] == status]
    date = pd.to_datetime(grouped_df['Date']).dt.date.sort_values(
        ascending=False).reset_index(drop=True)[0].strftime('%m/%d/%Y')
    fig = px.line(melted_df,
                  x='Date',
                  y='value',
                  title='Cases through {}. Choose different countries for comparison.'.format(date),
                  template='plotly_dark',
                  color='Country/Region',
                  height=400
                  )
    fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                      paper_bgcolor=colors['graph_background'],
                      plot_bgcolor=colors['graph_background'],
                      yaxis_title='Total Cases')
    fig.update_xaxes(tickangle=45)
    return fig

new_cases(app)

if __name__ == '__main__':
    app.run_server(debug=True)
