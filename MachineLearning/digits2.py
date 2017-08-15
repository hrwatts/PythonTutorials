#machine learning with digits dataset!
#python3 ~/Documents/pyfiles/digits2.py
#which by the way, is just the absolute file path of digits2.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#this file shows off Cross Validation Grid Search, a way to efficiently choose
#hpyerparameters

#imports
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#let's load our dataset which is already available from sklearn
digits = datasets.load_digits()

#instantiate a blank (defualt) model
knn = KNeighborsClassifier()

#create a dictionary for hyperparameters you want to cycle through
param_grid = {'n_neighbors':np.arange(1,10)}

#set up the grid search
knn_cv = GridSearchCV(knn, param_grid, cv=5)

#fit the grid search to the data
knn_cv.fit(digits.data, digits.target)

#check out what the results are
#score is mean cross validation score over the fold
print('The best parameter in our grid: '+str(knn_cv.best_params_))
print('The score of best parameter: '+str(knn_cv.best_score_))

#output to console
'''
The best parameter in our grid: {'n_neighbors': 2}
The score of best parameter: 0.966611018364
'''
