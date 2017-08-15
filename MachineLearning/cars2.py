#cars mpg dataset (UCI)
#pre-prosessing raw data, missing values, pipelining
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/cars2.py

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
print(X_test.shape)

#fit pipeline to data
pipeline.fit(X_train, y_train)

#make a prediction
y_pred = pipeline.predict(X_test)

#manually evaluate the prediction
manual_score=np.mean(y_pred/y_test)
print(manual_score)

#score on the test set
score=pipeline.score(X_test,y_test)

#print out the score
print('The r-squared for our model: '+str(score))

#while something is clearly VERY odd about this r-squared being equal to 1
#I cannot uncover it
#here is output to console
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 9 columns):
mpg             398 non-null float64
cylinders       398 non-null int64
displacement    398 non-null float64
horsepower      398 non-null object
weight          398 non-null float64
acceleration    398 non-null float64
year            398 non-null int64
origin          398 non-null int64
name            398 non-null object
dtypes: float64(4), int64(3), object(2)
memory usage: 28.1+ KB
None
    mpg  cylinders  displacement horsepower  weight  acceleration  year  \
0  18.0          8         307.0      130.0  3504.0          12.0    70   
1  15.0          8         350.0      165.0  3693.0          11.5    70   
2  18.0          8         318.0      150.0  3436.0          11.0    70   
3  16.0          8         304.0      150.0  3433.0          12.0    70   
4  17.0          8         302.0      140.0  3449.0          10.5    70   

   origin                       name  
0       1  chevrolet chevelle malibu  
1       1          buick skylark 320  
2       1         plymouth satellite  
3       1              amc rebel sst  
4       1                ford torino  
DataFrame Shape: (398, 9)
      mpg  cylinders  displacement horsepower  weight  acceleration  year  \
32   25.0          4          98.0          ?  2046.0          19.0    71   
126  21.0          6         200.0          ?  2875.0          17.0    74   
330  40.9          4          85.0          ?  1835.0          17.3    80   
336  23.6          4         140.0          ?  2905.0          14.3    80   
354  34.5          4         100.0          ?  2320.0          15.8    81   
374  23.0          4         151.0          ?  3035.0          20.5    82   

     origin                  name  
32        1            ford pinto  
126       1         ford maverick  
330       2  renault lecar deluxe  
336       1    ford mustang cobra  
354       2           renault 18i  
374       1        amc concord dl  
      mpg  cylinders  displacement horsepower  weight  acceleration  year  \
32   25.0          4          98.0        NaN  2046.0          19.0    71   
126  21.0          6         200.0        NaN  2875.0          17.0    74   
330  40.9          4          85.0        NaN  1835.0          17.3    80   
336  23.6          4         140.0        NaN  2905.0          14.3    80   
354  34.5          4         100.0        NaN  2320.0          15.8    81   
374  23.0          4         151.0        NaN  3035.0          20.5    82   

     origin                  name  
32        1            ford pinto  
126       1         ford maverick  
330       2  renault lecar deluxe  
336       1    ford mustang cobra  
354       2           renault 18i  
374       1        amc concord dl  
New DataFrame shape: (392, 9)
[ 104.46938776  104.46938776  104.46938776  104.46938776  104.46938776
  104.46938776]
(298, 8)
(100, 8)
1.0
The r-squared for our model: 1.0
'''
