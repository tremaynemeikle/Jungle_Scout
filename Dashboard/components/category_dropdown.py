# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


#data = pd.read_pickle("/Users/trey/Desktop/Python Projects/Spotify EDA/Dashboard/components/data/playlist_data.pickle")

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    
    category_options = data["Category"].sort_values().unique()
    
    @app.callback(
                  Output(ids.CATEGORY_DROPDOWN, "value"), 
                  Input(ids.CAT_RESTORE_BUTTON, "n_clicks")
                  )
    def restore_cat(click):
        print(click)
        return data["Category"].sort_values().unique()
    
    return html.Div(children = [
                                html.H5("Select Catgories"), 
                                dcc.Dropdown(
                                            id = ids.CATEGORY_DROPDOWN,
                                            options = [{"label": i, "value": i} for i in category_options],
                                            multi = True,
                                            value = category_options,
                                            placeholder="Category",
                                            clearable = True
                                            ),
                                html.Button("Restore All", id = ids.CAT_RESTORE_BUTTON)
                                
                                ]
                    )
# %%
