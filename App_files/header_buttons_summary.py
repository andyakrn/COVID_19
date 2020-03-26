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
                  style=header_1_style)

summary_link = html.A('(Source).',
                      href='https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic',
                      target='_blank')

summary1 = html.P(children=['''
The 2019–20 coronavirus pandemic is an ongoing pandemic of coronavirus disease 2019 (COVID-19), 
caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The outbreak was first 
identified in Wuhan, Hubei, China, in December 2019, and was recognized as a pandemic by the 
World Health Organization (WHO) on 11 March 2020 
''', summary_link],

                  style=summary_style)


summary2 = html.P(children='''
The purpose of this dashboard is a visualization of the dynamics of the virus spreading around the world. 
The map can show the distribution of case by country at s selected date, as well as number of active, 
recovered and deceased cases. The plot below the map shows number of case for selected country vs time.  
Also, this plot allows comparing the dynamics of the spread between two selected countries. 
Bar plot shows the top 10 countries with the highest number of cases on the current date.  
A simple model (will be implemented later when more data become available) predicts a probability 
of survival. 
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
