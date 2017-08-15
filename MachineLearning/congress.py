#machine learning with the 1984 Congressional Voting database
#this is help for advanced metrics in classification models
#coincidentally, it also helps with databases from the internet
#and organizing data
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/congress.py

#imports
import numpy as np
import pandas as pd
from urllib.request import urlopen
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

#download the database from the internet
raw_data = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')

#change the raw text data to a DataFrame so we can look at it better
df = pd.read_csv(raw_data, header=None)
print(df.head())

#by the way, what these columns represent is here
'''
1. Class Name: 2 (democrat, republican)
2. handicapped-infants: 2 (y,n)
3. water-project-cost-sharing: 2 (y,n)
4. adoption-of-the-budget-resolution: 2 (y,n)
5. physician-fee-freeze: 2 (y,n)
6. el-salvador-aid: 2 (y,n)
7. religious-groups-in-schools: 2 (y,n)
8. anti-satellite-test-ban: 2 (y,n)
9. aid-to-nicaraguan-contras: 2 (y,n)
10. mx-missile: 2 (y,n)
11. immigration: 2 (y,n)
12. synfuels-corporation-cutback: 2 (y,n)
13. education-spending: 2 (y,n)
14. superfund-right-to-sue: 2 (y,n)
15. crime: 2 (y,n)
16. duty-free-exports: 2 (y,n)
17. export-administration-act-south-africa: 2 (y,n)
'''

#let's change the data into something more workable
#extract the target
target = np.array(df.iloc[:,0])

#extract the features (note, I made sure to generate a whole new dataframe)
bad_data = pd.DataFrame(df.iloc[:,1:])

#change the features into something other than 'y' 'n' or '?'
#'?' is abstain, which for all intents and purposes is a 'no' vote
bad_data[bad_data=='y'] = 1
bad_data[bad_data!=1] = 0

#numpy arrays are better
data = np.array(bad_data)

#now we can start work on our model
#make the model
knn = KNeighborsClassifier(n_neighbors=8)

#split our data
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.4,
	random_state=42, stratify=target)

#fit the model
knn.fit(X_train, y_train)

#get the basic accuray of the model
score = round(100*knn.score(X_test, y_test), 2)

#what's the score?
print("Simple accuracy of our model is: "+str(score)+"%")

#now let's get some more advanced metrics

#make a prediction
y_pred = knn.predict(X_test)

#make a confusion matrix (check out picture)
cm = confusion_matrix(y_test, y_pred)

#what does it look like?
print('Confusion matrix of test predictions: \n'+str(cm))

#metrics without even trying
#get the metrics computed with the confusion matrix
cr = classification_report(y_test, y_pred)

#now we get the good metrics
print('Classification Report:\n'+str(cr))

#note that you don't have to specify a class of interest, because it does them all

#here is the output
'''
           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
0  republican  n  y  n  y  y  y  n  n  n  y  ?  y  y  y  n  y
1  republican  n  y  n  y  y  y  n  n  n  n  n  y  y  y  n  ?
2    democrat  ?  y  y  ?  y  y  n  n  n  n  y  n  y  y  n  n
3    democrat  n  y  y  n  ?  y  n  n  n  n  y  n  y  n  n  y
4    democrat  y  y  y  n  y  y  n  n  n  n  y  ?  y  y  y  y
Simple accuracy of our model is: 94.25%
Confusion matrix of test predictions: 
[[100   7]
 [  3  64]]
Classification Report:
             precision    recall  f1-score   support

   democrat       0.97      0.93      0.95       107
 republican       0.90      0.96      0.93        67

avg / total       0.94      0.94      0.94       174
'''
