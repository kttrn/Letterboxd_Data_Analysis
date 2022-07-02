import pandas as pd

df = pd.read_csv('ratings.csv')
df = df.drop(['Date', 'Name', 'Year', 'Letterboxd URI'], axis=1)

def rating_occurrence(n):
    column = (df['Rating'] == n).sum()
    return column

print(rating_occurrence(0.5))
print(rating_occurrence(1.0))
print(rating_occurrence(1.5))
print(rating_occurrence(2.0))
print(rating_occurrence(2.5))
print(rating_occurrence(3.0))
print(rating_occurrence(3.5))
print(rating_occurrence(4.0))
print(rating_occurrence(4.5))
print(rating_occurrence(5.0))