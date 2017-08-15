#iris data set
#preprocessing data, scaling, pipeline
#python3 ~/Documents/pyfiles/iris4.py
#which by the way, is just the absolute file path of iris.py on my computer
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'

#imports
from sklearn import datasets
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#load our dataset
iris = datasets.load_iris()

#let's explore our data really quick
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.info())
print(df.describe())
print("First values in iris: \n"+str(df.head()))

#now we will scale and center our data, with standardization
X_scaled = scale(iris.data)
print(pd.DataFrame(X_scaled).describe())

#now you can see they all have the same standard deviation

#let's wrap everything up into a pipeline
steps=[('scaler',StandardScaler()),('knn',KNeighborsClassifier(n_neighbors=6))]
pipeline=Pipeline(steps)

#training and testing data
X_train, X_test, y_train,y_test = train_test_split(iris.data,iris.target,test_size=.3, random_state=42)

#fit data
pipeline.fit(X_train,y_train)

#predict
y_pred = pipeline.predict(X_test)

#score
score=round(100*pipeline.score(X_test,y_test), 2)
manual=round(100*np.sum(y_test==y_pred)/len(y_pred),2)

#results
print("Score Accuracy: "+str(score))
print("Manual Accuracy: "+str(manual))

#while I still feel like 100% accuracy is a totally useless model
#I can't actually find anything wrong with it
#output to console
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
sepal length (cm)    150 non-null float64
sepal width (cm)     150 non-null float64
petal length (cm)    150 non-null float64
petal width (cm)     150 non-null float64
dtypes: float64(4)
memory usage: 4.8 KB
None
       sepal length (cm)  sepal width (cm)  petal length (cm)  \
count         150.000000        150.000000         150.000000   
mean            5.843333          3.054000           3.758667   
std             0.828066          0.433594           1.764420   
min             4.300000          2.000000           1.000000   
25%             5.100000          2.800000           1.600000   
50%             5.800000          3.000000           4.350000   
75%             6.400000          3.300000           5.100000   
max             7.900000          4.400000           6.900000   

       petal width (cm)  
count        150.000000  
mean           1.198667  
std            0.763161  
min            0.100000  
25%            0.300000  
50%            1.300000  
75%            1.800000  
max            2.500000  
First values in iris: 
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
                  0             1             2             3
count  1.500000e+02  1.500000e+02  1.500000e+02  1.500000e+02
mean  -1.468455e-15 -1.657933e-15 -1.515825e-15 -8.052818e-16
std    1.003350e+00  1.003350e+00  1.003350e+00  1.003350e+00
min   -1.870024e+00 -2.438987e+00 -1.568735e+00 -1.444450e+00
25%   -9.006812e-01 -5.877635e-01 -1.227541e+00 -1.181504e+00
50%   -5.250608e-02 -1.249576e-01  3.362659e-01  1.332259e-01
75%    6.745011e-01  5.692513e-01  7.627586e-01  7.905908e-01
max    2.492019e+00  3.114684e+00  1.786341e+00  1.710902e+00
Score Accuracy: 100.0
Manual Accuracy: 100.0
'''
