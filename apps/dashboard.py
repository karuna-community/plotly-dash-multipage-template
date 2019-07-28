import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

# Add dashboard specific methods here

def get_dashboard_layout(ddf):

    # Call dashboard specific methods here

    return [
        html.Div(id='dashboard', children=[], className='dashboard')
    ]
