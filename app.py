import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#load in data file
DATA_PATH = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH + '/df_patient.pickle', 'rb')
df_patient = pickle.load(pickle_in)
    
colors = {
    'body_background': '#181A1C',
    'header_background': '#232629',
    'text': '#d6d9dc',
    'graph_background': '#181A1C',
    'page_background': '#181A1C',
    'bar_color': '#b30000',
}
app.layout = html.Main(
        style={
            'backgroundColor': colors['body_background'],
            'padding': '10px'
              },
        children=[
            html.Div(
                style={
                    'backgroundColor': colors['body_background'],
                      }
                    ),  

            

            html.H1(
                children='COVID-19 Coronavirus',
                style={
                    'backgroundColor': colors['header_background'],
                    'textAlign': 'center',
                    'color': colors['text'],
                    'font-family': 'Verdana',
                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                    'margin-top': '10px'
                      }  
                    ),
            html.Div(
                children='Coronaviruses are a large family of viruses that are common in people and many different species of animals, including camels, cattle, cats, and bats. Rarely, animal coronaviruses can infect people and then spread between people such as with MERS-CoV, SARS-CoV, and now with this new virus (named SARS-CoV-2).', 
                style={
                    'textAlign': 'left',
                    'backgroundColor': colors['header_background'],
                    'color': colors['text'],
                    'font-family': 'Verdana',
                    'font-size': '14px',
                    'margin': 'auto',
                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                    'margin-bottom': '10px'
        
                      }
                    ),
            html.Div(
                children='The SARS-CoV-2 virus is a betacoronavirus, like MERS-CoV and SARS-CoV.  All three of these viruses have their origins in bats. The sequences from U.S. patients are similar to the one that China initially posted, suggesting a likely single, recent emergence of this virus from an animal reservoir. (Source: CDC)', 
                style={
                    'textAlign': 'left',
                    'backgroundColor': colors['header_background'],
                    'color': colors['text'],
                    'font-family': 'Verdana',
                    'font-size': '14px',
                    'margin': 'auto',
                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                    'margin-bottom': '10px'
        
                      }
                    ),
            dcc.Graph(
                id='Graph1',
                style={
                    'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)'
                      },
                figure={
                    'data': [
                                {'x': df_patient['region'], 
                                 'y': df_patient['age'], 
                                 'type': 'bar'
                                },
                            ],
                    'layout': {
                                'plot_bgcolor': colors['graph_background'],
                                'paper_bgcolor': colors['page_background'],
                                'font': 
                                        {'color': colors['text']
                                        }
                              }
                        }
                      ),

            html.A(html.Button('Brian Kosiadi', 
                               
                                style={'color': colors['text'],
                                       'font-size' : '8px',
                                       'background-color': colors['header_background'],
                                       'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'                                    
                                       }),                               
                    href='https://www.linkedin.com/in/brian-kosiadi/'),
            
            html.A(html.Button('Andrei Zholud, Ph.D.', 
                                
                                style={'color': colors['text'],
                                       'font-size' : '8px',
                                       'background-color': colors['header_background'],
                                       'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'
                                        }),  
                    href='https://www.linkedin.com/in/andrei-zholud/'),
            html.A(html.Button('Christy Liner, MBA', 
                                style={'color': colors['text'],
                                       'font-size' : '8px',
                                       'background-color': colors['header_background'],
                                       'box-shadow':'0 8px 16px 0 rgba(0,0,0,2), 0 6px 20px 0 rgba(0,0,0,0.19)'
                                        }),  
                    href='https://www.linkedin.com/in/christy-liner/'),

            html.Footer(
                children='Brian Kosiadi | Andrei Zholud Ph.D. | Christy Liner MBA', 
                style={
                        'textAlign': 'center',
                        'color': colors['text'],
                        'backgroundColor': colors['header_background'],
                        'font-family': 'Verdana',
                        'box-shadow': '0 1px 3px 0 rgba(0, 0, 0, 2)',
                        'margin-top': '20px',
                        'margin-bottom': '0'
         
                      }),
                 ]
            )


if __name__ == '__main__':
    app.run_server(debug=True)