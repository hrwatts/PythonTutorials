#Decision tree, RandomizedSearchCV on iris dataset
#python3 ~/Documents/pyfiles/iris3.py
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'

#imports
from sklearn import datasets
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.grid_search import RandomizedSearchCV
from sklearn.grid_search import GridSearchCV
import random
import numpy as np

#trying to keep this as replicable as possible
rnum = 40
np.random.seed(rnum)
random.seed(rnum)

#load data
iris = datasets.load_iris()

#basically this is mainly illustrating RandomizedSearchCV
#it selects parameters to use rather than trying every single possibility
#which is computational less expensive, but could miss the very best one
#decision trees have lots of params so it's easy to illustrate with it

#set up params to try
params_r = {'max_depth':[3, None],
	'max_features':randint(1,5),
	'min_samples_leaf':randint(1,9),
	'criterion':['gini','entropy']}

params_g = {'max_depth':[3, None],
	'max_features':np.arange(1,5),
	'min_samples_leaf':np.arange(1,9),
	'criterion':['gini','entropy']}

#instantiate our tree
tree = DecisionTreeClassifier(random_state=rnum)

#set up our search grids
tree_rcv = RandomizedSearchCV(tree, params_r, cv=5)
tree_gcv = GridSearchCV(tree, params_g, cv=5)

#fit our models
tree_gcv.fit(iris.data, iris.target)
tree_rcv.fit(iris.data, iris.target)

#see the results
print('Random Tuned Decision Tree Parameters: \n'+str(tree_rcv.best_params_))
print('Random Best Score is: '+str(tree_rcv.best_score_))
print('Full Tuned Decision Tree Parameters: \n'+str(tree_gcv.best_params_))
print('Full Best Score is: '+str(tree_gcv.best_score_))

#alright, so after trying to make the console output the same everythime,
#here is output to console (dictionaries are unordered)
'''
Random Tuned Decision Tree Parameters: 
{'max_features': 2, 'max_depth': None, 'min_samples_leaf': 1, 'criterion': 'entropy'}
Random Best Score is: 0.966666666667
Full Tuned Decision Tree Parameters: 
{'max_features': 4, 'max_depth': 3, 'min_samples_leaf': 1, 'criterion': 'gini'}
Full Best Score is: 0.973333333333
'''
