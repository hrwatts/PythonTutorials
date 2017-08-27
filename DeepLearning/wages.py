#building neural network with keras and tensorflow for regression
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/wages.py

#imports
#I set random seed to reproduce console output
import pandas as pd
import numpy as np
np.random.seed(16)
from urllib.request import urlopen
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential

#basically this is how to set up a neural network using keras
#there are many settings to build a keras model, this is just an example

#steps to building a keras model
#1: Specify Architecture
#2: Compile
#3: Fit
#4: Predict

#download the database from the internet
raw_data = urlopen('https://assets.datacamp.com/production/course_1975/datasets/hourly_wages.csv')

#read in the data that you want to use it on
#this allows us to give keras parameters for it's achitecture
df = pd.read_csv(raw_data)
predictors = df.drop('wage_per_hour', 1).as_matrix()
target = df['wage_per_hour'].as_matrix()
X_train, X_test, y_train, y_test = train_test_split(predictors,target,test_size=0.05,random_state=42)

#STEP 1--------------------------------------------------------------------------------

#here is the number of nodes we want to use for the input layer
#you always want to know the # of columns (features)
#input layer nodes stored as n_cols
n_cols = X_train.shape[1]

#there are 2 ways to build a model
#sequential is the easier way
#sequential means that the neural network has only set of weights
#going to deeper layers, from shallower layers.
model = Sequential()

#now we add layers to our model
#here we add the input layer (well actually the 1st hidden layer)
#Dense means that all the nodes in the previous layer, connect
#to all the nodes in the next layer
#here we add a Dense input layer, with relu activation function, and 100 nodes
#you must specify the input_shape on the input function
#the input shape here says that it has n_cols for columns and could have any number
#of rows or data points
model.add(Dense(100, activation='relu', input_shape = (n_cols,)))

#add another Dense hidden layer with relu activation function
model.add(Dense(100, activation='relu'))

#output layer (we are predicting 1 thing, so one output)
#also, the output layer has no activation function
model.add(Dense(1))

#STEP 2---------------------------------------------------------------------------------
#the next step is to compile the model
#what we are doing is setting up an efficient way for our model
#to do forward and back propagation
#you must specify the optimizer
#optimizer has many options and is mathmatically complex
#so just choose a versatile one, like 'adam' which adjusts the learning rate
#as it does gradient decent, to ensure reasonable values throughout the process
#you must also specify the loss function
#for regression problems, 'mean_squared_error' is common
model.compile(optimizer='adam', loss='mean_squared_error')

#STEP 3-------------------------------------------------------------------------------
#after you compile your model, it must be fit to the data
#which is a process of forward and back propagation to update the weights
#one thing to note, optimizers work best when you scale your data
#so they are relatively all the same value
#a common scaling process is subtract the mean and divide by standard deviation
#(feature - mean(feature))/std(feature)
model.fit(X_train, y_train)

#STEP 4------------------------------------------------------------------------------
#prediction is easy
pred = model.predict(X_test)

#now we will take a look at how we did
y_compare = np.reshape(y_test, [-1,1])
print('% error values: \n'+str(np.round(100*abs(pred-y_compare)/y_compare,decimals=2)))

#output to console
'''
Using TensorFlow backend.
Epoch 1/10
507/507 [==============================] - 0s - loss: 36.8251      
Epoch 2/10
507/507 [==============================] - 0s - loss: 24.1738     
Epoch 3/10
507/507 [==============================] - 0s - loss: 22.5636    
Epoch 4/10
507/507 [==============================] - 0s - loss: 21.4385     
Epoch 5/10
507/507 [==============================] - 0s - loss: 21.6213     
Epoch 6/10
507/507 [==============================] - 0s - loss: 20.7006     
Epoch 7/10
507/507 [==============================] - 0s - loss: 21.0582     
Epoch 8/10
507/507 [==============================] - 0s - loss: 21.5301     
Epoch 9/10
507/507 [==============================] - 0s - loss: 20.6970    
Epoch 10/10
507/507 [==============================] - 0s - loss: 20.5325     
% error values: 
[[  23.24]
 [  33.69]
 [  39.31]
 [  65.03]
 [   4.3 ]
 [  13.59]
 [  65.44]
 [  44.46]
 [  32.29]
 [  53.88]
 [  46.8 ]
 [   7.93]
 [  22.83]
 [  27.73]
 [  58.27]
 [  37.63]
 [  46.33]
 [  75.46]
 [ 113.61]
 [  61.15]
 [  17.48]
 [  38.  ]
 [  53.46]
 [ 119.16]
 [   1.17]
 [   8.58]
 [  51.43]]
'''
