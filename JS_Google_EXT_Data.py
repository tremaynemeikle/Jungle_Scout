# %%
import pandas as pd 
from datetime import date
import os
from statistics import mean, median

pd.set_option('display.max_columns', None)

data_directory = "Data/Google_EXT_Data"

file_names = os.listdir(data_directory)

df_master = pd.DataFrame()

# Select starting date for filtering .. if none, default is 1 year from present day
year = 2023
month = 1
day = 1

Name = []
Price_Avg =[]
Units_Sold_Avg = []
Daily_Units_Sold = []
Revenue = []
Star_Rating = []
Reviews = []
Numb_Products_Last_Year = []
Review_Under_50 = []
Monthly_Sold_Above_300 =[]
Numb_Products_On_Page = []

filtered_df = pd.DataFrame()
raw_df = pd.DataFrame()

for i in file_names:

    if i == ".DS_Store":
        pass
    
    else:
        df = pd.read_csv(f"{data_directory}/{i}")

        df = df.iloc[:, 2:]

        col_float = ["Price", "Amazon Fees", "Monthly Revenue", "Net Revenue", "Star Rating"]
        col_int = ["Monthly Units Sold", "Daily Units Sold", "Reviews", "BSR"]

        df[col_int] = df[col_int].replace(",", "", regex = True)
        df[col_float] = df[col_float].replace([",", "\$"], "", regex = True)

        col_drop = ["Date First Available", "Monthly Units Sold", "Daily Units Sold", "Reviews"]

        df = df.dropna(axis = 0, subset = col_drop)

        df["Date First Available"] = pd.to_datetime(df["Date First Available"], format = "%m/%d/%Y")

        df["Monthly Revenue"] = df["Monthly Revenue"].replace("M", "0000", regex = True)

        Numb_Products_On_Page.append(len(df))

        if (year == None) | (month == None) | (day == None):
            year = (date.today().year - 1)
            month = date.today().month
            day = date.today().day

        date_filtered_df = df.loc[df["Date First Available"] >= f"{year}-{month}-{day}"]

        col_float = ["Price", "Monthly Revenue", "Star Rating"]
        col_int = ["Monthly Units Sold", "Daily Units Sold", "Reviews"]
        
        date_filtered_df[col_float] = date_filtered_df[col_float].astype(float)
        date_filtered_df[col_int] = date_filtered_df[col_int].astype(int)

        i = i[15:]
        i = i[:-4]

        review_50 = len(date_filtered_df.loc[date_filtered_df["Reviews"] <= 50])
        monthly_sold_300 = len(date_filtered_df.loc[date_filtered_df["Monthly Units Sold"] >= 300])

        Name.append(i)
        Price_Avg.append(date_filtered_df["Price"].median())
        Units_Sold_Avg.append(round(median(date_filtered_df["Monthly Units Sold"]), 2))
        Daily_Units_Sold.append(round(median(date_filtered_df["Daily Units Sold"])))
        Revenue.append(round(median(date_filtered_df["Monthly Revenue"]), 2))
        Star_Rating.append(round(mean(date_filtered_df["Star Rating"]), 2))
        Reviews.append(round(mean(date_filtered_df["Reviews"]), 2))
        Numb_Products_Last_Year.append(len(date_filtered_df))
        Review_Under_50.append(review_50)
        Monthly_Sold_Above_300.append(monthly_sold_300)

        filtered_df = pd.concat([filtered_df, date_filtered_df])
        raw_df = pd.concat([df, raw_df])


dict = {"Search Inquiry": Name, 
        "Price (Median)": Price_Avg,
        "# Prod. Montly Units Sold > 300": Monthly_Sold_Above_300, 
        "Monthly Units Sold (Median)": Units_Sold_Avg, 
        "Daily Units Sold (Median)": Daily_Units_Sold, 
        "Monthly Revenue (Median)": Revenue,
        "Star Rating": Star_Rating,
        "Prods. < 50 Reviews": Review_Under_50,
        "Reveiws (Avg)": Reviews,
        "Total # Of Products In Last Year": Numb_Products_Last_Year,
        "Total # Product On Page": Numb_Products_On_Page}

df_master = pd.DataFrame(dict)

df_master["% of Prods. W/ < 50 Reviews Of Recent Avail Prods."] = (df_master["Prods. < 50 Reviews"]/df_master["Total # Of Products In Last Year"]) * 100

#df_master.to_excel("../Previous Year Extension Data.xlsx")
df_master.to_csv("Data/Data Exports/Previous Year Extension Data")

raw_df.drop_duplicates(inplace = True)
raw_df.to_excel("../Spread Sheets/Full_DataSet.xlsx")


 # %%
