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
        graph_figures,
        user_input,
        user_output,
        all_buttons])


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
                        color=melted_df['value'],
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
     Input('status_radio', 'value')])
def update_figure(selected_country, radio_item):
    filtered_df = grouped_df.loc[grouped_df['Country/Region']
                                 == selected_country]
    melted_df = pd.melt(filtered_df, id_vars='Date', value_vars=[
                        'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
    fig = px.scatter(melted_df.loc[melted_df['Status'] == radio_item],
                     x='Date',
                     y='value',
                     title='Number of {} for {} (Select a different status or country to update)'.format(
                     radio_item, selected_country),
                     template='plotly_dark',
                     #  range_y=[0, int(filtered_df['Confirmed'].max())],
                     #  range_y=[0, 90000]
                     )
    fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                      paper_bgcolor=colors['graph_background'],
                      plot_bgcolor=colors['graph_background'])
    return fig


@app.callback(
    Output('user-output', 'children'),
    [Input('age', 'value'),
     Input('gender', 'value'),
     Input('pre_cond', 'value')])
def return_inputs(age, gender, pre_cond):
    return 'I am a {a} year old {g}, with {h} pre-existing health conditions.'.format(a=age, g=gender, h=pre_cond)


if __name__ == '__main__':
    app.run_server(debug=True)
