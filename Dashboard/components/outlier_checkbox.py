# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    
    
    return html.Div(
                    children = [
                                #html.H5("Remove Sales Outliers"), 
                                dcc.Checklist(
                                            id = ids.OUTLIER_CHECKBOX,
                                            options = ["Remove Sales Outliers"]
                                            #value = ["Remove Outliers"]
                                            ),
                                
                                ]
                    )
# %%
