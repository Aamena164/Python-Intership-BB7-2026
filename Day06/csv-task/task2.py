import pandas as pd

df=pd.read_csv("C:/Users/ACER/OneDrive/Documents/Python-Intership-BB7-2026/Day06/csv-task/products.csv")

filtered_df=df[df['Price']>5000]

print(filtered_df)