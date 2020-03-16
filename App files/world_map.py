from imports import *

fig = px.choropleth(
    grouped_df, 
    locations=grouped_df['Country/Region'], 
    locationmode='country names', 
    color = grouped_df['Confirmed'],
    hover_name = 'Country/Region',
    title='test title'
    )


world_map4 = dcc.Graph(figure=fig)

world_map3 = dcc.Graph(
    id='Graph3',
    style={
        'margin-right': '5px',
        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
        'width': '100%',
        'padding': '0'
    },
    figure={
        'data': [
           {'type': 'go.Choropleth',
            # 'data_frame': grouped_df,
            'locations': grouped_df['Country/Region'],
            'locationmode': 'country names',

            }
        ],
        'layout': {
            'title': 'Test Title',
            'plot_bgcolor': colors['graph_background'],
            'paper_bgcolor': colors['graph_background'],
            'font':
            {'color': colors['text']}
        },

    }
)
