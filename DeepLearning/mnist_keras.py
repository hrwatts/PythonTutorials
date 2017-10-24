#keras classifier for images
#python3 mnist_keras.py

import pandas as pd
import numpy as np
np.random.seed(16) #so it can be replicated
from sklearn import datasets
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.models import load_model

#load dataset
digits = datasets.load_digits()
n_cols = digits.data.shape[1]

#split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=21, stratify=digits.target)


model = Sequential()
model.add(Dense(4, activation='relu', input_shape=(n_cols,)))
#model.add(Dense(12, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train)
pred=model.predict(X_test)
