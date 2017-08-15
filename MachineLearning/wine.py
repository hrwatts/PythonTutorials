#red wine dataset
#pre-prosessing raw data, scaling, pipeline, cross validation
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/wine.py

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

#download the database from the internet
raw_data = urlopen('https://assets.datacamp.com/production/course_1939/datasets/winequality-red.csv')

#change the raw text data to a DataFrame so we can look at it better
df = pd.read_csv(raw_data, sep=';')
print(df.info())
print(df.describe())
print(df.head())

#the target is quality, and while it seems to be on a continous scale, it's 
#an integer between 3 and 8 so that's concise enough to do kNN
#we are going to set the whole thing up in a pipeline and do cross validation grid search

#create pipeline
steps=[('scaler',StandardScaler()),('knn',KNeighborsClassifier())]
pipeline=Pipeline(steps)

#create grid search for pipeline with parameters
#NOTE for the pipeline how knn parameters are set with two underscores
parameters={'knn__n_neighbors':np.arange(1,50)}
cv=GridSearchCV(pipeline,param_grid=parameters)

#training testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('quality', axis=1), df.quality,
	test_size=.2, random_state=21)

#fit model to data
cv.fit(X_train, y_train)

#results
y_pred=cv.predict(X_test)
print("CV best Parameters: "+str(cv.best_params_))
print("CV Score: "+str(cv.score(X_test, y_test)))
print("Classification Report:\n"+str(classification_report(y_test,y_pred)))

#accuracy not so good here, but hey, quality is subjective and these aren't balanced
#classes, what do you expect?
#output to console
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1599 entries, 0 to 1598
Data columns (total 12 columns):
fixed acidity           1599 non-null float64
volatile acidity        1599 non-null float64
citric acid             1599 non-null float64
residual sugar          1599 non-null float64
chlorides               1599 non-null float64
free sulfur dioxide     1599 non-null float64
total sulfur dioxide    1599 non-null float64
density                 1599 non-null float64
pH                      1599 non-null float64
sulphates               1599 non-null float64
alcohol                 1599 non-null float64
quality                 1599 non-null int64
dtypes: float64(11), int64(1)
memory usage: 150.0 KB
None
       fixed acidity  volatile acidity  citric acid  residual sugar  \
count    1599.000000       1599.000000  1599.000000     1599.000000   
mean        8.319637          0.527821     0.270976        2.538806   
std         1.741096          0.179060     0.194801        1.409928   
min         4.600000          0.120000     0.000000        0.900000   
25%         7.100000          0.390000     0.090000        1.900000   
50%         7.900000          0.520000     0.260000        2.200000   
75%         9.200000          0.640000     0.420000        2.600000   
max        15.900000          1.580000     1.000000       15.500000   

         chlorides  free sulfur dioxide  total sulfur dioxide      density  \
count  1599.000000          1599.000000           1599.000000  1599.000000   
mean      0.087467            15.874922             46.467792     0.996747   
std       0.047065            10.460157             32.895324     0.001887   
min       0.012000             1.000000              6.000000     0.990070   
25%       0.070000             7.000000             22.000000     0.995600   
50%       0.079000            14.000000             38.000000     0.996750   
75%       0.090000            21.000000             62.000000     0.997835   
max       0.611000            72.000000            289.000000     1.003690   

                pH    sulphates      alcohol      quality  
count  1599.000000  1599.000000  1599.000000  1599.000000  
mean      3.311113     0.658149    10.422983     5.636023  
std       0.154386     0.169507     1.065668     0.807569  
min       2.740000     0.330000     8.400000     3.000000  
25%       3.210000     0.550000     9.500000     5.000000  
50%       3.310000     0.620000    10.200000     6.000000  
75%       3.400000     0.730000    11.100000     6.000000  
max       4.010000     2.000000    14.900000     8.000000  
   fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \
0            7.4              0.70         0.00             1.9      0.076   
1            7.8              0.88         0.00             2.6      0.098   
2            7.8              0.76         0.04             2.3      0.092   
3           11.2              0.28         0.56             1.9      0.075   
4            7.4              0.70         0.00             1.9      0.076   

   free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \
0                 11.0                  34.0   0.9978  3.51       0.56   
1                 25.0                  67.0   0.9968  3.20       0.68   
2                 15.0                  54.0   0.9970  3.26       0.65   
3                 17.0                  60.0   0.9980  3.16       0.58   
4                 11.0                  34.0   0.9978  3.51       0.56   

   alcohol  quality  
0      9.4        5  
1      9.8        5  
2      9.8        5  
3      9.8        6  
4      9.4        5  
CV best Parameters: {'knn__n_neighbors': 1}
CV Score: 0.634375
Classification Report:
             precision    recall  f1-score   support

          3       0.00      0.00      0.00         1
          4       0.18      0.12      0.15        16
          5       0.66      0.72      0.69       127
          6       0.68      0.60      0.64       131
          7       0.63      0.69      0.66        42
          8       0.25      0.33      0.29         3

avg / total       0.63      0.63      0.63       320
'''
