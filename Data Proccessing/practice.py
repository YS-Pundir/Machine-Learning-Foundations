import pandas as pd
df=pd.read_csv("machine.csv")
print("Total misssing data")
print("Total null values : ")
print(df.isnull().sum())
print("The percentrage of the null values oer columns")
print(df.isnull().mean()*100)

df_CLeaned=df.dropna(axis=1)
print("The cleaned data is : ")
print(df_CLeaned)
df_CLeaned.to_csv("Cleaned_machine.csv")

