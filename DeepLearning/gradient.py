#manual gradient decent
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/gradient.py

#imports
import numpy as np

#working with 2 simulated values from 2 hidden nodes to output layer
#target value is 6
input_data = np.array([3,4])
weights = np.array([1,2])
target=6

#learning rate is the modification applied to the slope to figure out
#how far in what direciton to move. Typically 0.01
learning_rate = 0.01

#calculate predictions
preds = (weights*input_data).sum()

#calculate the error (pred-actual)
error = preds-target
print('Error: '+str(error))

#now we will start gradient decent
gradient = 2 * input_data*error
print("Gradient (Slopes of tangents for error): "+str(gradient))

#the first value is the 1st weight calculated slope with respect to error
#second is the 2nd weight calculated slope with respect to error
#the word 'gradient' is a mathematical term for an array of slopes
#for mean-squared-error, the slope goes by this
#2 * x * (y-xb)
#x and b may have multiple numbers
#x is some vector for each datapoint
#b is some vector
#(y-xb) is the error

#update the weights
weights_up = weights - (learning_rate*gradient)
print("New Weights: "+str(weights_up))

#update predictions
preds_up = (weights_up*input_data).sum()
error_up = preds_up-target
print('Error 1st pass: '+str(error_up))

#let's do it again
gradient_up = 2 * input_data*error_up
print("New Gradient (Slopes of tangents for error): "+str(gradient_up))
weights_up = weights_up - (learning_rate*gradient_up)
print("New Weights: "+str(weights_up))
preds_up = (weights_up*input_data).sum()
error_up = preds_up-target
print('Error 2nd pass: '+str(error_up))

#and with each pass of gradient decent our model becomes more accurate

#output to console
'''
Error: 5
Gradient (Slopes of tangents for error): [30 40]
New Weights: [ 0.7  1.6]
Error 1st pass: 2.5
New Gradient (Slopes of tangents for error): [ 15.  20.]
New Weights: [ 0.55  1.4 ]
Error 2nd pass: 1.25
'''
