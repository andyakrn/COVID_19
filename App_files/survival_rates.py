from imports import *

country_df = grouped_df.groupby('Country/Region').agg('sum')
country_df = country_df.sort_values('Confirmed', ascending = False)[:10]
country_df['Best Case'] = 1- (country_df['Deaths'] / country_df['Confirmed'])
country_df['Worst Case'] = 1 - (country_df['Deaths'] / (country_df['Recovered'] + country_df['Deaths']))

survival_df = pd.melt(country_df.reset_index(), 
                      id_vars = 'Country/Region', 
                      value_vars = ['Best Case', 'Worst Case'], 
                      value_name = 'Survival_Rate',
                      var_name = 'Scenario')

survival_fig = px.bar(survival_df,
                        x='Country/Region',
                        y='Survival_Rate',
                        barmode='group',
                        template='plotly_dark',
                        color='Scenario',
                        color_discrete_sequence = ['green', 'red'], 
                        title='Best and Worst Case Survival Rates for Tested Individuals')

survival_fig.update_layout(font={'family': font['font'],
                                   'color': colors['text']},
                             paper_bgcolor=colors['graph_background'],
                             plot_bgcolor=colors['graph_background'],
                             yaxis_title='New Cases')

survival_fig1 = dcc.Graph(id='survival_rates',
                              style=large_viz_style,
                              figure=survival_fig)

survival_figure = html.Figure(
    style=large_viz_container_style,
    children=survival_fig1)

# new_cases_figure = html.Figure(style=large_viz_container_style,
#                                children=[new_cases_figures])