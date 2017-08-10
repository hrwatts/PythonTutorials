#machine learning with the 1984 Congressional Voting database
#Logistic Regession training, Cross Validation Grid Search
#and organizing data
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/congress3.py

#imports
#NOTE sklearn 0.17 (the one I have) has the train_test_split function
#inside the cross_validation package
#also, GridSearchCV is in grid_search package in 0.17
#if using 0.18 (most current) do this:
#from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from urllib.request import urlopen
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#the same stuff from congress.py, just get the data and prepare it
raw_data = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')
df = pd.read_csv(raw_data, header=None)
target = np.array(df.iloc[:,0])
bad_data = pd.DataFrame(df.iloc[:,1:])
bad_data[bad_data=='y'] = 1
bad_data[bad_data!=1] = 0
data = np.array(bad_data)

print(df.head())

#alright, now let's start off with a single feature
#adoption of budget resolution, a fairly devisive vote
#print stuff to look at
d_feature = data[:,3]
budget = np.array(d_feature).reshape(-1,1)
print("Yes votes out of total: "+str(np.sum(budget))+'/'+str(len(budget)))
print("Number of Repulicans voting: "+str(np.sum(target=='republican')))
r_yes = np.sum(np.logical_and(target=='republican', d_feature==1))
d_yes = np.sum(np.logical_and(target!='republican', d_feature==1))
print("Republicans voting yes: "+str(r_yes))
print("Democrats voting yes: " + str(d_yes))

#we are going to use the grid search to find the very best value for C
#instantiate our model
logreg = LogisticRegression()

#make values of C we want to search over
#needs to be in a dictionatary
params = {'C':np.logspace(-5, 8, 20)}

#quickly, let's just look at the values the are using
print("Values for C in Grid SearchCV: \n"+str(params))

#so 20 spaced out values between .00001 and 100,000,000

#setup our GridSearchCV object with 5-fold cross validation
l_cv = GridSearchCV(logreg, params, cv=5)

#fit it to our data
l_cv.fit(budget, target)

#let's get the results
print('The best C in our grid: '+str(l_cv.best_params_))
print('The score of best C: '+str(l_cv.best_score_))

#well there you have it, 0.00001 is the best C to use in this case

#output to console
'''
           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
0  republican  0  1  0  1  1  1  0  0  0  1  0  1  1  1  0  1
1  republican  0  1  0  1  1  1  0  0  0  0  0  1  1  1  0  0
2    democrat  0  1  1  0  1  1  0  0  0  0  1  0  1  1  0  0
3    democrat  0  1  1  0  0  1  0  0  0  0  1  0  1  0  0  1
4    democrat  1  1  1  0  1  1  0  0  0  0  1  0  1  1  1  1
Yes votes out of total: 177/435
Number of Repulicans voting: 168
Republicans voting yes: 163
Democrats voting yes: 14
Values for C in Grid SearchCV: 
{'C': array([  1.00000000e-05,   4.83293024e-05,   2.33572147e-04,
         1.12883789e-03,   5.45559478e-03,   2.63665090e-02,
         1.27427499e-01,   6.15848211e-01,   2.97635144e+00,
         1.43844989e+01,   6.95192796e+01,   3.35981829e+02,
         1.62377674e+03,   7.84759970e+03,   3.79269019e+04,
         1.83298071e+05,   8.85866790e+05,   4.28133240e+06,
         2.06913808e+07,   1.00000000e+08])}
The best C in our grid: {'C': 1.0000000000000001e-05}
The score of best C: 0.95632183908
'''
