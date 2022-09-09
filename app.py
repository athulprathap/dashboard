from dash import Dash, html, dcc
import dash
from dash import Dash, html, dcc
from pyparsing import White
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)

app.layout = html.Div([
    # add a navbar
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("India", href="/india")),
            dbc.NavItem(dbc.NavLink("User Insights", href="/sunburst")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Ad Insights", href="/ads"),
                    dbc.DropdownMenuItem("Ad India", href="/india-ads"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Reelro Analytical Dashboard",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    # add the page content
    html.Div(id="page-content", className="p-4"),
    # add a animation to the page
    dbc.Spinner(html.Div(id="loading-output")),

    dash.page_container
])



if __name__ == '__main__':
	app.run_server(debug=True)