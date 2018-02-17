#Implementing Reinforcement Learning on a game called GridWorld
#you can learn about the game GridWorld here:
#https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html
#This program is based on a class I got on Udemy.com:
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer

#first let's build our environment for GridWorld, as simple as it is
#Remember reinforcement learning is heavily object oriented

import itertools

class Grid_World:
  '''
  this class is the GridWorld environment
  notice that it includes the player's character. The character
  is part of the environment, we only associate the agent with the
  ability to make decisions and learn

  it's also important to know that the agent's state is only where it
  currently is on the board, that is all it percieves
  though this is not a full state representation
  '''

  def __init__(self, width, height, start):
    '''
    initialize our grid_world environment
    width and height are that of the game board
    and start is a tuple of x,y coordinates for
    where the player starts on board

    it also starts by default with zero walls
    '''
    self.width = width
    self.height = height
    self.x = start[0]
    self.y = start[1]
    self.walls = []

  def state_rep(self):
    return(int(str(self.x)+str(self.y)))

  def set(self, rewards, actions):
    '''
    this is an all-in-one setter for rewards and actions
    rewards and actions are both dictionaries
    that use the state as the key and reward/possible actions allowed
    for the values

    actions are all the possible actions (as a list) that can take you to a new state,
    from the state you are in (the key)

    notably, tuples (state x,y pairs) are used as the keys for these dictionaries
    '''
    self.rewards = rewards
    self.actions = actions

  def set_state(self, state):
    '''
    to the agent, the 'state' is only it's location on the board
    to the environment, the only thing that can change is the location
    of the player. So a state transition occurs solely based on changing
    the position of the player

    the state is a coordinate tuple (x,y) for position of player on board
    '''
    self.x, self.y = state

  def get_state(self):
    '''
    a typical getter that will return a state tuple (x,y)
    '''
    return (self.x, self.y)

  def is_terminal(self, state):
    '''
    this method let's of know if a given state is terminal

    it does this by checking if the state is a key in the actions dictionary
    if it is not a key in the dictionary, then it has no actions associated
    with being in that state. If there are no actions to transition out
    of the state, then the state is terminal
    '''
    return state not in self.actions

  def game_over(self):
    '''
    returns whether or not the current state is terminal
    i.e. game over
    '''
    return self.is_terminal(self.get_state())

  def move(self, action):
    '''
    this function takes an action from the agent,
    checks to see if the move is legal (legal means that the action
    is in the list that is the value for dictionary actions using the state
    as the key), and then if it is legal it will set the player's position in
    the new state and will retrieve the reward from the reward dictionary (if
    there is a reward at all for that state) and the reward will be the return
    value
    '''
    if action in self.actions.get((self.x,self.y),[]):
      if action == 'U':
        self.y+=1 #as you might imagine going 'up' will increase y by one
      elif action == 'D':
        self.y-=1 #down
      elif action == 'L':
        self.x -=1 #left, negative on coordinate planes
      elif action == 'R':
        self.x +=1 #right

    #dict().get(): Return the value for key if key is in the dictionary, else default.
    #If default is not given, it defaults to None,
    #so that this method never raises a KeyError.
    return self.rewards.get((self.x,self.y), 0) #return the rewards at state or zero

  def undo(self, action):
    '''
    sets the state to what it would be if action was not taken
    assumes valid action
    '''
    if action == 'U':
      self.y+=1 #as you might imagine going 'up' will increase y by one
    elif action == 'D':
      self.y-=1 #down
    elif action == 'L':
      self.x -=1 #left, negative on coordinate planes
    elif action == 'R':
      self.x +=1 #right

    #this assertion statement is for debugging
    #it raises an AssertionError if statement inside doesn't evaluate to true
    #kinda like a sanity check
    assert(self.get_state() in self.all_states())

  def all_states(self):
    '''
    returns all known states
    that is anything that is a key for dictionaries
    rewards or actions

    remember that | is 'or' for sets and counts any state that is any either of them
    '''
    return set(self.actions.keys) | set(self.rewards.keys())

  def gen_states(self):
    '''
    a function that enumerates states (aka the grid coordinates)
    and returns them as a list

    Note: sum works just as you might expect using + to add up everything
    and to concatenate the multideminsional list together
    you just do sum(myList, [])
    '''
    states = sum([[(x,y) for x in range(self.width)] for y in range(self.height)], [])

    #removes any walls from possible states
    for wall in self.walls:
      if wall in states:
        states.remove(wall)

    return states

  def gen_actions(self, states):
    '''
    generates the actions dictionary
    based on valid states
    '''
    actions = {}
    for state in states:
      x,y = state
      action_list = []
      if (x,y+1) in states:
        action_list.append('U')
      if (x,y-1) in states:
        action_list.append('D')
      if (x-1,y) in states:
        action_list.append('L')
      if (x+1,y) in states:
        action_list.append('R')
      if len(action_list)>0:
        actions[state]=action_list

    return actions
      
    

#the rest are testing environment set ups, not part of the environment itself
def generate_grid(length, height, start, walls, terminal_rewards, step_cost=-.1):
    '''
    builds a valid Grid_World object base on these parameters
    
    a 'valid' grid world will be one such that
    - you can't have an action that moves you into a wall
    - you can't move off the board
    - the terminal states have no actions
    - all none terminal states have a reward equal to the step cost

    the step cost is what will incentivise the agent to solve the maze more quickly
    '''

    #the grid will be 4 long and 3 in height
    #the player will start position 0,0
    g = Grid_World(length,height, start)

    #add a wall at position x
    g.walls = walls

    #assign the rewards 1 and -1 (it is a dictionary)
    #to mark terminal states
    terminals = terminal_rewards.keys()

    #first get non-wall states (i.e. valid states)
    states = g.gen_states()

    #make the actions dictionary
    actions = g.gen_actions(states)


    #but remember terminal states are states which no action can be done to get out of
    #so remove terminal states from the actions
    for key in terminals:
      del actions[key]

    g.rewards = terminal_rewards
    g.actions = actions

    #assign each non terminal valid state with the step cost
    for key in actions:
      g.rewards[key]=step_cost

    #now we have the grid!
    return g

def test_grid():
  '''
  builds a pre-defined grid for testing

  looks like
  .  .  .  1
  .  x  . -1
  s  .  .  .
  '''

  g = generate_grid(4, 3, (0,0), [(1,1)], {(3,2):1, (3,1):-1}, -0.1)

  return g

def run_test():
  '''testing the test grid'''
  g = test_grid() #create test grid
  print("expected: 0,0 ||",g.get_state()) #show where player is now, should be 0,0
  r = g.move('U') #move up
  print("expected: 0,1 r=-0.1 ||",g.get_state(), r) # should be 0,1 and no reward
  r = g.move('R') #invalid move into wall
  #should still be in 0,1 since R is invalid. Also no reward
  print("expected: 0,1 r=-0.1 ||",g.get_state(), r)
  r = g.move('U')
  r = g.move('R')
  r = g.move('R')
  r = g.move('D')
  print("expected: 2,1 r=-0.1 ||",g.get_state(), r) #should be at 2,1 with no reward
  r = g.move('R') #move into terminal loose state
  print("expected: 3,1 r=-1 ||",g.get_state(), r)
  #try to move out of terminal state
  r = g.move('U')
  r = g.move('R')
  r = g.move('R')
  r = g.move('D')
  print("expected: 3,1 r=-1 ||",g.get_state(), r)
  print("test complete!")
  
  
if __name__ == "__main__":
  run_test()

  
  
