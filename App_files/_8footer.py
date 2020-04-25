from App_files.imports import *

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