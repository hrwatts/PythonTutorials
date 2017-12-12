#portland.py
#More Prophet forecasting

import numpy as np
import pandas as pd
import calendar
import matplotlib.pyplot as plt
from urllib.request import urlopen
from fbprophet import Prophet


#Monthly ridership of the portland public transit system
df = pd.read_csv("portland.csv", parse_dates=['date'])

#Prophet strictly enforces ds and y column names
df = df.rename(columns={'date': 'ds','riders': 'y'})

#check to make sure that went okay
print(df.info())

model = Prophet()

#let's actually withhold some data
train = df[:96] #8 years of data
test = df[96:] #about 1.5 years of data

model.fit(train)

#expanded datetime df to include 36 additional months based at the start of each month (MS)
future = model.make_future_dataframe(periods=36, freq='MS')

predictions = model.predict(future)

model.plot(predictions, uncertainty=True)
plt.ylabel('Monthly Number of Transit Passengers')
plt.xlabel('Date')
plt.show()

