# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

colors = {
    'background': '#FFFFFF',
    'text': '#7FDBFF'
}

data = pd.read_csv("Data/MOCK_DATA.csv")
fig = px.sunburst(data, path=['Category', 'Gender', 'Language'], values='Time most users are viewing')
fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))

data_1 = pd.read_csv("Data/MOCK_DATA_modified.csv")
figure = px.sunburst(data_1, path=['Location', 'Age', 'Gender'], values='Time most users are viewing')
figure.update_layout(margin=dict(t=10, b=10, r=10, l=10))

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div([
    dcc.Loading([
        # ...
    ])
])
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    dcc.Graph(
        id='example-graph-1',
        figure=figure
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)