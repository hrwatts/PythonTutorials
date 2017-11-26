#python3 ~/PythonTutorials/ReinforcementLearning/tic_tac_toe_human.py
#Iterative Re-enforcement learning agent, Value function
#Made from a class I got on Udemy
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer

import random
import turtle
import time

'''
This is the one I presented to my intelligent systems class, so it has more non-RL related
code to demonstrate the agent to people

Train the agent, play against it, watch it play

reinforcment learning favors objects over scripting code
at a high level, we have 2 main kinds objects
the environment
and the agent
We will have 2 agent objects (player 1 and player 2 in Tic-Tac-Toe)
both interact with the same single instance of the environment
and they both interact with it in the same way (function play_game(p1,p2,env))
'''

def play_game(pl1,pl2,env,human=0,verbose=True):
	'''
	This function runs an entire episode of the game

	When a human is playing, they can be player 1, or player 2
	'''

	#no epsilon against humans
	if human==1:
		h=True
		p1=Human(True)
		p2=pl2
		p2.epsilon=0
	elif human==2:
		h=True
		p1=pl1
		p1.epsilon=0
		p2=Human(False)
	else:
		h=False
		p1=pl1
		p2=pl2
		
	
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
		#if a human player is playing, Turtle power is enabled
		current_player.move(env, h, verbose)

		#update state histories every move
		state = env.get_state()
		p1.update_history(state)
		p2.update_history(state)

	#update the value function
	p1.update(env)
	p2.update(env)

	#restore epsilon for training
	if human==1:
		h=True
		p1=Human(True)
		p2=pl2
		p2.epsilon=pl1.epsilon
	elif human==2:
		h=True
		p1=pl1
		p1.epsilon=pl2.epsilon
		p2=Human(False)
	else:
		h=False
		p1=pl1
		p2=pl2
	


class Player:

	'''
	This object is a player in the game of Tic-Tac-Toe
	'''

	#define players with a learning rate (alpha), and epsilon for use in epsilon-greedy
	def __init__(self, player_one, epsilon=0.1, alpha=0.5):
		#hyper-parameters for RL
		self.epsilon=epsilon
		self.alpha=alpha

		#remember which player you are
		if player_one:
			self.p=1
		else:
			self.p=4

		#the values for each state, adjusted for player 1 and 2
		self.values = initialize_states(player_one)
		
		#also to include, is an array for all states
		#because of the iterative RL method we are using
		#we need a look-up table for states
		self.state_history=[]

	def reset_history(self):
		#reset state history to nothing
		self.state_history=[]

	def move(self, env, h, verbose):
		#chooses an action based on epsilon-greedy
		#generates random value to compare to epsilon
		#h passes on to env.draw_board()
		r = random.random()
		if r<self.epsilon:
			#do a random action instead of best known action
			if verbose:
				print("Random Action Being Taken...")
			
			#choose an action randomly from the empty spots
			#NOTE: Error will be thrown if no spots are available
			env.board[random.choice(env.valid_moves())]=self.p
		else:
			#do best known action based on value of the state
			#so look up the value in the dictionary
			
			#get all available moves
			moves = env.valid_moves()

			#for every valid move, look up and record what the value of
			#the next state would be if that move was taken
			record = []
			for m in moves:
				#pretend to make the move
				env.board[m]=self.p
				#look up the value of this state in the dictionary
				#and record it
				record.append(self.values[env.get_state()])

				#now while we are here let's take a look at what moves and
				#values the agent is considering
				if verbose:
					print("Value of possible move:",self.values[env.get_state()])
					env.draw_board(h, self.values[env.get_state()])

				#also remember to undo the pretend move
				env.board[m]=0

			#get the highest value, and use whatever move had the highest value
			m=moves[record.index(max(record))]
			env.board[m]=self.p

			#and draw it out so the people can see
			if verbose:
				env.draw_board(h, self.values[env.get_state()])
			
			

	def update_history(self, state):
		'''
		state = env.get_state()
		we want to update are history every move made, even of other players
		which is why we don't just throw this in with move()
		'''		
		self.state_history.append(state)
		
	def update(self, env):
		'''
		we want to BACKTRACK over the states, so that:
		V(prev_state) = V(prev_state) + alpha*(V(next_state) - V(prev_state))
		where V(next_state) = reward if it's the most current state

		NOTE: we ONLY do this at the end of an episode (single game of TicTacToe)
		not so for all the algorithms we will study
		'''
			
		if self.p==1:
			#you are p1
			reward=env.reward(True)
		else:
			#you are p2
			reward=env.reward(False)

		#now for back tracking through our state history
		#using our basic value function, assign values to each state
		#here target will be the place holder for value of next state
		target=reward
		for state in reversed(self.state_history):
			#new value = val prev + learning rate * (val next - val prev)
			value = self.values[state] + self.alpha*(target - self.values[state])
			
			#now update that state's value
			self.values[state]=value

			#now the value of this state, is the next state value of the state before it
			target=value

		#the game is done, clear the history of the episode
		self.reset_history()

			
