#machine learning with the 1984 Congressional Voting database
#Logistic Regession training, and ROC curves
#and organizing data
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/congress2.py

#imports
import numpy as np
import pandas as pd
from urllib.request import urlopen
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, confusion_matrix, classification_report
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
budget = np.array(data[:,3]).reshape(-1,1)
print("Yes votes out of total: "+str(np.sum(budget))+'/'+str(len(budget)))
print("Number of Repulicans voting: "+str(np.sum(target=='republican')))

#split our data
X_train, X_test, y_train, y_test = train_test_split(budget, target, test_size=0.4,
	random_state=42, stratify=target)

#instantiate our model
#the threshold is of great importance, but we really don't have enough info to set it
#more on thresholds later
logreg = LogisticRegression()

#NOTE Logistic Regression is actually used for binary classification

#fit our data
logreg.fit(X_train, y_train)

#make some predictions
y_pred = logreg.predict(X_test)

#get the confusion matrix and classification report
#see ConfusionMatrixMetrixs.png (picture) for info on what these mean
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)

#lets take a look
print('Confustion Matrix Defualt Threshold: \n'+str(cm))
print('Classification Report Defualt Threshold: \n'+str(cr))

#now we want to get our ROC curve for this
#Reciever Operating Characteristic Curve
#so basically we are plotting the effects of our threshold
#on the model

#get the prediction probability
#basically, logreg will generate a probabilty value
#that it weighs to be between 0, and 1
#either one class or the other
#the user determines where to draw the line
#and say what threshold between 0, and 1 to actually classify them
y_prob = logreg.predict_proba(X_test)

#now let's print some of it out and see what we got
print("Prediction probabilty: \n"+str(y_prob[:10,:]))

#you can see clearly that there are 2 columns for the 2 classes
#and it reasonably makes a good prediction, as there is only 
#2 different values observed
#but depending on where your threshold is
#you could be missing all the information the model is imparting

#we actually only need one column (probablity equal to 1, is in index 1)
y_pred_prob = y_prob[:,1]


#see confustion matrix (picture) for info on what these mean
#fpr is false positive rate
#tpr is true positive rate
#threshold is the p values for the curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob, pos_label = 'republican')

#on the ROC curve it's tpr/fpr
#now we plot
plt.plot([0,1],[0,1], 'k--')
plt.plot(fpr, tpr, label='Logistic Regression')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logic Regression ROC Curve')
plt.show()

#now we can see where the threshold might be best set
#you'd want to do this before setting a threshold

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
Prediction probabilty: 
[[ 0.12727806  0.87272194]
 [ 0.92865639  0.07134361]
 [ 0.92865639  0.07134361]
 [ 0.92865639  0.07134361]
 [ 0.92865639  0.07134361]
 [ 0.92865639  0.07134361]
 [ 0.92865639  0.07134361]
 [ 0.12727806  0.87272194]
 [ 0.92865639  0.07134361]
 [ 0.12727806  0.87272194]]
'''
