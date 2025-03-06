import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/shudh/OneDrive/Desktop/Nike/data/data1.csv', sep="\t")

df["building_number"] = df["addressLine1"].str.extract(r'(\d+)')
df["address"]=df["addressLine1"].str.replace(r'\d+', '', regex=True)

df_address=df[["addressLine1", "address","building_number","city","zipCode","Country"]]
search_building_number="160"
df1=df[df["building_number"].str.contains(search_building_number, case=False, na=False)]

# print(df.columns)
print(df1["building_number"])
print(df1["addressLine1"])
