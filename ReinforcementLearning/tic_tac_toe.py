#python3 ~/PythonTutorials/ReinforcementLearning/tic_tac_toe.py
#Iterative Re-enforcement learning agent, Value function
#Made from a class I got on Udemy
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer

import numpy as np

'''
reinforment learning favors objects over scripting code
at a high level, we have 2 main kinds objects
the environment
and the agent
We will have 2 agent objects (player 1 and player 2 in Tic-Tac-Toe)
both interact with the same single instance of the environment
and they both interact with it in the same way (function play_game(p1,p2,env))
'''

def play_game(p1,p2,env):
	'''
	This function runs an entire episode of the game
	'''
	
	turn=0
	
	#loops until the game is over
	while not env.game_over()[0]:
		#a single turn will consist of one player moving a move
		#making sure in between turns to alternate
		if turn%2==0:
			current_player=p1
		else:
			current_player=p2
		turn+=1

		#current player makes a move
		current_player.move(env)

		#update state histories every move
		state = env.get_state()
		p1.update_history(state)
		p2.update_history(state)

		#update the value function
		p1.update(env)
		p2.update(env)

class Player:

	'''
	This object is a player in the game of Tic-Tac-Toe
	'''

	#define players with a learning rate (alpha), and epsilon for use in epsilon-greedy
	def __init__(self, epsilon=0.1, alpha=0.5):
		self.epsilon=epsilon
		self.alpha=alpha
		
		#also to include, is an array for all states
		#because of the iterative RL method we are using
		#we need a look-up table for states
		self.state_history=[]

	def set_value_function(self,value_function):
		self.vf = value_function

	def move(self, env):
		#chooses an action based on epsilon-greedy
		#generates random value to compare to epsilon
		r = np.random.rand()
		if r<self.epsilon:
			#do a random action instead of best known action
			pass
			

	def update_history(self, state):
		# state = env.get_state()
		#we want to update are history every move made, even of other players
		self.state_history.append(state)
		
	def update(self, env):
		# we want to BACKTRACK over the states, so that:
		# V(prev_state) = V(prev_state) + alpha*(V(next_state) - V(prev_state))
		# where V(next_state) = reward if it's the most current state
		#
		# NOTE: we ONLY do this at the end of an episode
		# not so for all the algorithms we will study
		

class Board:
	
	'''
	This object represents the game board
	'''

	def __init__(self):
		#board will be initialized just as all zeros
		self.board=[0,0,0,0,0,0,0,0,0]

	def get_state(self):
		'''
		will return an integer that will uniquely index the current state
		for this purpose, I will just use the board itself as the state index
		'''
		state=""
		for pos in self.board:
			state+=str(pos)
		return int(state)
		
		
	def game_over(self):
		#returns a boolean whether or not game has a winner or is a draw
		#if it is over, it will also return who won
		#(0=draw, 1=player 1, 2=player 2)
		
		over=False

		victories=[]

		board=self.board

		#checks all possible victories, and see if anyone has won
		#if no one has won, then it sees if there are empty spaces to determine a draw
		#row victories
		victories.append(sum([x for x in board[:3]]))
		victories.append(sum([x for x in board[3:6]]))
		victories.append(sum([x for x in board[6:]]))
		#column victories
		victories.append(sum([x for index,x in enumerate(board) if index%3==0]))
		victories.append(sum([x for index,x in enumerate(board) if index%3==1]))
		victories.append(sum([x for index,x in enumerate(board) if index%3==2]))
		#diagonal victories
		victories.append(sum([board[0],board[4],board[8]]))
		victories.append(sum([board[2],board[4],board[6]]))

		#player 1 has a value of 1
		#player 2 has a value of 4
		#empty space has value of 0

		winner=0

		for vic in victories:
			if vic==3:
				over=True
				winner=1
				break
			if vic==12:
				over=True
				winner=2
				break
			if 0 not in board:
				over=True
				winner=0
				break

		return (over,winner)



#---------------------------------------------------------------------
#The program runs here
#---------------------------------------------------------------------
p1=Player()
p2=Player()
env=Board()

play_game(p1,p2,env)









