#cars mpg dataset
#pre-prosessing raw data, dummy variables
#made based on the class I got from DataCamp.com 'Supervised Learning with scikit-learn'
#python3 ~/Documents/pyfiles/cars.py

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

#download the database from the internet
raw_data = urlopen('https://assets.datacamp.com/production/course_1939/datasets/auto.csv')

#change the raw text data to a DataFrame so we can look at it better
df = pd.read_csv(raw_data)
print(df.head())

#Origin is a very useful feature, we dont want to get rid of it!
#as shown by this boxplot, it is helpful in predicting mpg
df.boxplot('mpg','origin', rot=60, grid=False)
plt.show()

#Data exploration is always the precurser to model building

#sklearn likes to use numerical values for everything, even catagorical variables
#so we are going to encode the 'origin' feature using dummy variables
#see picture on dummy variables for more info
df_origin = pd.get_dummies(df)
print(df_origin.head())

#you don't want duplicate data in your dataset wjen working with sklearn
#so we will need to get rid of one of the columns, as if it is 0 in the
#other 2 columns, it's implicitly the 3rd variable
df_origin = df_origin.drop('origin_Asia', axis=1)

#NOTE we could have done this with the drop_first argument in get_dummies()

#now that our data is ready, let's use it for ridge regression

#split data (the target is mpg)
X=df_origin.drop('mpg', axis=1)
y=df_origin.mpg
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

#instantiate model, and go ahead an fit it to data
ridge=Ridge(alpha=.5, normalize=True).fit(X_train, y_train)

#score it
score = ridge.score(X_test, y_test)

#view results
print("The resulting r-squared is: "+str(score))

#output to console
'''
    mpg  displ   hp  weight  accel  origin  size
0  18.0  250.0   88    3139   14.5      US  15.0
1   9.0  304.0  193    4732   18.5      US  20.0
2  36.1   91.0   60    1800   16.4    Asia  10.0
3  18.5  250.0   98    3525   19.0      US  15.0
4  34.3   97.0   78    2188   15.8  Europe  10.0
    mpg  displ   hp  weight  accel  size  origin_Asia  origin_Europe  \
0  18.0  250.0   88    3139   14.5  15.0            0              0   
1   9.0  304.0  193    4732   18.5  20.0            0              0   
2  36.1   91.0   60    1800   16.4  10.0            1              0   
3  18.5  250.0   98    3525   19.0  15.0            0              0   
4  34.3   97.0   78    2188   15.8  10.0            0              1   

   origin_US  
0          1  
1          1  
2          0  
3          1  
4          0  
The resulting score is: 0.719064519022
'''
