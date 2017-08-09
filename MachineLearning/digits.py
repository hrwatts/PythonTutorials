#machine learning with digits dataset!
#python3 ~/Documents/pyfiles/digits.py
#which by the way, is just the absolute file path of digits.py on my computer
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
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#let's load our dataset which is already available from sklearn
digits = datasets.load_digits()

#what's in digits?
print("Digits keys: " +str(digits.keys()))

#data and images are essentially the exact same thing
print("Shape of data: "+str(digits.data.shape))
print("Type of data: "+ str(type(digits.data)))
print("Shape of images: "+str(digits.images.shape))
print("Type of images: "+ str(type(digits.data)))

#alright, now lets split our data into X (features) and y (target) for train and test
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=21, stratify=digits.target)

#set K in our KNN Classifier model
knn = KNeighborsClassifier(n_neighbors=8)

#fit our model to our training set
knn.fit(X_train, y_train)

#predict the labels of our testing set
prediction = knn.predict(X_test)

#how does our model fair?
score = round(knn.score(X_test, y_test)*100,2)
print("Our model scored: " + str(score) + "% with k equal to 8")

#but what about underfitting and overfitting data? We should use the ideal number
#to figure this out without knowing mathmatically, we will just use computer to
#run through a number of possibilities

#create the range for which you want to try values of k
neighbors=np.arange(1,9)

#let's check what we just made
print("Range for k: " + str(neighbors))

#we want an easy way to look at all the values at once, so we will plot it
#we will make some empty arrays to store values for the axises
train_accuracy = np.empty(len(neighbors)) 
test_accuracy = np.empty(len(neighbors))

for index, k in enumerate(neighbors):
	#we want to cycle through k values we made in neighbors
	knn = KNeighborsClassifier(n_neighbors=k)
	
	#fitting data again
	knn.fit(X_train, y_train)

	#store our testing and training scores in the arrays we made
	train_accuracy[index] = knn.score(X_train, y_train)
	test_accuracy[index] = knn.score(X_test, y_test)

#lets plot our results!
#title plot for awesomeness
plt.title("Various values for k")

#basically (x-axis, y-axis, legend-stuff)
plt.plot(neighbors, test_accuracy, label='Test Accuarcy')
plt.plot(neighbors, train_accuracy, label ='Train Accuracy')

#tell it to show the legend
plt.legend()

#give axises names
plt.xlabel('Value for K (# neighbors)')
plt.ylabel('Accuracy')

#always remember to display your plot
plt.show()

#and now you can see what the effects of changing the number of neighbors
#in k-NN does, and what is the best one
#generally, you'd want to get the middle sweet spot that ignores wobbles of accuracies
#so in this case, 3 or 7. 1 is normally a terrible idea.
#here is what the output to console should be
'''
Digits keys: dict_keys(['DESCR', 'images', 'target', 'data', 'target_names'])
Shape of data: (1797, 64)
Type of data: <class 'numpy.ndarray'>
Shape of images: (1797, 8, 8)
Type of images: <class 'numpy.ndarray'>
Our model scored: 97.78% with k equal to 8
Range for k: [1 2 3 4 5 6 7 8]
'''
