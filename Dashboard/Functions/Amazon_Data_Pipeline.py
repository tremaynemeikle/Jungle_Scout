# %%
import pandas as pd 
from datetime import date
import os
from statistics import mean, median

def data_pipeline(data_type: str, folder = None):
    
    if data_type == "data_base":

        # Concat csvs
        df = pd.DataFrame()

        data_directory = "Data/Product CSVs"
        folder = "Prod. Data - STD - Price 25-40 - Review max 1000 - FDA 6M"

        for i in os.listdir(f"{data_directory}/{folder}"):

            if i == ".DS_Store":
                pass
            else:
                get_df = pd.read_csv(f"{data_directory}/{folder}/{i}", header = 2)
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
        df.to_csv(f"Data/Data Exports/Prod. Database Data/{folder}")
    
    
    elif data_type == "ext_search":
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

        df_master.drop_duplicates(inplace=True)
        df_master.reset_index(drop = True, inplace=True)
        #df_master.to_excel("../Previous Year Extension Data.xlsx")
        df_master.to_csv("Data/Data Exports/Filtered Extension Data")

        raw_df.drop_duplicates(inplace = True)
        column_to_move = raw_df.pop("Link")

        # insert column with insert(location, column_name, column_value)
        raw_df.insert(1, "Link", column_to_move)

        raw_df.reset_index(drop = True, inplace=True)
        raw_df.to_csv("Data/Data Exports/Full Prod List CSV/Full_Data")

    else:
        print("Check data_type")
    
    return None




        # %%


if __name__ == "__main__":
    data_pipeline("data_base")