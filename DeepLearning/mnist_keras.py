#keras classifier for images
#python3 mnist_keras.py

import pandas as pd
import numpy as np
np.random.seed(16) #so it can be replicated

#just cause I'm lazy I am pulling from some sklearn datasets and tools
from sklearn import datasets
from sklearn.model_selection import train_test_split

#but the real point is that Keras replaces your interface with tensorflow
#it uses tensorflow, so all that must still be install but this package is awesome
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.models import load_model

#load dataset
digits = datasets.load_digits()
X = digits.data
y = to_categorical(digits.target)
n_cols = X.shape[1]


#split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=21, stratify=y)
print(X_train.shape,y_train.shape)
#these few lines of easily readable code replaces dozens in tensorflow
model = Sequential()
model.add(Dense(24, activation='sigmoid', input_shape=(n_cols,)))
model.add(Dense(18, activation='sigmoid'))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50)
pred=model.predict(X_test)

#this is just to pred the data for display
index_pred =np.array([p.tolist().index(max(p)) for p in pred])
index_y =np.array([yy.tolist().index(1) for yy in y_test])
acc = np.equal(index_y,index_pred)
print("Accuracy on testing set:",round(sum(acc)/acc.shape[0],2))
