# %%
from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from datetime import date

from . import ids

def render(app: Dash, data: pd.DataFrame):

    initial_data_copy = data.copy()
    
    @app.callback(  
                    [         
                     Output(ids.DATA_TABLE, "data"),
                     Output(ids.STORE_DATA, "data"),
                     Output(ids.DATA_TABLE, "tooltip_data")
                    ],
                    [
                     Input(ids.CATEGORY_DROPDOWN, "value"),
                     Input(ids.OUTLIER_CHECKBOX, "value"),
                     Input(ids.DATE_RANGE_BEGIN, "date"),
                     Input(ids.DATE_RANGE_END, "date"),
                     Input(ids.SALES_LOWER_BOUND, "value"),
                     Input(ids.SALES_UPPER_BOUND, "value"),
                     Input(ids.PRICE_LOWER_BOUND, "value"),
                     Input(ids.PRICE_UPPER_BOUND, "value"),
                     Input(ids.PRODUCT_FILTER, "value"),
                     Input(ids.REVIEW_FILTER_LOWER_BOUND, "value"),
                     Input(ids.REVIEW_FILTER_UPPER_BOUND, "value"),
                     Input(ids.REVENUE_FILTER_LOWER_BOUND, "value"),
                     Input(ids.REVENUE_FILTER_UPPER_BOUND, "value")
                    ]
                )
    def update_table(category: list[str], outlier: str, begin_date: str, end_date: str, sales_min: int, sales_max: int, price_min: int, price_max: int, product: list[str], review_min: int, review_max:int, revenue_min:int, revenue_max:int):

        data_copy = initial_data_copy.copy()

        filtered_data = data_copy.query("Category == @category")
        
        # Column Filters
        if sales_min is None:
               sales_min = 0
        
        if price_min is None:
               price_min = 0

        if review_min is None:
               review_min = 0
        
        if revenue_min is None:
               revenue_min = 0
        


        if sales_max is None:
               sales_max = 10000000
        
        if price_max is None:
               price_max = 10000000
        
        if review_max is None:
               review_max = 10000000
       
        if revenue_max is None:
               revenue_max = 10000000
        
        if product is not None:
                filtered_data = filtered_data.loc[(filtered_data["Product Name"].str.contains(product))]
               
        
        filtered_data = filtered_data.loc[(filtered_data["Monthly Units Sold"] >= sales_min) & (filtered_data["Monthly Units Sold"] <= sales_max)]

        filtered_data = filtered_data.loc[(filtered_data["Price"] >= price_min) & (filtered_data["Price"] <= price_max)]

        filtered_data = filtered_data.loc[(filtered_data["Reviews"] >= review_min) & (filtered_data["Reviews"] <= review_max)]

        filtered_data = filtered_data.loc[(filtered_data["Monthly Revenue"] >= revenue_min) & (filtered_data["Monthly Revenue"] <= revenue_max)]

        

        filtered_data.reset_index(drop = True, inplace = True)
        
        if begin_date is not None:
                date_object = date.fromisoformat(begin_date)
                date_string = date_object.strftime('%d/%m/%Y')
        date_string = pd.to_datetime(date_string, dayfirst=True)
        filtered_data = filtered_data.loc[filtered_data["Date First Available"] >= date_string]


        if (outlier == ['Remove Sales Outliers']) & (len(filtered_data) > 0):

                df_std = pd.DataFrame()
                column = "Monthly Units Sold"

                for i in filtered_data["Category"].unique():
                        df_cat = filtered_data.loc[filtered_data["Category"] == i].reset_index(drop = True)
                        sales_median = df_cat[column].median()
                        quantile_25 = df_cat[column].quantile(.25)
                        quantile_75 = df_cat[column].quantile(.75)

                        z_score = []

                        for j in range(0, len(df_cat[column])):

                                # Robust Scaler Since Outliers Present
                                z = (df_cat[column][j] - sales_median)/(quantile_75 - quantile_25)
                                z_score.append(z)

                        df_cat["zscore"] = z_score

                        df_std = pd.concat([df_std, df_cat]).reset_index(drop = True)

                # Drop outliers
                df_std.drop((df_std[df_std["zscore"] > 3].index), inplace = True)
                df_std.drop((df_std[df_std["zscore"] < -3].index), inplace = True)

                df_std.reset_index(drop = True, inplace = True)

                filtered_data = df_std.copy()
        
        return filtered_data.to_dict('records'), filtered_data.to_dict('records'), filtered_data.to_dict('records') 

        
    return html.Div(
                        [
                         html.Div(
                                 dash_table.DataTable(
                                                         id = ids.DATA_TABLE,
                                                         data = initial_data_copy.to_dict('records'), 
                                                         columns = [{"name": i, "id": i, "type": "float"} for i in initial_data_copy.columns],
                                                         page_size = 100,
                                                         sort_action='native',
                                                         style_table=[{'overflowX': 'auto'}, {'height': 5000} ],
                                                         style_cell={
                                                                         # all three widths are needed
                                                                         'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                                                         'overflow': 'hidden',
                                                                         'textOverflow': 'ellipsis',
                                                                     },
                                                         fixed_rows={'headers': True},
                                                         tooltip_data=initial_data_copy.to_dict('records'),
                                                         tooltip_delay=0,
                                                         tooltip_duration=None,
                                                         filter_action='native'
                                                         
                                                      )
                                 )
                        ],
                        style = {'marginBottom': 50, 'marginTop': 25}
                    )


      
                                
                    
# %%
