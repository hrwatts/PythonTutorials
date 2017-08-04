#iris machine learning testing
#to use go to terminal and type:
#python3 ~/Documents/pyfiles/iris.py
#which by the way, is just the absolute file path of iris.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'

#needed imports for this exercise
#if you don't have any of these, install them
#keyword for what you need to install is on the left-hand side
#if using Ubuntu, it's easy
#sudo apt install python3-PACKAGE_TO_INSTALL
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#making my plot look good by using an industry standard plotting theme
plt.style.use('ggplot')

#load the tutorial dataset included in sklearn, it's pre-made for testing
iris = datasets.load_iris()

#just a little fun title
print("[PRINT1] This is iris.py!")

#just looking at the type of iris
print("[PRINT2] iris variable datatype: "+str(type(iris)))

#its a 'Bunch'! Which is kinda like a dictionary. So let's print the keys
print("[PRINT3] iris var keys: " + str(iris.keys()))

#Most important are the 'data' which is our features/columns/independent variables
#and the 'target' which is the target/dependent variable.
#so what are their types?
print("[PRINT4] the type of 'data' inside iris: "+str(type(iris.data)))
print("[PRINT5] the type of 'target' inside iris: "+str(type(iris.target)))

#you see they are both numpy arrays!
#let's take a look into the shape of 'data' the one we will work with most
print("[PRINT6] iris.data.shape: "+str(iris.data.shape))

#it's (150,4) meaning their are 4 features/columns, and 150 rows/entries or data points

#what about the target?
print("[PRINT7] iris.target.shape: " + str(iris.target.shape))

#it's (150,)... what does that mean?
#basically it's just a single dimensional array with 150 values
#so? what else? well lets print the whole thing
print("[PRINT8] iris.target: \n" + str(iris.target))

#it seems 'target' is made up of 0s, 1s, and 2s... and what does that mean?
#let's see about 'target_names'
print("[PRINT9] iris.target_names: " + str(iris.target_names))

#so it has 3 values, 'setosa', 'versicolor', and 'virginica'
#these coorespond to the 0,1,2 in 'target'. 
#you'd know this of course, if you looked at the documentation
#here: help(datasets.load_iris)
#press q to exit help... it's tricky sometimes

#or it's actually included in the dataset itself. How helpful!
print("[PRINT10] iris.DESCR to follow... \n" + str(iris.DESCR) + "\n[PRINT10e] End iris.DESCR")

#now it's time to do some EDA
#or Exploratory Data Analysis
#which basically means we need to have a look at what we are working with

#let's start by simplifying things
#X will by our independent variables
X=iris.data

#y will be our dependent variable
y=iris.target

#load this mess of a 'Bunch' into a pandas dataframe
#so what is about to happend is:
#a dataframe will be made with the features in iris.data
#and the names of the columns will be imported from iris.feature_names
df = pd.DataFrame(X, columns=iris.feature_names)

#it's easy to get a brief insight by looking at the first 5 entries using the head() method
print("[PRINT11] 1st five entries of the dataframe:\n"+str(df.head()))

#now how about visual EDA?
#we are about to use a complex pandas scatter matrix, so follow closely...
#df is obviously needed cause we want to visualize that
#c is color, c=y since we want it colored by their species, y=iris.target
#figsize, we pass it a list that says how big we want the figure, 8x8 is medium sized
#s=150, s is the 'marker size', so we tell it how many points to use
#marker is the shape of the marker, defualt is '.' but you can make it a diamond with 'D'
pd.scatter_matrix(df, c=y, figsize=[8,8], s=145, marker='D')

#but... where's my scatter matrix?
#silly, always use plt.show()!
#plt.show()
#01324-1834813-481-834-18431-4838418481746583462347564578262758674875845687458675489267

#be careful! make sure to exit out of the plot before giving more commands in the console

#honestly this looks like too much info
#but hey! check out petal length and petal width intersection
#there's a strong coorelation!
#that's about all you'll get unless you understand what your looking at
#ie, you know statistics
#but at least we have an understanding of the structure of the data we have

#MACHINE LEARNING-------------------------------------------------------------
#I wanna do machine learning!
#well, you'll need to import something first!
#I already did at the top
#from sklearn.neighbors import KNeighborsClassifier
#This allows us access to K-Nearest Neighbors
#basically datapoints get a label based on the labels of nearby points
#setting to 6 means it will use the 6 nearest points to decided based on majority rules
knn=KNeighborsClassifier(n_neighbors=6)

#due to limited real-world data that is reliable,
#let's split our data into a training and testing set using the same way as before
#X will be training, it has 145 of the original values
#also we change y cause we can't have missing values
#talk about some mess with these numpy arrays...
X = np.vstack((iris.data[1:75], iris.data[78:149]))
print("[PRINT12] shape of *new* X: "+str(X.shape))
y = np.concatenate((iris.target[1:75], iris.target[78:149]), axis=0)
print("[PRINT13] shape of *new* y: "+str(y.shape))

#X_test is testing, psuedo new data to use our model on, just 5 observations
X_test = np.vstack((iris.data[:1], iris.data[75:78], iris.data[149:]))
print("[PRINT14] shape of X_test: "+str(X_test.shape))

#store test data labels info for checking later
y_test = np.concatenate((iris.target[:1], iris.target[75:78], iris.target[149:]), axis=0)

