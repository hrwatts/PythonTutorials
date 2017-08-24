#manual forward propagation
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/forward.py


#imports
import numpy as np

#we are going to simulate a neural network forward propagation algorithm
#see the picture forwardPropagation.png for more info
#the basics are it moves from input layer, hidden layer, output layer
#input is data observed or fitted
#hidden is all the behind the scenes way the model works with inputs
#output is the target, the product of processes in the hidden layer

#say we have 2 features in the input layer for a single observation
#those features are numerical, with values 2 and 3
input_data = np.array([2,3])

#from the input layer, interactions between features are represented by nodes in the hidden layer
#the significance of each interaction is denoted by parameters called weights
#weights are directly used to scale the input data into proper significance
#after the initial layer is complete, then the nodes themselves interact with each other
#in the exact same way, each node connects with weights to a new node
#in this case it goes into the output layer after the 2 hidden nodes
#the connections for the nodes to the output have weights too
weights = {'node_0': np.array([1,1]), 'node_1': np.array([-1,1]), 'output': np.array([2,-1])}
print(weights)

#the algorithm for caculating forward propagation is as follows
#(input val1 * weight val1) + (input val2, weight val2)
node_0_val = (input_data*weights['node_0']).sum()
node_1_val = (input_data*weights['node_1']).sum()

#for simplicity, we will hold the entire hidden layer in a variable
hidden_layer_vals = np.array([node_0_val, node_1_val])
print(hidden_layer_vals)

#to calculate to output layer, it works the same way
output_val = (hidden_layer_vals*weights['output']).sum()
print(output_val)

#so here you can see for the given weights those values end up as 9 for the output.
#this is the basis of forward propagation

#output to console
'''
{'output': array([ 2, -1]), 'node_0': array([1, 1]), 'node_1': array([-1,  1])}
[5 1]
9
'''
