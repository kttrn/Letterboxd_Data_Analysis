import pandas as pd
import csv
from matplotlib import pyplot as plt

df = pd.read_csv('ratings.csv')
df = df.drop(['Date', 'Name', 'Year', 'Letterboxd URI'], axis=1)


def rating_occurrence(n):
    """This function calculates the number of occurrences of each rating"""
    column = (df['Rating'] == n).sum()
    return column


star1 = rating_occurrence(0.5)
star2 = rating_occurrence(1.0)
star3 = rating_occurrence(1.5)
star4 = rating_occurrence(2.0)
star5 = rating_occurrence(2.5)
star6 = rating_occurrence(3.0)
star7 = rating_occurrence(3.5)
star8 = rating_occurrence(4.0)
star9 = rating_occurrence(4.5)
star10 = rating_occurrence(5.0)


# Create a new csv file for the amount of occurrences of ratings
header = ['0.5', '1.0', '1.5', '2.0', '2.5', '3.0', '3.5', '4.0', '4.5', '5.0']
data = [star1, star2, star3, star4, star5, star6, star7, star8, star9, star10]

with open('my_ratings.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# Visualizing
my_ratings = pd.read_csv('my_ratings.csv')
print("Contents in csv file:\n", my_ratings)
my_ratings.plot(kind='bar', figsize=(10, 5), title="My Letterboxd ratings")
plt.show()

