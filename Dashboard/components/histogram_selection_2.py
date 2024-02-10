# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids

def render(app: Dash) -> html.Div:
    
    category_options = ["Category", "Net Revenue", "Monthly Units Sold", "Price", "Reviews", "Date First Available"]
    
    return html.Div(children = [html.H5("y-axis"), 
                                dcc.Dropdown(
                                            id = ids.HISTOGRAM_SELECTION_2,
                                            options = [{"label": i, "value": i} for i in category_options],
                                            multi = False,
                                            placeholder="Column",
                                            clearable = True
                                            ),
                                
                                ]
                    )
# %%
