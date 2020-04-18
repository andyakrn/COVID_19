from imports import *
us_df['Total Tests Performed'] = us_df['totalTestResults']
status = ['Confirmed', 'Deaths', 'Total Tests Performed']

us_map_status_radio_items = dcc.RadioItems(
    id='us_map_status_radio',
    options=[{'label': i, 'value': i} for i in status],
    value='Confirmed',
    style=radio_item_style)

us_map_by_status = dcc.Graph(id='us_map_by_status')

us_map = html.Figure(
    style=large_viz_container_style,
    children=[us_map_status_radio_items, us_map_by_status])


def update_us_map(app):
    @app.callback(
        Output('us_map_by_status', 'figure'),
        [Input('us_map_status_radio', 'value')])
    def update_us_figure(radio_item):
        max_cases = us_df[radio_item].max()
        # us_df.sort_values(by='Date',inplace=True)

        us_map_fig = px.choropleth(us_df,
                                    locations='State_code',
                                    locationmode='USA-states',
                                    scope='usa',
                                    color=radio_item,
                                    hover_name='State',
                                    title='{} by Country Over Time (Hover for Country Names)'.format(
                                        radio_item),
                                    color_continuous_scale=['green', 'yellow','orange', 'orangered', 'red'],
                                    animation_frame='Date',
                                    range_color=[0, max_cases],
                                    template='plotly_dark',
                                    height=600,
                                    )
        us_map_fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                                 paper_bgcolor=colors['graph_background'],
                                 plot_bgcolor=colors['graph_background']

                                 )
        us_map_fig.update_layout(coloraxis_colorbar=dict(xanchor="right", x=.05, xpad=0),
                                 )
        return us_map_fig
