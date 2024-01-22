# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

from . import ids


#data = pd.read_pickle("/Users/trey/Desktop/Python Projects/Spotify EDA/Dashboard/components/data/playlist_data.pickle")

def render(app: Dash) -> html.Div:
    
    return html.Div(children = [
                                html.H5("Sales Filter"),  
                                dbc.Row([
                                        dbc.Col(
                                                [
                                                dcc.Input(id = ids.SALES_LOWER_BOUND, type = "number", placeholder="Sales Min")
                                                ]
                                                ),

                                        dbc.Col(
                                                [
                                                dcc.Input(id = ids.SALES_UPPER_BOUND, type = "number", placeholder= "Sales Max")
                                                ]
                                                )
                                        ])

                                ]
                    )
# %%