class Human:
	'''
	Human class is a dummy player, not just because it isn't as good
	as my highly trained agent, but also because it fakes functionality of
	a Player class just so I can save some code
	'''

	def __init__(self,player_one):

		#remember which player you are
		if player_one:
			self.p=1
		else:
			self.p=4

	def move(self, env, h, dummy):
		#get valid moves
		valid = env.valid_moves()

		#Since you are the human, choose your move
		#prompt helps you out
		prompt="Make a move...\nMoves:\n-------\n"
		prompt+="|1|2|3|\n-------\n|4|5|6|\n-------\n|7|8|9|\n-------\n"
		m=77
		while m not in valid:
			if m!=77:
				print("That move isn't valid")
			m = int(input(prompt))-1
		#place your piece
		env.board[m]=self.p
		
		#turtle power
		turtle_print(env.board, "Human")
			

	def update_history(self, state):
		#dummy
		pass
		
	def update(self, env):
		#dummy
		pass
	
		

class Board:
	
	'''
	This object represents the game board
	'''

	def __init__(self):
		#board will be initialized just as all zeros
		self.board=[0,0,0,0,0,0,0,0,0]

	def valid_moves(self):
		#returns the positions on the board which a
		#player has not already occupied
		return [index for index,val in enumerate(self.board) if val==0]

	def reward(self, player_one):
		'''
		you can't have an RL agent without rewards, that'd be madness!
		a reward must be given for every state transition, which is why we
		can't just call it when the game is over
		you reward the agent at every action, but it only gets +1 if it wins
		'''

		over, winner = self.game_over()

		#check if game is over, if not, no reward
		if not over:
			return 0
		elif player_one:
			#if player one, and you won the game, you get a reward
			if winner==1:
				return 1
			else:
				#player one didn't win
				return 0
		else:
			#player two's perspective
			if winner==2:
				return 1
			else:
				return 0

	def get_state(self):
		'''
		Will return a string that will uniquely index (hash) the current state.
		For this purpose, I will just use the board itself as the state index

		Example:
		-------  Which is just the array [1,0,1,0,0,0,0,4,0]
		|X| |X|  Is hashed as
		-------	 "101000040"
		| | | |  Because I assign player 1 as 1
		-------  and player 2 as 4 for use in game_over() calculations
		| |O| |
		-------
		'''

		state=""
		for pos in self.board:
			state+=str(pos)
		return state

	def draw_board(self, h, v):
		'''
		a really basic visuaization of the board in console
		if verbose is false, nothing will show
		'''
		if not h:
			string='| '

			for i,val in enumerate(self.board):
				if i%3==0:
					if i!=0:
						print(string)
					print("-------------")
					string='| '
				if val==1:
					string+="X"
				elif val==4:
					string+="O"
				else:
					string+=" "
				string+=" | "
				if i==8:
					print(string)
					print("-------------")
					print(" ")
		else:
			#Enable Turtle power
			turtle_print(self.board, v)
		
		
	def game_over(self):
		'''
		returns a boolean whether or not game is over
		if it is over, it will also return who won
		(0=draw, 1=player 1, 2=player 2)
		'''
		
		over=False

		victories=[]

		board=self.board

		#checks all possible victories, and see if anyone has won
		#if no one has won, then it sees if there are empty spaces to determine a draw
		#row victories
		victories.append(board[0] + board[1] + board[2])
		victories.append(board[3] + board[4] + board[5])
		victories.append(board[6] + board[7] + board[8])
		#column victories
		victories.append(board[0] + board[3] + board[6])
		victories.append(board[1] + board[4] + board[7])
		victories.append(board[2] + board[5] + board[8])
		#diagonal victories
		victories.append(board[0] + board[4] + board[8])
		victories.append(board[2] + board[4] + board[6])

		#player 1 has a value of 1
		#player 2 has a value of 4
		#empty space has value of 0

		winner=0

		#there is only one way to add up to 3, or 12 (3 1's and 3 4's)
		#hince my choosing of the numbers for player one and two
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
	
	

