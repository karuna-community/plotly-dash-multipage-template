import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

# Add dashboard specific methods here

def get_dashboard2_layout(ddf2):

    # Call dashboard specific methods here

    return [
        html.Div(id='dashboard2', children=[], className='dashboard2')
    ]
