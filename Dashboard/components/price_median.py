# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


def render(app: Dash) -> html.Div:
    
    @app.callback(
                    Output(ids.PRICE_MEDIAN, "children"),
                    Input(ids.STORE_DATA, "data")
                 )
    def update_metrics(data):
        
        if len(data) == 0:
            price_med = 0
        
        else:
            data = pd.DataFrame(data)
            price_med = data["Price"].median()
        
        print(data)
        return html.Div(
                        [
                        html.Div(
                                 [     
                                     html.H1(price_med)
                                 ]
                                )
                        ]       
                        )

    return html.Div(id = ids.PRICE_MEDIAN
                    )
# %%



