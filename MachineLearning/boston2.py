#more machine learning with boston dataset!
#python3 ~/Documents/pyfiles/boston2.py
#which by the way, is just the absolute file path of boston2.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#this is a REGRESSION model but with more advanced features

#imports
#NOTE sklearn 0.17 (the one I have) has the train_test_split (and cross_val_score) function 
#inside the cross_validation package
#if using 0.18 (most current) do this:
#from sklearn.model_selection import train_test_split (also this for cross_val_score)
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import timeit

#we will be doing the same thing as in boston.py, except with cross validation

#load the dataset
boston = datasets.load_boston()

#split the data into a testing and training set
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target,
	test_size=0.3, random_state=42)

#generate our linear model
reg = LinearRegression()

#use cross_val_score to generate a 5-fold cross validation of our model
#what this does is it will compute the r^2 (the sum of the residual^2 of the OLS method)
#for each fold (out of k-folds) and places them in a k-sized numpy.array
cv_results = cross_val_score(reg, boston.data, boston.target, cv=5)

#let's see the results
print("The cross validation results: \n"+str(cv_results))

#but isn't the 5th value negative? uh, don't worry about that. 
#It just means the model ended up being very bad at predicting your data points
#for more info on that, go here
#https://stats.stackexchange.com/questions/183265/what-does-negative-r-squared-mean

#the cross validation helps us to understand the represendation of our data in our test_train_split
#with this, we can do some meaningful statistics
print("The mean of our cross validation array: "+str(np.mean(cv_results)))

#the better fit means you get a value closer to 1

#now let's try to regularize our model
#basically, with higher dimensions of features in our model 
#we will start to see problems of overfitting
#to solve this we will use regularization
#check out the pictures to see the difference between
#the LeanrModel calculations for OLS loss function
#and the additions using different regularization methods

#let's use Ridge Regression to regularize our data (see imports)
#alpha is the parameter we set to limit overfitting, if it is too high
#it will lead to underfitting
#normalize=True just means all our features will be on the same scale
ridge = Ridge(alpha=0.1, normalize=True)

#Ridge Regression works basically the exact same way that LinearRegression works
reg.fit(X_train, y_train)
ridge.fit(X_train, y_train)

#let's see how the score compares to LinearRegression model
reg_score = round(reg.score(X_test, y_test), 4)
ridge_score = round(ridge.score(X_test, y_test), 4)

print('Ridge Regression r-squared: '+str(ridge_score))
print('Linear Regression r-squared: '+str(reg_score))

#but there is also Lasso Regression (see imports)
#it uses a different formula to regularize data
lasso = Lasso(alpha=0.1, normalize=True)

#let's compare this one to LinearRegression
lasso.fit(X_train, y_train)
lasso_score =round(lasso.score(X_test, y_test), 4)
print('Lasso Regression r-squared: '+str(lasso_score))

#what is cool about Lasso Regression is that it tends to reduce the less important
#(for predicting) features' coefficients to zero.
#Regression Models use a line to predict data, recall math class a line is
# y=ax+b, y is the target, x is a feature, the model chooses an a and b
# for multi feature things it goes by this
# y=a1x1 + a2x2... +anxn +b 
# a's are coefficients for each feature
#what is important to know is that lasso will handle this for you
#and you can see how it does it and get important features that way

#so let's grab exactly what effect the lasso has on coefficients
#by grabbing the coefficients chosen to be used for the line
lasso_coef = lasso.fit(boston.data, boston.target).coef_

#this can also be done like this
l_cf = lasso.coef_

#and now to visualize what the effects are
plt.plot(range(len(boston.feature_names)), l_cf)
plt.xticks(range(len(boston.feature_names)), boston.feature_names, rotation = 60)
plt.ylabel("Coefficients")
plt.show()

#here we can clearly see that the most important feature for predicting
#the median value of a home is the number of rooms

#output to console
'''
The cross validation results: 
[ 0.63861069  0.71334432  0.58645134  0.07842495 -0.26312455]
The mean of our cross validation array: 0.350741350933
Ridge Regression r-squared: 0.6996
Linear Regression r-squared: 0.7109
Lasso Regression r-squared: 0.595
'''
