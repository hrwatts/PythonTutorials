#based on a course I got at DataCamp.com "pandas Foundations"
#working with date time in pandas!
#pandas_austin.py

import numpy as np
import pandas as pd
from urllib.request import urlopen

url = ('https://assets.datacamp.com/production/course_1639/'+
	'datasets/weather_data_austin_2010.csv')

raw_data0 = urlopen(url)
raw_data1 = urlopen(url)
raw_data2 = urlopen(url)
raw_data3 = urlopen(url)

#reads without parsing the str to DateTime object (technically TimeStamp object)
print("Start---------\n")
df = pd.read_csv(raw_data0)

print(df.iloc[0])
print(df.Date[0])
print(type(df.Date[0]))

#but you can still parse it even after this!
#you tell it what format it is currently in, and it can change it!
date_format = '%Y%m%d %H:%M'
df.Date = pd.to_datetime(df.Date, format=date_format)
print(df.iloc[0])
print(df.Date[0])
print(type(df.Date[0]))

#reading in the data with argument parse_dates=True
#will convert string dates (true to look in all columns, or specify) 
#found into ISO 8601 format datetime objects
#yyyy-mm-dd hh:mm:ss
print("DF1---------\n",df.head())
df = pd.read_csv(raw_data1, parse_dates=['Date'])

print(df.iloc[0])
print(df.Date[0])
print(type(df.Date[0]))

#sometimes the date is in such a strange format that pandas can't automattically convert it
#so you need to throw in a date parser, which is a function that puts the string into a more
#acceptable format, pandas.datetime.strptime() 
#will take a string and strip it into a format pandas likes
#since we have our dates as yyyymmdd hr:min this is what we tell strptime()
dateparse = lambda x: pd.datetime.strptime(x, '%Y%m%d %H:%M')

df = pd.read_csv(raw_data2, parse_dates=['Date'], date_parser=dateparse)


print("DF2---------\n",df.head())
print(df.Date[0])
print(type(df.Date[0]))

#but (as you can see) pandas was able to catch that there was no "-" in the dates and no secs either
#something that really comes in handy when working with dated datasets is indexing by dates
#instead of 0,1,2,3,4,5 indexing ect, use the dates to index your dataframe!
df = pd.read_csv(raw_data3, parse_dates=['Date'], date_parser=dateparse, index_col='Date')

print("DF3---------\n",df.head())
print("DF3 INFO()---------")
print(df.info())

#so using this, pandas will be more intuitive about what is in the dataframe
#look at df.info(), its says
'''
DatetimeIndex: 8759 entries, 2010-01-01 00:00:00 to 2010-12-31 23:00:00
'''
#so you can in a much easier way see that this data is hourly for all of 2010
#way better than just '8759' entries
#you can also use much more sophisticated slicing (use .loc NOT .iloc)

#let's get the temperature for Austin at midnight on Feb 2nd
print("Feb 2nd Midnight Temp:",df.loc['2010-02-02 00:00:00', 'Temperature'])

#but it gets even better! Check out getting an entire day
#you don't even have to get fancy with dates!
print('May 4th All day Temp\n',df.loc['2010-5-4','Temperature'])

#this is known as partial string selection
#you could have used any of these as well, pandas supports it!
#df.loc['May 4, 2010']
#df.loc['2010-May-4']
#you could also do entire months, years, basically whatever
#you can even slice with partial datetime strings
print('Temperature Midnight June 11th to 3pm 4th of July\n',
	df.loc['2010-6-11':'July 4, 2010 15:00','Temperature'])
