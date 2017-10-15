#based on a course I got at DataCamp.com "pandas Foundations"
#pandas time series, resampling, moving averages 
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
#you pretty much need to pair resampling with some statistical method such as these:
#mean/median/prod/sum/std/var, but you can also use stuff like count,min,max
morning_dew = df.loc['March 2010', 'DewPoint'].resample('D').mean()

print(morning_dew)
morning_dew.plot()
plt.title('Avg Dew Point in Austin, TX Mar 2010')
plt.show()

#we can also get the high for every month really easily
highs = df.Temperature.resample('M').max()
highs.plot(kind='bar')
plt.title('Monthly Highs Austin, TX 2010')
plt.tight_layout()
plt.show()

#we can also use moving averages (rolling means) instead of resampling
#here we apply a window of every 24 values, it doesn't matter the kind of values
#and again you'll need to chain it with some statistical method
july_temp = df['Temperature']['July 1, 2010':"July 20, 2010"]
smooth_july = july_temp.rolling(window=24).mean()
july_df = pd.DataFrame({'smooth':smooth_july,'original':july_temp})
july_df.plot()
plt.title("Temperature in July 2010 Austin, TX")
plt.show()

#and you can even combine both rolling and resampling for an even more concise view
#with even less fluctuation
#we are going to compare fall and spring highs
#here our rolling average will be calculated every week
spring = df['Temperature']['March 20, 2010':'June 21, 2010']
spring_highs = spring.resample('D').max()
#reset index will allow me to compare the two side-by-side, but will remove helpful date info
spring_highs_smoothed = spring_highs.rolling(window=7).mean().reset_index(drop=True)

fall = df['Temperature']['Sep 22, 2010':'Dec 21, 2010']
fall_highs = fall.resample('D').max()
fall_highs_smoothed = fall_highs.rolling(window=7).mean().reset_index(drop=True)

seasons = pd.DataFrame({'spring':spring_highs_smoothed,'fall':fall_highs_smoothed})
seasons.plot()
plt.title('Highs During Spring and Fall Austin, TX')
plt.show()
