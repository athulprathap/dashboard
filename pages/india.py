from operator import imod
from dash import Dash, html, dcc
from pyparsing import White
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash
from dash import html, dcc, callback, Input, Output
from urllib.request import urlopen
import json
import plotly.express as px

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})



fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="world",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

dash.register_page(__name__)

colors = {
    'background': '#FFF4E4',
    'text': '#000000'
}

# define the page content with variable called layout
layout = html.Div(
    style={'backgroundColor': colors['background']}, 
children=[


    dbc.Row([
    html.H1(
        children='Welcome to DashBoard',
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
    html.Div(children='ReelRo Analytics Dashboard', style={
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
    html.Br(),
    html.Br(),
    dbc.Row([
    dbc.Col([dcc.Graph(
        id='sunburst',
        figure=fig,
        style={'marginTop': '0', 'marginBottom': '100', 'marginLeft': '0', 'marginRight': '0', 'paddingTop': '0', 'paddingBottom': '0', 'paddingLeft': '0', 'paddingRight': '0'}
        
    )
    ])
    ]),

    html.Br(),
    html.Br(),
    

    dbc.Row([
        dbc.Col([
             html.H1(
        children='World Map',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontSize': '3.5rem',
            'Bottom': '100'
            
            }
                )   
        ])
    ])
])

