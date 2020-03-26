from imports import *


header1 = html.H1(children='COVID-19 Coronavirus Dashboard',
                  style=header_1_style)

header2 = html.H4(children='Brian Kosiadi, BS | Andrei Zholud PhD | Christy Liner MBA | Chinwe Egwim, BA',
                  style=header_2_style)

summary1 = html.P(children='Coronaviruses are a large family of viruses that are common in people and many different species of animals, including camels, cattle, cats, and bats. Rarely, animal coronaviruses can infect people and then spread between people such as with MERS-CoV, SARS-CoV, and now with this new virus (named SARS-CoV-2).',
                  style=summary_style)

summary2 = html.P(children='The SARS-CoV-2 virus is a betacoronavirus, like MERS-CoV and SARS-CoV.  All three of these viruses have their origins in bats. The sequences from U.S. patients are similar to the one that China initially posted, suggesting a likely single, recent emergence of this virus from an animal reservoir. (Source: CDC)',
                  style=summary_style)

headers = html.Div(style={'display': 'flex',
                          'flex-direction': 'column'},
                   children=[header1, header2, summary1, summary2])

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
#test