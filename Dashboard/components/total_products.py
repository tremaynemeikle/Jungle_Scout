# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids
from . import data_table


def render(app: Dash) -> html.Div:
    
    

    @app.callback(
                    Output(ids.TOTAL_PRODUCTS, "children"),
                    Input(ids.STORE_DATA, "data")
                 )
    def update_metrics(data):
        #data = data.from_dict()
        print(pd.DataFrame(data))
        return html.Div(
                        [
                        html.Div(
                                 [     
                                     html.H1(len(data))
                                 ]
                                )
                        ]       
                        )

    return html.Div(id = ids.TOTAL_PRODUCTS
                    )
# %%



