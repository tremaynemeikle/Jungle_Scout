# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


def render(app: Dash) -> html.Div:
    
    

    @app.callback(
                    Output(ids.SALES_MEDIAN, "children"),
                    Input(ids.STORE_DATA, "data")
                 )
    def update_metrics(data):
        
        if len(data) == 0:
            sales_med = 0
        
        else:
            data = pd.DataFrame(data)
            sales_med = data["Est. Monthly Sales"].median()
        
        print(data)
        return html.Div(
                        [
                        html.Div(
                                 [     
                                     html.H1(sales_med)
                                 ]
                                )
                        ]       
                        )

    return html.Div(id = ids.SALES_MEDIAN
                    )
# %%



