import pandas as pd
import numbers as np
import random

data1 = [random.random() for _ in range(10000)]  # Use range instead of a tuple
df = pd.DataFrame(data1, columns=["Random Values"])  # Adding a column name for clarity
print(df.head())

# ------------------------------------------------------------------------------

data2 = [[i,random.random(10,99)] for i in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
df = pd.DataFrame(data2)
print(df.head())

#  (OR)

data2 = [[i, random.uniform(10, 99)] for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
df = pd.DataFrame(data2, columns=["Letter", "Random Value"])
print(df.head())

# ------------------------------------------------------------------------------

data3 = {"Model":["T57","T61","T64","T65"],
         "Price" : ["1.42","1.48","1.73","1.95"],
         "Size":["57 inches","61 inches","64 inches","65 inches"]}

df = pd.DataFrame(data3)
print(df.head())

# ------------------------------------------------------------------------------

data3 = {"Model":["T57","T61","T64","T65"],
         "Price" : ["1.42","1.48","1.73","1.95"],
         "Size":["57 inches","61 inches","64 inches","65 inches"]}

df = pd.DataFrame(
    {"Price": data3["Price"],"Size": data3["Size"]},
    index=data3["Model"])

print(df.head())

# ------------------------------------------------------------------------------

data3 = {"Model":["T57","T61","T64","T65"],
         "Price" : ["1.42","1.48","1.73","1.95"],
         "Size":["57 inches","61 inches","64 inches","65 inches"]}
df = pd.DataFrame(data3)
print(df.loc[:"T61"])

# ------------------------------------------------------------------------------

data4 = [{"Ht": 63, "Len": 45, "Wt": 2.6},
         {"Ht": 29, "Wt": 1.7},
         {"Ht": 37, "Len": 71,"Wt": 4.2}]
df = pd.DataFrame(data4)
print(df.head())

# ------------------------------------------------------------------------------

data4 = [{"Ht": 63, "Len": 45, "Wt": 2.6},
         {"Ht": 29, "Wt": 1.7},
         {"Ht": 37, "Len": 71,"Wt": 4.2}]
df = pd.DataFrame(data4)
df.to_csv("d:\SnowFlake\Re_Prac\prac2_Pandas.csv")

# ------------------------------------------------------------------------------

df = pd.read_csv("d:\SnowFlake\Re_Prac\prac2_Pandas.csv")

print(df)

# ------------------------------------------------------------------------------

df = pd.read_csv("d:\SnowFlake\Re_Prac\prac2_Pandas.csv")
d4str = df.to_string()
print(d4str)

# ------------------------------------------------------------------------------

df = pd.read_csv("d:\SnowFlake\Re_Prac\prac2_Pandas.csv")
data4_json = df.to_json()
print(data4_json)

# ------------------------------------------------------------------------------
