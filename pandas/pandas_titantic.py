#pandas_titantic.py
#string manipulation
#based on a course I got at DataCamp.com "pandas Foundations"

import numpy as np
import pandas as pd
from urllib.request import urlopen
import matplotlib.pyplot as plt

url = ('https://assets.datacamp.com/production/course_1639/datasets/titanic.csv')

raw_data = urlopen(url)

df = pd.read_csv(raw_data)

#take a look at what we will be working with
print(df.iloc[0])

#to manipulate strings, use the .str method on the string column and than whatever you'd
#like to do chained to it
name_lower = df.name.str.lower()
print(name_lower.head())

#this means (not exactly regex, but close!) can be done extremely easily
#let's use this to see how many people who boarded the Titantic lived in Missouri
#fillna just means I am filling NaN values with false.
home_missouri = df['home.dest'].str.contains('MO').fillna(False)
print(df[home_missouri].name)

#wow just 4 people! All from St. Louis too.

#since true is equal to 1 we can also use this to count things
#let's compare the number of cabins on the Titantic
a = df.cabin.str.contains('A').fillna(False).sum()
b = df.cabin.str.contains('B').fillna(False).sum()
c = df.cabin.str.contains('C').fillna(False).sum()
d = df.cabin.str.contains('D').fillna(False).sum()
e = df.cabin.str.contains('E').fillna(False).sum()
f = df.cabin.str.contains('F').fillna(False).sum()
g = df.cabin.str.contains('G').fillna(False).sum()
t = df.cabin.str.contains('T').fillna(False).sum()
cabins = [a,b,c,d,e,f,g,t]
cabin_names = ['A','B','C','D','E','F','G','T']
plt.bar(range(8), height=cabins)
plt.xticks(np.arange(8),cabin_names)
plt.show()

#looks like most of the cabins were C
