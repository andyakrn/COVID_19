from imports import *

button_style = {'color': colors['text'],
               'font-size' : '16px',
               'border-radius': '10px',
               'height': '40px',
               'width': '170px',
               'max-width': '200px',
               'background-color': colors['header_background'],
               'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'                                    
                 }
brian_button = html.A(html.Button('Brian Kosiadi, BS', 
                    style=button_style               
                      ),                               
                    href='https://www.linkedin.com/in/brian-kosiadi/')

andrei_button = html.A(html.Button('Andrei Zholud, PhD', 
                    style=button_style
                       ),  
                    href='https://www.linkedin.com/in/andrei-zholud/')
christy_button = html.A(html.Button('Christy Liner, MBA', 
                    style=button_style
                       ),   
                    href='https://www.linkedin.com/in/christy-liner/')
chinwe_button = html.A(html.Button('Chinwe Egwim, BA', 
                     style=button_style
                       ),  
                    href='https://www.linkedin.com/in/chinwe-egwim752/')