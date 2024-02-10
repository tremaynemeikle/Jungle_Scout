# %%
import pandas as pd 
import os 

# Concat csvs
df = pd.DataFrame()

data_directory = "Data/Data Exports/Full Prod List CSV"


get_df = pd.read_csv(f"{data_directory}/Full_Data")
df = pd.concat([df, get_df])

df.drop_duplicates(inplace=True)

df.reset_index(drop = True, inplace = True)

# Remove dollar signs
str_cols = df.select_dtypes(include=['object'])

for i in str_cols:
    #df[i] = df[i].str[1:]
    df[i] = df[i].str.replace('$', "", regex = True) 
    df[i] = df[i].str.replace(',', "", regex = True)
    df[i] = df[i].str.replace('N.A', "--", regex = True)

# Drop '--' and Nan from 'Est. Monthly Sales'
df.drop(df[df["Monthly Units Sold"] == "--"].index, inplace = True)
df.drop(df[df["Monthly Units Sold"].isnull()].index, inplace = True)

df.drop(df[df["Monthly Revenue"] == "--"].index, inplace = True)

# Convert columns to int
int_cols = ["Monthly Units Sold"]
for i in int_cols:
    df[i] = df[i].astype(int)

# Convert columns to float
float_cols = ["Monthly Revenue", "Price"]
for i in float_cols:
    df[i] = df[i].astype(float)

# Convert date time
df["Date First Available"] = pd.to_datetime(df["Date First Available"], dayfirst=True)

df.drop(columns = df.columns[0], inplace=True)

# Export Cleaned data to pickle
df.to_pickle("Jungle_Prod_Data_Clean/Jungle_Data_Std_300")


# %%
