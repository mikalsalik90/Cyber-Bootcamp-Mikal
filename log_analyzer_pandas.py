import pandas as pd 

df = pd.read_csv("logs.csv")
print(df)
grouped = df.groupby("ip")["count"].sum()
df.columns = df.columns.str.strip()

