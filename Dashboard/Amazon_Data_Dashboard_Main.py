
# %%
from dash import Dash, html
from dash_bootstrap_components.themes import SUPERHERO, BOOTSTRAP
import dash_bootstrap_components as dbc

from components.layout import create_layout

#import JS_Google_EXT_Data

import pandas as pd

import os

# %%
def main() -> None:

    
    print(os.getcwd())

    data = pd.read_pickle("Jungle_Prod_Data_Clean/Jungle_Data_Std_300")
    #data = pd.read_csv("Data/Data Exports/Full_Data")
    app = Dash(external_stylesheets = [dbc.themes.JOURNAL, dbc.icons.FONT_AWESOME])

    app.title = "Product Database Analysis"
    app.layout = create_layout(app, data)

    app.run()


if __name__ == "__main__":
    main()


# %%
