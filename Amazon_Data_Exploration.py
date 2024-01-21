# %%
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_pickle("Jungle_Prod_Data_Clean/Jungle_Data_Std_300")

df_std = pd.DataFrame()
column = "Est. Monthly Sales"

for i in df["Category"].unique():
    df_cat = df.loc[df["Category"] == i].reset_index(drop = True)
    sales_median = df[column].median()
    quantile_25 = df[column].quantile(.25)
    quantile_75 = df[column].quantile(.75)

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





# Table stats grouped by categories (Monthly Sales Outliers removed)
df_std.groupby(by = ["Category"]).agg(
                                    
                                    No_Items = ('Category', 'count'),
                                    Monthly_Revenue_Median = ('Est. Monthly Revenue', 'median'), 
                                    Monthly_Sales_Median = ('Est. Monthly Sales', 'median'), 
                                    Price_Median = ('Price', 'median'),
                                    Reviews_Mean = ('Reviews', 'mean')
                                    
                                    ).sort_values(by = "No_Items", ascending=False)



# %%