#based on a course I got at DataCamp.com "pandas Foundations"
#pandas time series, resampling
#pandas_austin3.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen

url = ('https://assets.datacamp.com/production/course_1639/'+
	'datasets/weather_data_austin_2010.csv')

raw_data = urlopen(url)

df = pd.read_csv(raw_data, parse_dates=['Date'], index_col='Date')

#we will be doing similar stuff as pandas_austin2.py, but with built in pandas methods
#like getting average dew point for every day in March
morning_dew = df.loc['March 2010', 'DewPoint'].resample('D').mean()

print(morning_dew)
morning_dew.plot()
plt.show()


