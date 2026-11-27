import pandas as pd

df=pd.read_csv("C:/Users/ACER/OneDrive/Documents/Python-Intership-BB7-2026/Day06/csv-task/marks.csv")

Average=df['Maths'].mean()
topper_index =df['Maths'].idxmax()
topper_record = df.loc[topper_index]

print(f"Average Marks is {Average}")

print("\n--- Topper Details ---")
print(f"Name: {topper_record['Student']}")

