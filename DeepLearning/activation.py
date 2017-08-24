#manual activation function with forward propagation, multilayer neural network
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/activation.py


#imports
import numpy as np

#same as before in forward.py
#input data, features 1 observation
input_data = np.array([2,3])

#same thing with weights
#each connection to a hidden node has it's own weight
weights = {'node_0': np.array([1,1]), 'node_1': np.array([-1,1]), 'output': np.array([2,-1])}
print(weights)

#the algorithm for caculating forward propagation is as follows
#(input val1 * weight val1) + (input val2, weight val2)
#EXCEPT
#this time we will use an activation function
#the s-function used to be useful, so we will use that here
#industry standard is now ReLU
#so activation functions are applied after the forward propagation
#into a layer of the hidden layer, so we will break it up into
#node input (forward prop), and node output (after activation function)
node_0_in = (input_data*weights['node_0']).sum()
node_0_out = np.tanh(node_0_in)

node_1_in = (input_data*weights['node_1']).sum()
node_1_out = np.tanh(node_1_in)

#for simplicity, we will hold the entire hidden layer in a variable
hidden_layer_vals = np.array([node_0_out, node_1_out])
print(hidden_layer_vals)

#to calculate to output layer, forward propagation is conintued since we only have
#1 hidden layer, and the activation function only applies to values in hidden nodes
output_val = (hidden_layer_vals*weights['output']).sum()
print(output_val)

#so we can see it is incridibly similar, just with a function applied inbetween on the
#hidden node values.

#we can also use the ReLU function, which is really basic
#essentially it just returns 0 if input is negative, or if positive returns the input
def relu(input):
	'''simulate Rectified Linear Activation Function'''
	output=max(input,0)
	return output

#redu some calculations
node_0_out = relu(node_0_in)
node_1_out = relu(node_1_in)
hidden_layer_vals = np.array([node_0_out, node_1_out])
output_val = (hidden_layer_vals*weights['output']).sum()
print(output_val)

#the calculations came out extremely different
#1... and 9 

#let's do a neural network two layers deep
#see multilayerNetwork.png for more info
#again with just 2 features, this time 3, and 5
input_data = np.array([3,5])

#weights
#since it's two layers deep it will have 4 hidden nodes
#naming is like binary
weights = {
'node_00': np.array([2,4]),
'node_01': np.array([4,-5]), 
'node_10': np.array([-1,1]),
'node_11': np.array([2,2]),
'output': np.array([-3,7])}

#first hidden layer
node_00_in = (input_data*weights['node_00']).sum()
node_00_out = relu(node_00_in)

node_01_in = (input_data*weights['node_01']).sum()
node_01_out = relu(node_01_in)

first_hidden = (node_00_out, node_01_out)

#apply 2nd hidden layer
node_10_in = (first_hidden*weights['node_10']).sum()
node_10_out = relu(node_10_in)

node_11_in = (first_hidden*weights['node_11']).sum()
node_11_out = relu(node_11_in)

sec_hidden = (node_10_out, node_11_out)

#output layer
output = (sec_hidden*weights['output']).sum()

#results
print(output)

#output to console
'''
{'output': array([ 2, -1]), 'node_0': array([1, 1]), 'node_1': array([-1,  1])}
[ 0.9999092   0.76159416]
1.23822425257
9
364
'''
