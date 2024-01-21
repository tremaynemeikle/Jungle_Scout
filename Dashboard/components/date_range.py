# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from datetime import date
import datetime
import dash_bootstrap_components as dbc

from . import ids

def render(app: Dash) -> html.Div:
   
    return html.Div(
                    children = [
                                html.H5("Date First Available Range"), 
                                dbc.Row(
                                        [
                                        dbc.Col(
                                                dbc.Card(
                                                         [
                                                          dcc.DatePickerSingle(
                                                                                id = ids.DATE_RANGE_BEGIN,
                                                                                min_date_allowed = date(2015, 1, 1),
                                                                                max_date_allowed=date.today(),
                                                                                #initial_visible_month=date(2022, 1, 1),
                                                                                placeholder = "Begin Date",
                                                                                date = date.today() - datetime.timedelta(days=365)
                                                                                #end_date=date(2017, 8, 25)
                                                                               )
                                                         ]
                                                        )
                                                ),
                                        dbc.Col(
                                                dbc.Card(
                                                         [
                                                          dcc.DatePickerSingle(
                                                                                id = ids.DATE_RANGE_END,
                                                                                min_date_allowed = date(2015, 1, 1),
                                                                                max_date_allowed=date.today(),
                                                                                #initial_visible_month=date.today(),
                                                                                placeholder = "End Date",
                                                                                date = date.today()
                                                                                #end_date=date(2017, 8, 25)
                                                                               )
                                                         ]
                                                        )
                                                )
                                         ]
                                        )

                                
                                
                                
                                
                                ]
                    )
# %%
