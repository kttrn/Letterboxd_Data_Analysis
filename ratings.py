import pandas as pd

df = pd.read_csv('ratings.csv')
df = df.drop(['Date', 'Name', 'Year', 'Letterboxd URI'], axis=1)


column1 = (df['Rating'] == 0.5).sum()
print(column1)
column2 = (df['Rating'] == 1.0)

column3 = (df['Rating'] == 1.5).sum()
print(column3)

