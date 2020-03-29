from imports import *

app = dash.Dash(__name__, )

app.title = 'COVID-19 Visualization Dashboard'

server = app.server

app.layout = html.Main(

    style=main_app_style,
    children=[
        html.Img(src='data:image/jpeg;base64,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'),
        headers,
        world_map,
        graph_figures,
        interactive_graph,
        graphs4_5,
        country_comparison_figure,
        prediction_container,
        user_input,
        user_output,
        disclainer_container])

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
                                  title='{} by Country Over Time (Year 2020) <br>(Hover for Country Names)'.format(
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


@app.callback(
    Output('user-output', 'children'),
    [Input('submit-button', 'n_clicks')],
     [State('age', 'value'),
     State('gender', 'value')])
def return_inputs(n_clicks, age, gender):
    if n_clicks==0:
        return 'RESULT: Enter age and gender for likelihood of survival.'
    if n_clicks>0:
        if age == None or gender == None:
            return 'RESULT: Enter age and gender for likelihood of survival.'
        elif age != None and gender != None:
            if gender=='Female':
                gender_numeric=0
            else:
                gender_numeric=1
            prediction = rfc_model.predict([[age, gender_numeric]])
            if prediction == 1: 
                prognosis = 'Survival is likely.'
            else: 
                prognosis = 'Severe complications are likely.'
            return 'RESULT: Prognosis for a {} year old {}: {}'.format(age, gender, prognosis)

if __name__ == '__main__':
    app.run_server(debug=True)
