from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(
    style=main_app_style,
    children=[
        headers,
        world_map,
        interactive_graph,
        graphs4_5,
        prediction_container,
        user_input,
        user_output,
        graph_figures,
        all_buttons,
        disclainer_container])

@app.callback(
    Output('world_map_by_status', 'figure'),
    [Input('map_status_radio', 'value')])
def update_figure(radio_item):
    max_cases = grouped_df[radio_item].max()
    melt_df = pd.melt(grouped_df, id_vars=['Date', 'Country/Region'], value_vars=[
        'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
    melted_df = melt_df.loc[melt_df['Status'] == radio_item]
    fig = px.choropleth(melted_df,
                        locations='Country/Region',
                        locationmode='country names',
                        color='value',
                        hover_name='Country/Region',
                        title='{} by Country Over Time (Year 2020) <br>(Hover for Country Names)'.format(
                            radio_item),
                        color_continuous_scale=['green', 'yellow',
                                                'orange', 'orangered', 'red'],
                        projection='natural earth',
                        animation_frame='Date',
                        range_color=[0, max_cases],
                        template='plotly_dark')
    fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                      paper_bgcolor=colors['graph_background'],
                      plot_bgcolor=colors['graph_background'])
    return fig

@app.callback(
    Output('plot_by_country', 'figure'),
    [Input('country_dropdown', 'value'),
     Input('type_of_cases_radio', 'value')])
def update_graph(selected_country, type_of_cases):
    filtered_df = grouped_df.loc[grouped_df['Country/Region']
                                 == selected_country]
    melted_df = pd.melt(filtered_df, id_vars=['Date', 'PopTotal'], value_vars=[
                        'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
    if type_of_cases=='Total':
        y= 'value'
    else:
        melted_df['Per Capita'] = melted_df['value' ]/ melted_df['PopTotal']
        y = 'Per Capita'
    fig = px.line(melted_df,
                  x='Date',
                  y=y,
                  title='Cases in {} (Select a different country to update)'.format(
                      selected_country),
                  template='plotly_dark',
                  color='Status',
                  color_discrete_map={'Recovered': 'Green',
                                      'Confirmed': 'Yellow',
                                      'Active': 'Orange',
                                      'Deaths': 'Red'})
    fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                      paper_bgcolor=colors['graph_background'],
                      plot_bgcolor=colors['graph_background'],
                      yaxis_title= 'Total Cases')
    return fig

@app.callback(
    Output('global_plot', 'figure'),
    [Input('type_of_cases_radio', 'value')])
def update_graph(type_of_cases):
    filtered_df = grouped_df.loc[grouped_df['Country/Region']!='Cruise Ship']
    filtered_df = filtered_df.loc[filtered_df['PopTotal']>10000]
    filtered_df=filtered_df.groupby('Country/Region').agg('max')
    if type_of_cases == 'Total':
        df = filtered_df.sort_values('Confirmed', ascending=False).iloc[:20]
        df.sort_values('Confirmed', inplace = True)
        x=df['Confirmed']
        y=df.index
    else: 
        df = filtered_df.sort_values('Confirmed Cases Per 1M', ascending=False).iloc[:20]
        df.sort_values('Confirmed Cases Per 1M', inplace = True)
        x=df['Confirmed Cases Per 1M']
        y=df.index
    fig = px.scatter(data_frame = df,
                  x=x,
                  y=y,
                  title='Countriese with Highest Confirmed Cases',
                  template='plotly_dark')
    fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                      paper_bgcolor=colors['graph_background'],
                      plot_bgcolor=colors['graph_background'],
                      yaxis_title= '')
    
    return fig


@app.callback(
    Output('user-output', 'children'),
    [Input('age', 'value'),
     Input('gender', 'value')])
def return_inputs(age, gender):
    return ''
    # plug into trained model and output the prediction
    # return 'I am a {a} year old {g}.'.format(a=age, g=gender)


if __name__ == '__main__':
    app.run_server(debug=True)
