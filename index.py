import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app, server
from apps import dashboard, dashboard2

csv = "mydatastore.csv"

# Add global app methods here
def get_database():

    db = pd.read_csv(csv)

    return db

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div(children=[
        html.H1(children='Plotly Dash Multipage Template App'),
        html.Div(children=[
            html.A(html.Button('Dashboard', className='tab-button'),
                href='/'),
            html.A(html.Button('Dashboard2', className='tab-button'),
                href='/'),
        ], className='tabs'),
    ], className='nav'),

    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    df = get_database()

    if pathname == '/':
        return dashboard.get_dashboard_layout(df)
    elif pathname == '/dashboard2':
         return dashboard2.get_dashboard2_layout(df)
    else:
        return dashboard.get_dashboard_layout(df)

if __name__ == '__main__':
    app.run_server(debug=True)
