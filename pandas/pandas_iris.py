#panda_iris.py
#demonstrate some powerful uses of the pandas library
#Visual Exploratory Data Analysis
#based on a course I got at DataCamp.com "pandas Foundations"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen

url = ("https://raw.githubusercontent.com/"+
"uiuc-cse/data-fa14/gh-pages/data/iris.csv")

raw_data = urlopen(url)

iris = pd.read_csv(raw_data)

#.info() gives you some information about the dataframe
print(iris.info())

#.describe() gives you a statistical outlook of a dataframe
print(iris.describe())

#.head() returns the first 5 values
print(iris.head())

#let's do some EDA, Exploratory Data Analysis
#built into dataframes are helpful .plot() methods
#specific x and y axis, and tell it you want a scatter plot
iris.plot(x='sepal_length',y='sepal_width',kind='scatter')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

#let's make a box plot out of one feature
#range is the out lines with dashes to them
#interquartile range (IQR) is shown by the outer edges of the box
#median is the red line inside
plt.close()
iris.plot(y='sepal_length',kind='box')
plt.ylabel('sepal length (cm)')
plt.show()

#now a histogram
#you can pass arguments of a matplotlib histgram to this the exact same
plt.close()
iris.plot(y='sepal_length',kind='hist',bins=30, range=(4,8), normed=True)
plt.xlabel('sepal length (cm)')
plt.show()

#a Cumulative Distribution Function histogram
plt.close()
iris.plot(y='sepal_length',kind='hist',bins=30,cumulative=True,
          range=(4,8), normed=True)
plt.xlabel('sepal length (cm)')
plt.show()
