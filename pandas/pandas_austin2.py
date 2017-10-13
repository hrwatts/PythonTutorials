#based on a course I got at DataCamp.com "pandas Foundations"
#more working with data time in pandas!
#pandas_austin2.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen

url = ('https://assets.datacamp.com/production/course_1639/'+
	'datasets/weather_data_austin_2010.csv')

raw_data = urlopen(url)

#same as austin, except now we start out with the good df, indexed by dates
df = pd.read_csv(raw_data, parse_dates=['Date'], index_col='Date')

#check it out
print(df.head())


print('DewPoint Monthly----------')
#let's say that we want to see the dewpoint throughout the month of March
print(df.loc['March 2010'].size)
print(df.loc['March 2010'].index.hour)

#but its waaaay too much to view it hourly (2229 values!), so how about every morning?
#be sure to slice using the same df subslice!
morning_dew =  df.loc['March 2010'][df.loc['March 2010'].index.hour==6]

#now you have the daily dew point of march at 6am
print(morning_dew['DewPoint'])

morning_dew['DewPoint'].plot()
#plt.show()

#we can clearly see it steadily goes up throughout march! Much easier than hourly plotting...
df.loc['March 2010']['DewPoint'].plot()
#plt.show()

#but let's say for some reason you now have only this "morning_dew" dataframe to work out of
#and you want to to be accessable just like the normal march 2010 dataframe is, hourly
#but you don't have any more data to put in. You can back and forward fill the existing data
#to populate the entire dataframe

#first we will reindex our dataframe to be accessable hourly (with data, already hourly accessable)
morning_dew_hourly = morning_dew.reindex(df.loc['March 2010'].index)
print(morning_dew_hourly.loc['March 1, 2010'])

#but there is still no data for all those blank slots!
#try using the method argument, this time with forward fill 
morning_dew_hourly = morning_dew.reindex(df.loc['March 2010'].index, method='ffill')
print(morning_dew_hourly.loc['March 1, 2010'])

#now the method argument again, this time with backwards fill 
morning_dew_hourly = morning_dew.reindex(df.loc['March 2010'].index, method='bfill')
print(morning_dew_hourly.loc['March 1, 2010'])

