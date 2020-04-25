from App_files.imports import *


header1 = html.H1(children='COVID-19 Coronavirus Dashboard',
                  style=header_1_style,
                  )




summary2 = html.P(children=['''
The purpose of this project is to create a dashboard that visualizes the virus' spread across 
the globe. It features an animated map that illustrates the progression of cases over time, 
along with a plot that allows the user to compare the growth rates of cases between two countries. 
View our ''', 
html.A('Github page', href="https://github.com/andyakrn/COVID_19", style={'color': 'red'},
target='_blank'), 
' for data sources and other information.']
,
                  style=summary_style)

headers = html.Div(style={'display': 'flex',
                          'flex-direction': 'column'},
                   children=[header1, summary2])
