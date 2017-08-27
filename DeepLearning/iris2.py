#more advanced ways of optimizing, early stopping, validation
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/iris2.py

#imports
#also, I set the random seed so that the console output is reproducable
import numpy as np
np.random.seed(16)
from sklearn import datasets
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping

#same as before, get data and prepare it
iris = datasets.load_iris()
X = iris.data
y=to_categorical(iris.target)

#get info for building input layer
n_cols = X.shape[1]

#make model systematocally because we will want to change things
def get_model(in_layer_shape):
	model = Sequential()
	model.add(Dense(64, activation='relu', input_shape=(in_layer_shape,)))
	model.add(Dense(32, activation='relu'))
	model.add(Dense(3, activation='softmax'))
	return model

#we will be working with different learning rates to see their effect on our model
learning_rates=[.000001,.01,1]

#we also want to stop training once we stop improving our validation loss
#to do this, we will create an early stopping monitor
#that will stop fitting our data over epochs after the validation loss stops improving
#this is done with the argument patience=# which tells it how many epochs to wait
#before stopping 2 or 3 is common, more than 3 very, very rare
monitor = EarlyStopping(patience=2)

#iterate over the learning rate and compile and fit the model for each one
for iteration,rate in enumerate(learning_rates):
	print('Iteration: '+str(iteration+1) + " with learning rate: "+str(rate))
	model = get_model(n_cols)
	my_optimizer = SGD(lr=rate)
	model.compile(optimizer=my_optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
	#add callbacks for the early stopping monitor
	#and since we have early stopping, we will go beyond
	#the defualt 10 for how many epochs to fit our data to
	model.fit(X, y, validation_split=.1, epochs=20, callbacks=[monitor])

#we can see that the small learning rate goes through all the epochs since
#it keeps imporving, but it doesn't do it fast enough to make it really
#useful, and the high learning rate becomes useless very quickly

#output to console
'''
Using TensorFlow backend.
Iteration: 1 with learning rate: 1e-06
Train on 135 samples, validate on 15 samples
Epoch 1/20
135/135 [==============================] - 0s - loss: 1.1052 - acc: 0.3704 - val_loss: 1.2015 - val_acc: 0.0000e+00
Epoch 2/20
135/135 [==============================] - 0s - loss: 1.1051 - acc: 0.3704 - val_loss: 1.2014 - val_acc: 0.0000e+00
Epoch 3/20
135/135 [==============================] - 0s - loss: 1.1051 - acc: 0.3704 - val_loss: 1.2013 - val_acc: 0.0000e+00
Epoch 4/20
135/135 [==============================] - 0s - loss: 1.1051 - acc: 0.3704 - val_loss: 1.2012 - val_acc: 0.0000e+00
Epoch 5/20
135/135 [==============================] - 0s - loss: 1.1050 - acc: 0.3704 - val_loss: 1.2011 - val_acc: 0.0000e+00
Epoch 6/20
135/135 [==============================] - 0s - loss: 1.1050 - acc: 0.3704 - val_loss: 1.2010 - val_acc: 0.0000e+00
Epoch 7/20
135/135 [==============================] - 0s - loss: 1.1049 - acc: 0.3704 - val_loss: 1.2009 - val_acc: 0.0000e+00
Epoch 8/20
135/135 [==============================] - 0s - loss: 1.1049 - acc: 0.3704 - val_loss: 1.2008 - val_acc: 0.0000e+00
Epoch 9/20
135/135 [==============================] - 0s - loss: 1.1048 - acc: 0.3704 - val_loss: 1.2007 - val_acc: 0.0000e+00
Epoch 10/20
135/135 [==============================] - 0s - loss: 1.1048 - acc: 0.3704 - val_loss: 1.2005 - val_acc: 0.0000e+00
Epoch 11/20
135/135 [==============================] - 0s - loss: 1.1047 - acc: 0.3704 - val_loss: 1.2005 - val_acc: 0.0000e+00
Epoch 12/20
135/135 [==============================] - 0s - loss: 1.1047 - acc: 0.3704 - val_loss: 1.2004 - val_acc: 0.0000e+00
Epoch 13/20
135/135 [==============================] - 0s - loss: 1.1046 - acc: 0.3704 - val_loss: 1.2003 - val_acc: 0.0000e+00
Epoch 14/20
135/135 [==============================] - 0s - loss: 1.1046 - acc: 0.3704 - val_loss: 1.2002 - val_acc: 0.0000e+00
Epoch 15/20
135/135 [==============================] - 0s - loss: 1.1046 - acc: 0.3704 - val_loss: 1.2001 - val_acc: 0.0000e+00
Epoch 16/20
135/135 [==============================] - 0s - loss: 1.1045 - acc: 0.3704 - val_loss: 1.2000 - val_acc: 0.0000e+00
Epoch 17/20
135/135 [==============================] - 0s - loss: 1.1045 - acc: 0.3704 - val_loss: 1.1999 - val_acc: 0.0000e+00
Epoch 18/20
135/135 [==============================] - 0s - loss: 1.1044 - acc: 0.3704 - val_loss: 1.1998 - val_acc: 0.0000e+00
Epoch 19/20
135/135 [==============================] - 0s - loss: 1.1044 - acc: 0.3704 - val_loss: 1.1997 - val_acc: 0.0000e+00
Epoch 20/20
135/135 [==============================] - 0s - loss: 1.1043 - acc: 0.3704 - val_loss: 1.1996 - val_acc: 0.0000e+00
Iteration: 2 with learning rate: 0.01
Train on 135 samples, validate on 15 samples
Epoch 1/20
135/135 [==============================] - 0s - loss: 1.3588 - acc: 0.2593 - val_loss: 1.1211 - val_acc: 0.0000e+00
Epoch 2/20
135/135 [==============================] - 0s - loss: 1.0114 - acc: 0.4296 - val_loss: 1.0590 - val_acc: 0.7333
Epoch 3/20
135/135 [==============================] - 0s - loss: 0.9491 - acc: 0.6667 - val_loss: 0.8433 - val_acc: 1.0000
Epoch 4/20
135/135 [==============================] - 0s - loss: 0.8897 - acc: 0.6444 - val_loss: 1.1292 - val_acc: 0.0000e+00
Epoch 5/20
135/135 [==============================] - 0s - loss: 0.8573 - acc: 0.7481 - val_loss: 0.8186 - val_acc: 0.8667
Epoch 6/20
135/135 [==============================] - 0s - loss: 0.8112 - acc: 0.7852 - val_loss: 0.6193 - val_acc: 1.0000
Epoch 7/20
135/135 [==============================] - 0s - loss: 0.7798 - acc: 0.7185 - val_loss: 0.8716 - val_acc: 0.5333
Epoch 8/20
135/135 [==============================] - 0s - loss: 0.7452 - acc: 0.7778 - val_loss: 1.0275 - val_acc: 0.0000e+00
Epoch 9/20
135/135 [==============================] - 0s - loss: 0.7201 - acc: 0.7481 - val_loss: 0.7253 - val_acc: 1.0000
Iteration: 3 with learning rate: 1
Train on 135 samples, validate on 15 samples
Epoch 1/20
135/135 [==============================] - 0s - loss: 8.3303 - acc: 0.3481 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 2/20
135/135 [==============================] - 0s - loss: 11.9393 - acc: 0.2593 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 3/20
135/135 [==============================] - 0s - loss: 11.9393 - acc: 0.2593 - val_loss: 1.1921e-07 - val_acc: 1.0000
Epoch 4/20
135/135 [==============================] - 0s - loss: 11.9393 - acc: 0.2593 - val_loss: 1.1921e-07 - val_acc: 1.0000
'''