def initialize_states(player_one=True):
	'''
	For this game we initialize every state, and store it in a dictionary
	This function creates and returns that dictionary for either player
	1 = win
	0 = loose or draw
	0.5 = every other state (such as an unfinished game)
	
	Don't worry about impossible states, as they will never be used
	or updated since the game never reaches those states
	'''

	temp = Board()
	values={}
	

	#recursively fill the values of my states
	def re_state(position):
		for digit in [0,1,4]:
			temp.board[position]=digit
			
			#at this point we have a unique board configuration (state)
			#so we need to get it's value, and then put it in our dictionary
			outcome = temp.game_over()
			
			#just initializing the value we will assign the state
			v=0

			#if game over
			if outcome[0]:
				winner=outcome[1]
				#if player 2, values are reversed (except draw)
				if player_one:
					if winner==1:
						#player 1 wins, value=1
						values[temp.get_state()]=1
					else:
						#draw or player 2 wins, value = 0
						values[temp.get_state()]=0
				else:
					#player 2's perspective
					if winner==2:
						#player 2 wins, value=1
						values[temp.get_state()]=1
					else:
						#draw or player 1 wins, value = 0
						values[temp.get_state()]=0
			else:
				#not game over (undetermined)
				values[temp.get_state()]=.5


			if position>0:
				re_state(position-1)

	#actually call the recursive function
	re_state(8)

	return values

def turtle_print(board,v):
	'''
	takes in the board of the game, and generates turtle graphics for it
	'''

	turtle.clearscreen()

	tu = turtle.Turtle()
	tu.speed(0)
	tu.pensize(8)
	#line 1
	tu.penup()
	tu.goto(-300,-100)
	tu.pendown()
	tu.goto(300,-100)
	#line 2
	tu.penup()
	tu.goto(-300,100)
	tu.pendown()
	tu.goto(300,100)
	#line 3
	tu.penup()
	tu.goto(-100,300)
	tu.pendown()
	tu.goto(-100,-300)
	#line 4
	tu.penup()
	tu.goto(100,300)
	tu.pendown()
	tu.goto(100,-300)
	tu.ht()
	
	positions={
			0:(-200,200),
			1:(0,200),
			2:(200,200),
			3:(-200,0),
			4:(0,0),
			5:(200,0),
			6:(-200,-200),
			7:(0,-200),
			8:(200,-200)
		}

	def draw_x(pos):
		tu=turtle.Turtle()
		tu.speed(0)
		tu.penup()
		tu.pensize(8)
		tu.goto(positions[pos])
		tx,ty=tu.pos()
		tu.goto(tx+90,ty+90)
		tu.pendown()
		tu.goto(tx-90,ty-90)
		tu.penup()
		tu.goto(tx+90,ty-90)
		tu.pendown()
		tu.goto(tx-90,ty+90)
		tu.ht()

	def draw_o(pos):
		tu=turtle.Turtle()
		tu.shape("turtle")
		tu.left(45)
		tu.penup()
		tu.turtlesize(7,7)
		tu.goto(positions[pos])
		

	turtle.title("Value of prospective state: " + str(v))

	for index,pos in enumerate(board):
		if pos==1:
			draw_x(index)
		if pos==4:
			draw_o(index)

	time.sleep(.75)


	
	
	
	

#---------------------------------
#The "main" of the program is this
#---------------------------------
p1 = Player(True)
p2 = Player(False)

play = "yes"
while play=="yes":
	num_train = int(input("How many times should your agent train?"))
	verbose = input("Show training?")
	if verbose=="yes":
		verbose=True
	else:
		verbose=False
	
	for t in range(num_train):
		env=Board()
		play_game(p1,p2,env,verbose=verbose)

	h_player = int(input("What player would you like to be?"))
	if h_player>0:
		env=Board()
		play_game(p1,p2,env,human=h_player)

	play = input("Would you like to do this again?")

print("Thanks for playing!")




