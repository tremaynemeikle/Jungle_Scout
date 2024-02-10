# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


#data = pd.read_pickle("/Users/trey/Desktop/Python Projects/Spotify EDA/Dashboard/components/data/playlist_data.pickle")

def render(app: Dash) -> html.Div:
    
    category_options = ["Category", "Net Revenue", "Monthly Sales", "Price", "Reviews", "Date First Available"]
    
    return html.Div(children = [html.H5("Select Histogram Data"), 
                                dcc.Dropdown(
                                            id = ids.HISTOGRAM_SELECTION,
                                            options = [{"label": i, "value": i} for i in category_options],
                                            multi = False,
                                            value = "Category",
                                            placeholder="Column",
                                            clearable = True
                                            ),
                                
                                ]
                    )
# %%
