# %%
import pandas as pd 
from datetime import date
import os
from statistics import mean

pd.set_option('display.max_columns', None)

data_directory = "Google_EXT_Data"

file_names = os.listdir(data_directory)

df_master = pd.DataFrame()

Name = []
Price_Avg =[]
Units_Sold_Avg = []
Daily_Units_Sold = []
Revenue = []
Star_Rating = []
Reviews = []

df_prev_year = pd.DataFrame()

for i in file_names:

    df = pd.read_csv(f"{data_directory}/{i}")

    df = df.iloc[:, 2:]

    col_float = ["Price", "Amazon Fees", "Monthly Revenue", "Net Revenue", "Star Rating"]
    col_int = ["Monthly Units Sold", "Daily Units Sold", "Reviews", "BSR"]

    df[col_int] = df[col_int].replace(",", "", regex = True)
    df[col_float] = df[col_float].replace([",", "\$"], "", regex = True)

    col_drop = ["Date First Available", "Monthly Units Sold"]

    df = df.dropna(axis = 0, subset = col_drop)

    df["Date First Available"] = pd.to_datetime(df["Date First Available"], format = "%m/%d/%Y")


    year = (date.today().year - 1)
    month = date.today().month
    day = date.today().day

    df = df.loc[df["Date First Available"] >= f"{year}-{month}-{day}"]

    col_float = ["Price", "Monthly Revenue", "Star Rating"]
    col_int = ["Monthly Units Sold", "Daily Units Sold", "Reviews"]
    
    df[col_float] = df[col_float].astype(float)
    df[col_int] = df[col_int].astype(int)

    Name.append(i)
    Price_Avg.append(df["Price"].mean())
    Units_Sold_Avg.append(round(mean(df["Monthly Units Sold"]), 2))
    Daily_Units_Sold.append(round(mean(df["Daily Units Sold"])))
    Revenue.append(round(mean(df["Monthly Revenue"]), 2))
    Star_Rating.append(round(mean(df["Star Rating"]), 2))
    Reviews.append(round(mean(df["Reviews"]), 2))

    df_prev_year = pd.concat([df_prev_year, df])


dict = {"Search Inquiry": Name, 
        "Price": Price_Avg, 
        "Monthly Units Sold": Units_Sold_Avg, 
        "Daily Units Sold": Daily_Units_Sold, 
        "Monthly Revenue": Revenue,
        "Star Rating": Star_Rating,
        "Reveiws": Reviews}

df_master = pd.DataFrame(dict)


# %%
