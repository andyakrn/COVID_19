from App_files.imports import *

status = ['Confirmed', 'Active', 'Recovered', 'Deaths']

map_status_radio_items = dcc.RadioItems(
    id='map_status_radio',
    options=[{'label': i, 'value': i} for i in status],
    value='Confirmed',
    style=radio_item_style)

world_map_by_status = dcc.Graph(id='world_map_by_status')

world_map = html.Figure(
    style=large_viz_container_style,
    children=[map_status_radio_items, world_map_by_status])

def update_world_map(app):
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
                                    title='{} by Country Over Time (Hover for Country Names)'.format(
                                        radio_item),
                                    color_continuous_scale=['green', 'yellow',
                                                            'orange', 'orangered', 'red'],
                                    projection='natural earth',
                                    animation_frame='Date',
                                    range_color=[0, max_cases],
                                    template='plotly_dark',
                                    height=600
                                    )
        world_map_fig.update_layout(font={'family': font['font'], 'color': colors['text']},
                                    paper_bgcolor=colors['graph_background'],
                                    plot_bgcolor=colors['graph_background'],
                                    autosize = True,                                   
                        
                                    
                                    )
        world_map_fig.update_layout(coloraxis_colorbar=dict(xanchor="right", x=.05, xpad=0))
        return world_map_fig
