# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


from . import ids


def render(app: Dash) -> html.Div:
    
    @app.callback(
                    Output(ids.HIST_GRAPH, "figure"),
                    [
                     Input(ids.STORE_DATA, "data"),
                     Input(ids.HISTOGRAM_SELECTION, "value"),
                     Input(ids.HISTOGRAM_SELECTION_2, "value")
                    ]
                 )
    def update_graph(data, selection, selection_2):
        
        data = pd.DataFrame(data)
        
        if selection_2 is None:
            fig = px.histogram(data, x = selection)
        
        else:

            data = data.groupby(by = ["Category"]).median().reset_index()
            fig = px.bar(data, x = selection, y = selection_2)

        return fig
        

    return dcc.Graph(id = ids.HIST_GRAPH
                     )
# %%



