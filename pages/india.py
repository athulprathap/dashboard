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
import xlrd
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt


fp = "Igismap/Indian_States.shp"
map_df = gpd.read_file(fp)


dash.register_page(__name__)

colors = {
    'background': '#FFF4E4',
    'text': '#000000'
}

# define the page content with variable called layout
layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
])
