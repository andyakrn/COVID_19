
grouped_df['Change in New Weekly Cases'] = np.where(grouped_df['Country/Region']==grouped_df['Country/Region'].shift(1), (grouped_df['New Weekly Cases'] - grouped_df['New Weekly Cases'].shift(1)), grouped_df['New Weekly Cases'])

grouped_df['new_cases'] = grouped_df['Confirmed'] - grouped_df['Confirmed'].shift(1)
us_df = grouped_df.loc[grouped_df['Country/Region']=='United States'].reset_index()

us_df.drop(0, inplace = True)

us_df['week_number'] = us_df['Datetime'].dt.week

us_df = us_df.groupby('week_number').agg('sum')

us_df['new_case_growth_rate_from_previous_week'] = ((us_df['new_cases'] - us_df['new_cases'].shift(1)) / us_df['new_cases'].shift(1))

px.line(us_df, x=us_df.index, y='new_case_growth_rate_from_previous_week')px.line(us_df, x=us_df.index, y='new_case_growth_rate_from_previous_week')px.line(us_df, x=us_df.index, y='new_case_growth_rate_from_previous_week')px.line(us_df, x=us_df.index, y='new_case_growth_rate_from_previous_week')