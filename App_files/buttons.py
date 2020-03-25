from imports import *

brian_button = html.A(html.Button('Brian Kosiadi, BS', style=button_style),
                      href='https://www.linkedin.com/in/brian-kosiadi/')

andrei_button = html.A(html.Button('Andrei Zholud, PhD', style=button_style),
                       href='https://www.linkedin.com/in/andrei-zholud/')

christy_button = html.A(html.Button('Christy Liner, MBA', style=button_style),
                        href='https://www.linkedin.com/in/christy-liner/')

chinwe_button = html.A(html.Button('Chinwe Egwim, BA', style=button_style),
                       href='https://www.linkedin.com/in/chinwe-egwim752/')

all_buttons = html.Figure(style={'display': 'flex',
                                 'flex-direction': 'row',
                                 'justify-content': 'space-between'},
                          children=[brian_button, andrei_button, christy_button, chinwe_button])
#test