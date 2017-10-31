#pandas_population.py
#interpolation
#based on a course I got at DataCamp.com "pandas Foundations"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen

#world population every 10 years
raw_data = urlopen('https://assets.datacamp.com/production/'+
'course_1639/datasets/world_population.csv')

#read it in, make a datetime object out of the year column, and make that the index
df = pd.read_csv(raw_data, parse_dates=True, index_col='Year')

#take a look
print(df.head())

df.plot(kind='bar')
plt.title("World Population by decade")
plt.xlabel('Year')
plt.ylabel('World Population')
plt.show()

#now we will up sample this to yearly (A for annually)
df_resampled=df.resample('A').first()
print(df_resampled.head())

#but when we do this we end up with a lot of NaNs that we
#could reasonably fill with data through interpolation
#if we wanted the values to be filled in linearly between decades
#we can tag .interpolate('linear') on to the end of our resampling
df = df.resample('A').first().interpolate('linear')
print(df.head())

df.plot()
plt.title("Yearly interpolation of World Population")
plt.xlabel('Year')
plt.ylabel('World Population')
plt.show()
