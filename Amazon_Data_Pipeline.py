# %%
import pandas as pd 
import os 

# Concat csvs
df = pd.DataFrame()

for i in os.listdir("Jungle_Prod_Data"):

    if i == ".DS_Store":
        pass
    else:
        get_df = pd.read_csv(f"Jungle_Prod_Data/{i}", header = 2)
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
df.drop(df[df["Est. Monthly Sales"] == "--"].index, inplace = True)
df.drop(df[df["Est. Monthly Sales"].isnull()].index, inplace = True)

df.drop(df[df["Est. Monthly Revenue"] == "--"].index, inplace = True)

# Convert columns to int
int_cols = ["Est. Monthly Sales"]
for i in int_cols:
    df[i] = df[i].astype(int)

# Convert columns to float
float_cols = ["Est. Monthly Revenue", "Price"]
for i in float_cols:
    df[i] = df[i].astype(float)

# Convert date time
df["Date First Available"] = pd.to_datetime(df["Date First Available"], dayfirst=True)

# Export Cleaned data to pickle
df.to_pickle("Jungle_Prod_Data_Clean/Jungle_Data_Std_300")


# %%
