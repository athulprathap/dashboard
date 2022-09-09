import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path='/')

colors = {
    'background': '#FFF4E4',
    'text': '#000000'
}
"""
layout = html.Div(
    style={'backgroundColor': colors['background']}, 
children=[


    dbc.Row([
    html.H1(
        children='Welcome to Homepage',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontSize': '3.5rem',
            'fontWeight': 'bold',
            'marginTop': '50',
            'marginBottom': '0',
            'marginLeft': '0',
            'marginRight': '0',
            'paddingTop': '50',
            'paddingBottom': '0',
            'paddingLeft': '0',
            'paddingRight': '0',
            'backgroundColor': colors['background'],
            'borderBottom': '1px solid #FFF4E4',
            'borderTop': '1px solid #FFF4E4',
            'borderLeft': '1px solid #FFF4E4',
            'borderRight': '1px solid #FFF4E4',
            'borderRadius': '0',
            'boxShadow': '2px 2px 2px 2px #000000',
        }
    )
    ]),
    
    dbc.Row([
    html.Div(children='Analytics App', style={
        'textAlign': 'center',
        'color': colors['text'],
        'fontSize': '1.5rem',
        'fontWeight': 'bold',
        'marginTop': '0',
        'marginBottom': '0',
        'marginLeft': '0',
        'marginRight': '0',
        'paddingTop': '0',
        'paddingBottom': '0',
        'paddingLeft': '0',
        'paddingRight': '0',
        'backgroundColor': colors['background'],
        'borderBottom': '1px solid #FFF4E4',
        'borderTop': '1px solid #FFF4E4'

    })
    ]),
    html.H1(children='This is our Analytics page'),
    html.Div([
        "Select a page: ",
        dcc.RadioItems(['india', 'sunburst','india_ads','ads'],
            'sunburst',
        id='analytics-input',
        # add space between the radio items
        style={'display': 'inline-block', 'margin': '0 20px'})
    ]),
    html.Br(),
    html.Div(id='analytics-output'),
]
)

"""
layout = html.Div([

    dbc.Container(
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H2("Reelro", className="display-4"),
                        html.P(
                            "ReelRo Dashboard"
                            "This Dashboard is created to analyse the data of ReelRo",
                            className="lead",
                        ),
                    ],
                    className="p-5 bg-light",
                )
            ),
            className="mt-4",
        )
    ),


])