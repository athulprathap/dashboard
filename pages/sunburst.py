from dash import Dash, html, dcc
from pyparsing import White
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash
dash.register_page(__name__)

#external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

colors = {
    'background': '#FFF4E4',
    'text': '#000000'
}

data = pd.read_csv("dashboard/Data/ReelRo_Data.csv")
fig = px.sunburst(data, path=['Category', 'Gender', 'Language'], values='Time most users are viewing',
    color_discrete_sequence=px.colors.qualitative.Set3,)
                  
fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))

figure = px.sunburst(data, path=['Location', 'Age_Group', 'Gender'], values='Time most users are viewing',color_discrete_sequence=px.colors.qualitative.T10)
figure.update_layout(margin=dict(t=10, b=10, r=10, l=10))

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
figure.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


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
        style={'marginTop': '0', 'marginBottom': '0', 'marginLeft': '0', 'marginRight': '0', 'paddingTop': '0', 'paddingBottom': '0', 'paddingLeft': '0', 'paddingRight': '0'}
        
    )
    ]),
    dbc.Col([dcc.Graph(
        id='sunburst2',
        figure=figure
    )
    ])
    ]),

    html.Br(),
    html.Br(),
    

    dbc.Row([
        dbc.Col([
             html.H1(
        children='User Interaction',
        style={
            'textAlign': 'center',
            'color': colors['text']
            
            }
                )   
        ]),
        dbc.Col([
         html.H1(
        children='User Demographics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
                )
        ])
    ])
])