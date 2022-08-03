from enum import auto
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
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
pio.renderers.default = 'browser'
dash.register_page(__name__)



colors = {
    'background': '#FFF4E4',
    'text': '#000000'
}

india_states = json.load(open("maps/states_india.geojson", "r"))

state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]


df = pd.read_csv("Data/india_census.csv")
df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])

df["DensityScale"] = np.log10(df["Density"])

fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="DensityScale",
    hover_name="State or union territory",
    hover_data=["Density"],
    title="India Population Density",
    height=800,
    width=700
)

fig.update_geos(fitbounds="locations", visible=False)


#fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))

fig.update_layout(
    autosize=False
)

# define the page content with variable called layout
layout = html.Div(children=[
    html.H1(children=''),

    html.Div(children='''
       '''),
    dcc.Graph(
        id='india-map',
        figure=fig,
        responsive=True
    )
])

