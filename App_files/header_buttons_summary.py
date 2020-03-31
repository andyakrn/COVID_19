from imports import *

brian_button = html.A(html.Button('Brian Kosiadi, BS', style=button_style),
                      href='https://www.linkedin.com/in/brian-kosiadi/',
                      target='_blank',
                      title='Linked In - Brian Kosiadi')

andrei_button = html.A(html.Button('Andrei Zholud, PhD', style=button_style),
                       href='https://www.linkedin.com/in/andrei-zholud/',
                       target='_blank',
                       title='Linked In - Andrei Zholud')

christy_button = html.A(html.Button('Christy Liner, MBA', style=button_style),
                        href='https://www.linkedin.com/in/christy-liner/',
                        target='_blank',
                        title='Linked In - Christy Liner')

chinwe_button = html.A(html.Button('Chinwe Egwim, BA',
                                   style=button_style,
                                   ),
                       href='https://www.linkedin.com/in/chinwe-egwim752/',
                       target='_blank',
                       title='Linked In - Chinwe Egwim')

all_buttons = html.Figure(style={'display': 'flex',
                                 'flex-direction': 'row',
                                 'justify-content': 'space-between'},
                          children=[brian_button, andrei_button, christy_button, chinwe_button])

header1 = html.H1(children='COVID-19 Coronavirus Dashboard',
                  style=header_1_style,
                  )

summary_link = html.A('(Source)',
                      href='https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic',
                      target='_blank')

summary1 = html.P(children=['''
On March 11, 2019, The World Health Organization (WHO) recognized COVID-19 as a pandemic. 
The coronavirus disease 2019 (COVID-19) is a respiratory illness caused by severe acute respiratory 
syndrome coronavirus 2 (SARS-CoV-2). Since the first outbreak in December 2019 in Wuhan, China, 
more than 494,000 cases have been reported in over 190 countries and territories.
''', summary_link],

                  style=summary_style)


summary2 = html.P(children='''
The purpose of this project is to create a dashboard that visualizes the virus' spread across 
the globe. It features an animated map that illustrates the progression of cases over time, 
along with a plot that allows the user to compare the growth rates of cases between two countries. 
There is also a bar plot showing the amount of cases for the top 10 countries.
''',
                  style=summary_style)

headers = html.Div(style={'display': 'flex',
                          'flex-direction': 'column'},
                   children=[header1, all_buttons, summary1, summary2])

prediction = html.P(children='*Enter in age and gender to view mortality rate of those that tested positive for COVID-19.',
                    style=prediction_style)

prediction_container = html.Div(style={'display': 'flex',
                                       'flex-direction': 'column'},
                                children=[prediction])

disclaimer = html.P(children='*This does not take into consideration those that contracted COVID-19 but were not tested. This website does not provide medical advice and is for informational purposes only. Please seek medical advice from a health care professional for any questions.',
                    style=prediction_style)

disclainer_container = html.Div(style={'display': 'flex',
                                       'flex-direction': 'column'},
                                children=[disclaimer])
