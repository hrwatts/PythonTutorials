#python3 ~/PythonTutorials/ReenforcementLearning/bandits2.py
#The Multi-Arm Bandit problem
#Re-enforcement learning, optimistic initial values strategy, greedy
#Made from a class I got on Udemy
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer

import numpy as np
import matplotlib.pyplot as plt

#this is basically the same as bandit.py except it uses a different strategy

class Bandit:
	'''
	bandit represents a slot machine
	m is the true win rate of the machine
	we will be using the mean to calculate the win rate
	since it is hidden from us
	and N is the number of times we've tried a machine
	'''
	def __init__(self, m):
		self.m = m
		#initialize the mean to some optimistic value
		self.mean = 1
		self.N = 1

	def pull(self):
		#this is the reward given
		p = np.random.random()
		if p < self.m:
			#win
			return 1
		else:
			#lose
			return 0

	def update(self, x):
		self.N +=1
		self.mean = (1 - 1/self.N)*self.mean + (1/self.N)*x

def run_experiment(m1,m2,m3,N):
	"""
	we take in the true win rates for bandits
	and the number of times we want to play
	"""
	bandits = [Bandit(m1),Bandit(m2),Bandit(m3)]
	
	#for PLOTTING ONLY
	#this is not needed for functioning
	data = np.empty(N)

	#play game N times
	for i in range(N):
		#we explore automatically now instead of randomly
		#since unexplored bandits will have that really optimistic
		#initial value and will appear the best one to the agent

		j = np.argmax([b.mean for b in bandits])
		x = bandits[j].pull()
		bandits[j].update(x)

		#for PLOTTING
		data[i] = x

	#this is basically the rate your agent sees at the win rate per bandit
	#once the experiment is over
	cumulative_average = np.cumsum(data)/(np.arange(N)+1)

	plt.plot(cumulative_average)

	#just lines, like grid lines
	plt.plot(np.ones(N)*m1)
	plt.plot(np.ones(N)*m2)
	plt.plot(np.ones(N)*m3)

	plt.xscale('log')
	plt.show()

	for index,b in enumerate(bandits):
		print("Bandit " + str(index) + ' ' + str(b.mean))
	
	return cumulative_average

#run the actual experiment with given bandit win rates
experiment = run_experiment(0.10,0.20,0.30, 100000)

#compared to Epsilon-Greedy you can tell this strategy finds the optimal bandit sooner
#and waste nothing after fiding it, only explointing the best path

#output to console
'''
Bandit 0 0.25
Bandit 1 0.25
Bandit 2 0.2993449672483532
'''
