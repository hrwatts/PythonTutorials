#Iterative Policy Evaluation testing on grid_world using a few policies
#This program is based on a class I got on Udemy.com:
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer


import numpy as np
import matplotlib.pyplot as plt
from grid_world import test_grid

def print_values(values, grid):

  for y in range(grid.height):
    
    print('------------------------------')

    for x in range(grid.width):

      values.get((x,y))

      print(round(x,2),' | ')


def print_policy(policy, grid):

  pass

if __name__ == '__main__':
  '''
  this is the iterative policy evaluation
  kinda like gradient decent
  you are trying to get the slope of the change in value
  from one iteration to the next very close to 0

  the psuedocode for this is:

  set threshold
  threshold = some small number close to zero

  initialize
  V(s)=0 for all states

  while(forever):

    intialize the change in value to zero
    delta_value = 0
  
    for each state:
    
      old_value = V(state)
      
      V(state) = (summation of policy probability distribution *
                  summation of state transition probability distribution)
                  
      delta_value = current delta_value or abs( V(state) - old_value )

      if delta_value < threshold:
            break while loop

  V(s) is now close to the converged value for the given policy

  '''
  g = test_grid()

  states = g.all_states()

  #set threshold
  threshold = 10**-4

  #initialize the value function for every state to be zero
  values = {}
  for state in states:
    values[state] = 0

  #start infinite while loop
  while True:
    #intialize change in value to start at zero
    delta = 0

    #now go through the value of each state
    
