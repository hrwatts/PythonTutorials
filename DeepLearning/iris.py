#building neural network with keras and tensorflow for classification
#basics of model use, saving/loading
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/iris.py

#imports
#NOTE: also install h5py
#also, I set the random seed so that the console output is reproducable
import pandas as pd
import numpy as np
np.random.seed(16)
from sklearn import datasets
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.models import load_model

#let's get our data ready
iris = datasets.load_iris()

#you really need to pay attention in classification
#problems, each possible class needs to be in a binary column
#ie 1=in class, 0=not in class
y=to_categorical(iris.target)
print(y[0], y[50], y[120])

X = iris.data

#train test split your data
X_train, X_test, y_train, y_test = train_test_split(X,y,
	test_size=0.05,random_state=42,stratify=y)

#get the number of input nodes per observation (number of features)
n_cols = X.shape[1]

#instantiate our model
model = Sequential()

#add the first layer
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))

#add another layer
model.add(Dense(100, activation='relu'))

#output layer (3 nodes for 3 possible outputs)
#classification commonly uses 'softmax' activation function
#softmax ensures that the predictions sum to 1 so they can be intepreted better
model.add(Dense(3, activation='softmax'))

#choose optimizer and loss function
#classification 'categorical_crossentropy' is common
#you can also specify the output during fitting into easier to understand metrics
#in classification you can use metrics=['accuracy'] argument
#sdg is stochiastic gradient decent
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

#fit our model to the training data
model.fit(X_train, y_train)

#why not go ahead and save our model?
#.h5 is the common extension
#NOTE: while you don't need to import it
#h5py is a required package to do this
model.save('iris.h5')

#demonstrate loading model
iris_model = load_model('iris.h5')

#let's verify that this model is indeed the same
print(model.summary())
print(iris_model.summary())

#make a prediction
pred=iris_model.predict(X_test)

#do some work preparing this for display
total=0
for index,row in enumerate(pred):
	row[row==max(row)]=1
	row[row!=1]=0
	if (row==y_test[index]).sum()==3:
		total+=1
print('Accuracy: '+str(total/len(pred)))

#output to console
'''
Using TensorFlow backend.
[ 1.  0.  0.] [ 0.  1.  0.] [ 0.  0.  1.]
Epoch 1/10
142/142 [==============================] - 0s - loss: 1.1159 - acc: 0.3521     
Epoch 2/10
142/142 [==============================] - 0s - loss: 1.0076 - acc: 0.3380     
Epoch 3/10
142/142 [==============================] - 0s - loss: 0.9669 - acc: 0.6127     
Epoch 4/10
142/142 [==============================] - 0s - loss: 0.9174 - acc: 0.6761     
Epoch 5/10
142/142 [==============================] - 0s - loss: 0.8743 - acc: 0.7183     
Epoch 6/10
142/142 [==============================] - 0s - loss: 0.8397 - acc: 0.7746     
Epoch 7/10
142/142 [==============================] - 0s - loss: 0.8228 - acc: 0.6761     
Epoch 8/10
142/142 [==============================] - 0s - loss: 0.7843 - acc: 0.7394     
Epoch 9/10
142/142 [==============================] - 0s - loss: 0.7553 - acc: 0.7746     
Epoch 10/10
142/142 [==============================] - 0s - loss: 0.7303 - acc: 0.7254     
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 100)               500       
_________________________________________________________________
dense_2 (Dense)              (None, 100)               10100     
_________________________________________________________________
dense_3 (Dense)              (None, 3)                 303       
=================================================================
Total params: 10,903
Trainable params: 10,903
Non-trainable params: 0
_________________________________________________________________
None
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 100)               500       
_________________________________________________________________
dense_2 (Dense)              (None, 100)               10100     
_________________________________________________________________
dense_3 (Dense)              (None, 3)                 303       
=================================================================
Total params: 10,903
Trainable params: 10,903
Non-trainable params: 0
_________________________________________________________________
None
Accuracy: 0.875
'''
