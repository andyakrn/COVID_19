
import dash
import dash_core_components as dcc
import dash_html_components as html
from colors import colors

brian_button = html.A(html.Button('Brian Kosiadi', 
                    style={'color': colors['text'],
                           'font-size' : '8px',
                           'background-color': colors['header_background'],
                           'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'                                    
                           }),                               
                    href='https://www.linkedin.com/in/brian-kosiadi/')

andrei_button = html.A(html.Button('Andrei Zholud, Ph.D.', 
                    style={'color': colors['text'],
                           'font-size' : '8px',
                           'background-color': colors['header_background'],
                           'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'
                           }),  
                    href='https://www.linkedin.com/in/andrei-zholud/')
christy_button = html.A(html.Button('Christy Liner, MBA', 
                    style={'color': colors['text'],
                           'font-size' : '8px',
                           'background-color': colors['header_background'],
                           'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'
                          }),  
                    href='https://www.linkedin.com/in/christy-liner/')
chinwe_button = html.A(html.Button('Chinwe Egwim, BA', 
                                style={'color': colors['text'],
                                       'font-size' : '8px',
                                       'background-color': colors['header_background'],
                                       'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'
                                        }),  
                    href='https://www.linkedin.com/in/chinwe-egwim752/')