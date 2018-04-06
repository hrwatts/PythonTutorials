#don't do this
import warnings
warnings.filterwarnings("ignore")

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from sklearn import datasets
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential

#load the MNIST dataset of hand drawn numbers
digits = datasets.load_digits()
X = digits.data
y = to_categorical(digits.target)

#test numbers
test_numbers = []
for x in range(3):
    test_numbers.append(int(input("Enter a number below 1,797: ")))

#What does our data look like?
fig = plt.figure()
fig.suptitle("Handwritten Numbers")

img1 = np.reshape(X[test_numbers[0]],(8,8))
sp1 = plt.subplot(131)
sp1.set_title(str(np.argmax(y[test_numbers[0]])))
plt.imshow(img1)

img2 = np.reshape(X[test_numbers[1]],(8,8))
sp2 = plt.subplot(132)
sp2.set_title(str(np.argmax(y[test_numbers[1]])))
plt.imshow(img2)

img3 = np.reshape(X[test_numbers[2]],(8,8))
sp3 = plt.subplot(133)
sp3.set_title(str(np.argmax(y[test_numbers[2]])))
plt.imshow(img3)
plt.show()


#This is the entire code for the nueral net
input_columns = X.shape[1] #used for the input layer
out_columns = y.shape[1]   #used for the output layer
num_nodes = 24             #for convenience
model = Sequential()
model.add(Dense(num_nodes, activation='relu', input_shape=(input_columns,)))
model.add(Dense(int(num_nodes*0.75), activation='relu')) #hidden layer
model.add(Dense(out_columns, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=50, verbose=True)
#done!

#How did it do?
for num in test_numbers:
    pred = model.predict(np.reshape(X[num],(1,64)))
    print("Real Number:",np.argmax(y[num]),"Predicted:",np.argmax(pred))

'''
#test on my own handwriting!
seven = misc.imread("seven.bmp")
print(seven)
#misc.imresize(seven, )
'''
