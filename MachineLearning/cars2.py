#cars mpg dataset (UCI)
#pre-prosessing raw data, dummy variables, missing values, pipelining
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/cars.py

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#fetch data from internet
raw_data = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data')

#it doesn't come with a header, so I made this short one out of its description
header = ['mpg','cylinders','displacement','horsepower','weight','acceleration',
	'year','origin','name']

#turn it into a dataframe
df = pd.read_table(raw_data, names=header, delim_whitespace=True)

#you should always check out your data when first loading it
print(df.info())
print(df.head())
print('DataFrame Shape: '+str(df.shape))

#it never says so, but in origin, 1 is USA, 2 is Europe, and 3 is Asia
#also, it says that the columns are non-null, but missing values are encoded
#using a '?' so we will go through several methods of fixing the problem
#of missing data

#show some places where ? indicates missing data
missing=df.horsepower=='?'
print(df[missing])

#first, let's try dropping every observation using ?
df.replace('?', np.nan, inplace=True)

#check out replaced
print(df[missing])

#drop them
df_dropped = df.dropna()
print("New DataFrame shape: "+str(df_dropped.shape))

#now, seeing as there is only 6 out of the 398 entries, dropping them isn't so bad
#but for obvious reasons, you probably won't want to simply delete data that was
#considered meaningful by the people who collected it. So you'll want to try other
#more robust method if possible

#one of those is imputing. Which is basically guessing what the missing values are
#with neutral-ish values such as the means of non-missing values

#instantiate our imputer
#let it know what the missing values are
#mean is the method we want to use on missing values
#axis=0 tells it to go column-wise
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

#sklearn does not like DataFrames, and wants numpy arrays
X = np.array(df.drop('name', axis=1))
y = np.array(df.mpg)

#fit the imputer to our data
imp.fit(X)

#transform** our data
#**transform just is a special jargon word for models that transform our data
X = imp.transform(X)

#results for horsepower from the previously missing data
print(X[missing][:,3])

#now you may think, "oh gee, that was easy, now we can use our data with sklearn!"
#but the quest for ultimate one liners never ceases in the world of programming
#you can do everything all at once with pipelining

#instantiate imputer
imp2 = Imputer(missing_values='NaN', strategy='mean', axis=0)

#instantiate machine learning model
reg = LinearRegression()

#pipelining uses two-tuples (two valued objects), with the name of step, and estimator
#NOTE each step but the last must be a transformer, and the last must be an estimator
steps = [('imputation',imp2),('linear regression',reg)]

#make your pipeline, using the pipeline constructor
pipeline=Pipeline(steps)

#always good to have training and testing data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.25,random_state=42)
print(X_train.shape)


#fit pipeline to data
pipeline.fit(X_train, y_train)

#score on the test set
score=pipeline.score(X_test,y_test)

#print out the score
print('The r-squared for our model: '+str(score))
