from imports import *

app = dash.Dash(__name__, )

app.layout = html.Main(
    style={
        'backgroundColor': colors['body_background'],
        'width': '97%',
        'padding': '10px',
        'display': 'flex',
        'flex-direction': 'column',
    },
    children=[
        headers,
        world_map,
        graph_figures,
<<<<<<< HEAD
        big_graph,
        all_buttons],
=======
        interactive_graph,
        user_input,
        user_output,
        all_buttons,

    ],
>>>>>>> ae40e9b286c1a8351c63b3877fb2ffff4c71803e
)


@app.callback(
    Output('plot_by_country', 'figure'),
    [Input('country_dropdown', 'value'),
     Input('status_radio', 'value')])
def update_figure(selected_country, radio_item):
    filtered_df = grouped_df.loc[grouped_df['Country/Region']
                                 == selected_country]
    melted_df = pd.melt(filtered_df, id_vars='Date', value_vars=[
                        'Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Status')
    fig = px.bar(melted_df.loc[melted_df['Status'] == radio_item],
                 x='Date',
                 y='value',
                 title='Number of {} for {} (Select a different status or country to update)'.format(
        radio_item, selected_country),
        barmode='group',
        template='plotly_dark',
        range_y=[0, int(filtered_df['Confirmed'].max()),
                 ]
    )
    fig.update_layout({'paper_bgcolor': colors['graph_background'],
                       'plot_bgcolor': colors['graph_background'],
                    #    'color': colors['text'],
                       # 'font': {'color': colors['text']
                       })

    return fig


<<<<<<< HEAD
# @app.callback(
#     Output('user-output', 'children'),
#     [Input('age', 'value'),
#      Input('gender', 'value'),
#      Input('pre_cond', 'value')])
# def return_inputs(age, gender, pre_cond):
#     return 'I am a {a} year old {g}, with {h} pre-existing health conditions.'.format(a = age, g = gender, h = pre_cond)
=======
@app.callback(
    Output('user-output', 'children'),
    [Input('age', 'value'),
     Input('gender', 'value'),
     Input('pre_cond', 'value')])
def return_inputs(age, gender, pre_cond):
    return 'I am a {a} year old {g}, with {h} pre-existing health conditions.'.format(a=age, g=gender, h=pre_cond)
>>>>>>> ae40e9b286c1a8351c63b3877fb2ffff4c71803e


if __name__ == '__main__':
    app.run_server(debug=True)
