import pandas as pd
df=pd.read_csv("machine.csv")
print("Total misssing data")
print(df.isnull().sum())

df_CLeaned=df.dropna(axis=1)
print("The cleaned data is : ")
print(df_CLeaned.to_)

