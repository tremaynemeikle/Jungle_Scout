# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


from . import ids


def render(app: Dash) -> html.Div:
    
    @app.callback(
                    Output(ids.SCAT_GRAPH_REV_REVIEW, "figure"),
                    Input(ids.STORE_DATA, "data")
                 )
    def update_graph(data):
        
        data = pd.DataFrame(data)

        fig = px.scatter(data, x = "Reviews", y = "Est. Monthly Revenue", hover_data = ["Product Name", "ASIN"])
        #df_group = data.groupby(by = ["Category"]).median().reset_index()
        #fig = px.bar(df_group, x = "Category", y = "Est. Monthly Revenue")

        return fig
        

    return dcc.Graph(id = ids.SCAT_GRAPH_REV_REVIEW,
                     )
# %%



