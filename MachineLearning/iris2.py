#iris machine learning testing, part 2
#to use go to terminal and type:
#python3 ~/Documents/pyfiles/iris2.py
#which by the way, is just the absolute file path of iris.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'

#imports
#NOTE sklearn 0.17 (the one I have) has the train_test_split function
#inside the cross_validation package
#if using 0.18 (most current) do this:
#from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#fancy plotting setting
plt.style.use('ggplot')

#set everything up like in iris.py
iris = datasets.load_iris()
X=iris.data
y=iris.target
df = pd.DataFrame(X, columns=iris.feature_names)

#remember X is features and y is labels
#now we will split data into 2 sets, train and test
#X and y because those are the features and labels you want to split
#test_size is how much you want to become the test data versus train data, 25% is standard
#random state is the random seed. Basically you want it to be random, but reproducable
#use stratify=y (list containing labels) to let it know you want a good distribution of labels
#otherwise it be dumb if it was predicting the same outcome every time
#it's gonna return 4 variables in said order
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3, random_state=21, stratify=y)

#let's set it to 8 this time
knn=KNeighborsClassifier(n_neighbors=8 )

#fit model to our training data
knn.fit(X_train, y_train)

#make predictions of out test data
prediction = knn.predict(X_test)

#figure out the accuracy by dividing correct predictions by total predictions
accuracy = round(100*np.sum(prediction==y_test)/len(y_test), 2)

#but you could do it way faster!
easy_acc = round(100*knn.score(X_test, y_test), 2)

#show results!
print("Your model has an accuracy of "+str(easy_acc)+ "%")

#This is a much better way, super simple compared to the first iris.py!
#since we keep the same random seed the output should be the same too
#the only thing this script prints is:
'''
Your model has an accuracy of 95.56%
'''
