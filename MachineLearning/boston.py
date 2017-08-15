#machine learning with boston dataset!
#python3 ~/Documents/pyfiles/boston.py
#which by the way, is just the absolute file path of boston.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#this is a REGRESSION model

#imports
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

boston_ds = datasets.load_boston()
#check out the keys in boston_ds
print("Keys for Boston dataset: "+str(boston_ds.keys()))

#to make this more workable, convert it to a pandas DataFrame
boston = pd.DataFrame(boston_ds.data, columns=boston_ds.feature_names)

#let's take a look at boston
print(boston.head())

#NOTE the target (Median Value of owner occupied homes) is not included here

#but what does this mean? Let's consult the DESCR
print(boston_ds.DESCR[270:1195])

#in order to make this work we will need to split this into features and targets
#and they need to be numpy arrays!
#X will be all our features (any dimension)
#y will be all our target (single dimension)
X = boston_ds.data
y = boston_ds.target

#first, we will try and predict the target using only one feature
#it's important to consider that not all features will be relevant
#when predicting a target. For value of dwellings, lets consider 
#the number of rooms only this time
X_rooms = X[:, 5]

#we may wish to visualize the data we are about to work with
#we will need to reshape them to look like 1d vectors for plotting
X_rooms = X_rooms.reshape(-1,1)
y = y.reshape(-1,1)

#let's plot
plt.scatter(X_rooms, y)
plt.ylabel("Median value of owner-occupied homes in $1000's")
plt.xlabel("average number of rooms per dwelling")
plt.show()
plt.clf()

#now let's try predicting using a linear model (regression)
reg = linear_model.LinearRegression()

#fit the data
reg.fit(X_rooms, y)

#since this is a linear model, the prediction should follow a line
#basically, we can visualize this line by starting at the smallest value
#and plotting to the largest since we only have 1 feature here
prediction_space = np.linspace(min(X_rooms),max(X_rooms)).reshape(-1,1)

#let's overlay this line onto our data to see our results
plt.scatter(X_rooms, y, color='blue')
plt.plot(prediction_space, reg.predict(prediction_space), color='black', linewidth=3)
plt.ylabel("Median value of owner-occupied homes in $1000's")
plt.xlabel("average number of rooms per dwelling")
plt.show()

#now let's fit the model to the entire dataset, containing a total of 9 features
#we will also split the data into testing and training sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#make a new model
reg_all = linear_model.LinearRegression()

#fit the data using the training set
reg_all.fit(X_train, y_train)

#let's see our accuracy
score = round(100*reg_all.score(X_test, y_test),2)
print("Accuracy for the model is: "+str(score) + "%")

#now this is just a helpful thing to learn how to use sklearn linear models
#normally you wouldn't apply linear regression exactly like this to achieve 
#desired results. Normally you'd regularize them first.

#here is the output
'''
Keys for Boston dataset: dict_keys(['target', 'data', 'feature_names', 'DESCR'])
      CRIM  ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD  TAX  PTRATIO  \
0  0.00632  18   2.31     0  0.538  6.575  65.2  4.0900    1  296     15.3   
1  0.02731   0   7.07     0  0.469  6.421  78.9  4.9671    2  242     17.8   
2  0.02729   0   7.07     0  0.469  7.185  61.1  4.9671    2  242     17.8   
3  0.03237   0   2.18     0  0.458  6.998  45.8  6.0622    3  222     18.7   
4  0.06905   0   2.18     0  0.458  7.147  54.2  6.0622    3  222     18.7   

        B  LSTAT  
0  396.90   4.98  
1  396.90   9.14  
2  392.83   4.03  
3  394.63   2.94  
4  396.90   5.33  
  - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

Accuracy for the model is: 71.09%
'''
