#more machine learning with boston dataset!
#python3 ~/Documents/pyfiles/boston3.py
#which by the way, is just the absolute file path of boston3.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#this is a REGRESSION model but with more advanced features

#imports
#NOTE sklearn 0.17 (the one I have) has the train_test_split (and cross_val_score) function 
#inside the cross_validation package
#if using 0.18 (most current) do this:
#from sklearn.model_selection import train_test_split (also this for cross_val_score)
from sklearn import datasets
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.cross_validation import cross_val_score
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#we are going to explore the effects of a varying alpha on our models

#import boston dataset
boston = datasets.load_boston()

#create a Ridge Regression model, leave alpha blank (auto 0)
r = Ridge(normalize=True)

#create an array for which you want to cycle through alpha (between 0 and 1)
alpha = np.arange(0,1.1,0.1)
print("Alpha Range: "+str(alpha))

#make some empty lists to store results in
#one for mean and the other for standard deviation
r_mean_l=[]
r_std_l=[]

#now for each alpha run a 10-fold CV and gather meaninful statistics
#storing each one in the relevant list
for a in alpha:
	#set alpha in model
	r.alpha = a
	
	#run 10-fold cross validatin
	r_cv = cross_val_score(r, boston.data, boston.target, cv=10)

	#put the statistical results in the lists
	r_mean_l.append(np.mean(r_cv))
	r_std_l.append(np.std(r_cv))

#print some results
r_mean = np.array(r_mean_l)
r_std = np.array(r_std_l)
print("CV Mean: " + str(np.round(r_mean, 2)))
print("CV Standard Deviation: " + str(np.round(r_std, 2)))

#visualize the results
plt.plot(alpha, r_mean, 'r', linewidth=2)
plt.fill_between(alpha, r_mean-r_std, r_mean+r_std, alpha=.3)
plt.ylabel('CV r squared values')
plt.xlabel('Alpha')
plt.axhline(c='k', ls='--')
plt.show()

#I wish I could be more confident about the values that are coming out of
#our cross validation. I'd think they'd be higher than that

#anyways here is the output to console
'''
Alpha Range: [ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1. ]
CV Mean: [ 0.2   0.33  0.36  0.36  0.36  0.35  0.34  0.32  0.31  0.29  0.27]
CV Standard Deviation: [ 0.6   0.45  0.39  0.35  0.33  0.31  0.29  0.28  0.27  0.27  0.27]
'''
