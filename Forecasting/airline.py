#airline.py
#Working with FaceBook Prophet on Box Jenkin's Monthly Airline Data
#Prophet Basics

#Based on a tutorial by Thomas Vincent on DigitalOcean.com
#https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-prophet-in-python-3

import numpy as np
import pandas as pd
import calendar
import matplotlib.pyplot as plt
from urllib.request import urlopen
from fbprophet import Prophet

#for some reason it is very difficult to find this small, simple dataset labeled
#in some format that python can read it, all I could find is raw numbers

#some background
#this dataset contains twelve years of monthly airline passengers from 1949 to 1960

url = "http://www.stat.purdue.edu/~chong/stat520/bjr-data/airline-pass"

raw_data = urlopen(url)

#it is not in a nice format to read into a dataframe
#so I fixed it
data = []
[[data.append(int(num)) for num in l] for l in [str(x)[4:-3].split() for x in raw_data]]

#now all the data is in a single vector
print(data[:12])

date = []
[[date.append(calendar.month_name[index]+', '+str(year)) 
	for index in range(1,13)] for year in range(1949,1961)]
print(date[:6])

#now that we have the data, and the date of the data, let's turn it into a dataframe
#that the tutorial supposes we have
data = np.array(data)
date = np.array(date)

df = pd.DataFrame({"Month":date,"AirPassengers":data})

#use %B for a month's fully qualified name
date_format = '%B, %Y'
df.Month = pd.to_datetime(df.Month, format=date_format)


print(df.head())

#----------------------------------------------------------------------------------------
#Here is where we can actually start using Prophet! We now have the same dataset as the tutorial
#Note: Prophet will use DateTime objects for date, so do not skip that step

#quick visualization of our data
df.set_index('Month').plot(figsize=(12, 8))
plt.ylabel('Monthly Number of Airline Passengers')
plt.xlabel('Date')
plt.show()

#so there is a clear pattern... but how do we extract that pattern and make predictions
#in a way that scales? Use Prophet!

#for starters, we will prepare the data into a way Prophet will work with it
#for some reason, Prophet requires that the two columns you use are named
#ds and y
#ds is the time column, y the metrics
#see the docs
'''
The input to Prophet is always a dataframe with two columns: ds and y. The ds (datestamp) column must contain a date or datetime (either is fine). The y column must be numeric, and represents the measurement we wish to forecast.
'''
df = df.rename(columns={'Month': 'ds','AirPassengers': 'y'})
print(df.head())

#this is where you would set some of your hyper-paramters if you want
#use help(Prophet) to check for parameters, the docs are incomplete online
#you would tune the hyper-parameters in order to adjust your model
model = Prophet()

#then since it is based off the sk-learn API, you can already figure how to use it
#since columns are hardcoded, rembemer to only use those!
model.fit(df)

#now it gave us a bunch of stuff that I really don't understand well
#but if you want to learn more just watch some YouTube videos on ARIMA models to understand

print(type(model))

#getting the predictions is the same, but since it is time-based it is a little trickier
#Prophet has a method that gives you a DataFrame with a column containing
#all dates of the training set, plus a series of future points you specify
#so for example I say 36 additional intervals, with a frequency of 'MS'
#'M' is monthly as you'd expect, and the 'S' after that means the start of each month
future_timestamps = model.make_future_dataframe(periods=36, freq='MS')

#see the end of the new timestamps
print(future_timestamps.tail())

#we need to do this because of the special way Prophet makes predictions
#to make predictions, you give the model dates to predict on
#otherwise similar to sk-learn
predictions = model.predict(future_timestamps)

#let's take a look at our model's predictions
print(predictions.head())

#now we observe a lot of data from this, again to learn more you should learn about ARIMA
#but here are some important take aways
#ds: the datestamp
#yhat: what statistics calls the forecasted value for y as time ds
#yhat_lower: lower bounds of our forecast at ds
#yhat_upper: upper bounds of our forecast at ds

#conviently, Prophet has built in ploting abilities
#which will plot what it believe to be important things
model.plot(predictions, uncertainty=True)
plt.ylabel('Monthly Number of Airline Passengers')
plt.xlabel('Date')
plt.show()

#the black dots are the observed values from the training set
#the thick blue line is yhat
#and the light blue is the area between yhat_upper and yhat_lower

#and also, wow that is some serious predictive power!

#another cool feature is that Prophet can easily show you what it is using to build it's model
#or in other words, the components of the model
model.plot_components(predictions)
plt.show()

#and this is nothing compared to it's built in ability for 'seasoning'
#in which is can make even more complex predictions