#now let's 'fit' the model to the data. about to have tons of info dropped
#pass in features (remember X?) and the target (y=iris.target)
#features and target here MUST be numpy arrays or pandas dataframes.
#FEATURES must take on continous values, like numbers
#and the array of FEATURES must be so that each column is a feature, and each row a data point
#There can't be any missing values in these datasets
#TARGET should be a single column, with the same number of values as in the feature data
knn.fit(X,y)

#check out what it does by printing out the return
print("[PRINT15] knn setting during fit(): \n"+str(knn.fit(X, y)))

#to use the model to predict the label of our testing data
#use .predict() method on our new data. Make sure new features are structured the same as old
prediction = knn.predict(X_test)

#the results?
print("[PRINT16] real label:"+ str(y_test))
print("[PRINT17] predicted label: "+str(prediction))

#[0 1 1 2 2]? What does this mean?
for index, sel in enumerate(prediction):
	print("[PRINT(for-loop"+str(index)+")] prediction #"+str(index) + " is: "
	 + str(iris.target_names[sel]))
	print("[PRINT(for-loop"+str(index)+")] is the prediction correct?: "
	 + str(y_test[index]==sel))

#looks like our model predicted 4 out of 5 correctly, not bad!
#This is what the output should look like
'''
[PRINT1] This is iris.py!
[PRINT2] iris variable datatype: <class 'sklearn.datasets.base.Bunch'>
[PRINT3] iris var keys: dict_keys(['DESCR', 'target', 'target_names', 'data', 'feature_names'])
[PRINT4] the type of 'data' inside iris: <class 'numpy.ndarray'>
[PRINT5] the type of 'target' inside iris: <class 'numpy.ndarray'>
[PRINT6] iris.data.shape: (150, 4)
[PRINT7] iris.target.shape: (150,)
[PRINT8] iris.target: 
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
[PRINT9] iris.target_names: ['setosa' 'versicolor' 'virginica']
[PRINT10] iris.DESCR to follow... 
Iris Plants Database

Notes
-----
Data Set Characteristics:
    :Number of Instances: 150 (50 in each of three classes)
    :Number of Attributes: 4 numeric, predictive attributes and the class
    :Attribute Information:
        - sepal length in cm
        - sepal width in cm
        - petal length in cm
        - petal width in cm
        - class:
                - Iris-Setosa
                - Iris-Versicolour
                - Iris-Virginica
    :Summary Statistics:

    ============== ==== ==== ======= ===== ====================
                    Min  Max   Mean    SD   Class Correlation
    ============== ==== ==== ======= ===== ====================
    sepal length:   4.3  7.9   5.84   0.83    0.7826
    sepal width:    2.0  4.4   3.05   0.43   -0.4194
    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
    petal width:    0.1  2.5   1.20  0.76     0.9565  (high!)
    ============== ==== ==== ======= ===== ====================

    :Missing Attribute Values: None
    :Class Distribution: 33.3% for each of 3 classes.
    :Creator: R.A. Fisher
    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
    :Date: July, 1988

This is a copy of UCI ML iris datasets.
http://archive.ics.uci.edu/ml/datasets/Iris

The famous Iris database, first used by Sir R.A Fisher

This is perhaps the best known database to be found in the
pattern recognition literature.  Fisher's paper is a classic in the field and
is referenced frequently to this day.  (See Duda & Hart, for example.)  The
data set contains 3 classes of 50 instances each, where each class refers to a
type of iris plant.  One class is linearly separable from the other 2; the
latter are NOT linearly separable from each other.

References
----------
   - Fisher,R.A. "The use of multiple measurements in taxonomic problems"
     Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to
     Mathematical Statistics" (John Wiley, NY, 1950).
   - Duda,R.O., & Hart,P.E. (1973) Pattern Classification and Scene Analysis.
     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.
   - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System
     Structure and Classification Rule for Recognition in Partially Exposed
     Environments".  IEEE Transactions on Pattern Analysis and Machine
     Intelligence, Vol. PAMI-2, No. 1, 67-71.
   - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions
     on Information Theory, May 1972, 431-433.
   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II
     conceptual clustering system finds 3 classes in the data.
   - Many, many more ...

[PRINT10e] End iris.DESCR
[PRINT11] 1st five entries of the dataframe:
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
[PRINT12] shape of *new* X: (145, 4)
[PRINT13] shape of *new* y: (145,)
[PRINT14] shape of X_test: (5, 4)
[PRINT15] knn setting during fit(): 
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=6, p=2,
           weights='uniform')
[PRINT16] real label:[0 1 1 1 2]
[PRINT17] predicted label: [0 1 1 2 2]
[PRINT(for-loop0)] prediction #0 is: setosa
[PRINT(for-loop0)] is the prediction correct?: True
[PRINT(for-loop1)] prediction #1 is: versicolor
[PRINT(for-loop1)] is the prediction correct?: True
[PRINT(for-loop2)] prediction #2 is: versicolor
[PRINT(for-loop2)] is the prediction correct?: True
[PRINT(for-loop3)] prediction #3 is: virginica
[PRINT(for-loop3)] is the prediction correct?: False
[PRINT(for-loop4)] prediction #4 is: virginica
[PRINT(for-loop4)] is the prediction correct?: True
'''
