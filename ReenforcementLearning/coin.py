#python3 ~/PythonTutorials/ReenforcementLearning/coin.py
#Re-enforcement learning, Bayesian strategy
#Made from a class I got on Udemy
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

#this is just for visualizing what is going on
def plot(a, b, trial, ctr):
	x = np.linspace(0, 1, 200)
	#we are saying that 
	y = beta.pdf(x, a, b)
	mean = float(a) / (a + b)
	plt.plot(x, y)
	plt.title("Distributions after %s trials, true rate = %.1f, mean = %.2f" 
		% (trial, ctr, mean))
	plt.show()
	print("samples taken = ", trial, "| true rate =", ctr, "| mean so far =",round(mean,2))

#here we use the Bayesian rule to figure out what to use
#as the posterior, which will dictate the algorithm
#a coin toss follows the Bernoulli distribution
#so we look up and find that the conjugate prior distribution is Beta or [0,1]
#which takes in 2 hyper parameters a and b

#this is the true rate of "heads" or 1, %30
#but this is hidden from our model
true_ctr = 0.3

#instead we just start off guessing (1/1, uniform distribution), %50 1/1
a, b = 1, 1 # beta parameters

show = [0, 5, 10, 25, 50, 100, 200, 300, 500, 700, 1000, 1500]
for t in range(0,1501):
	#here we generate a "weighted" coin toss according to the true rate of "heads"
	coin_toss_result = (np.random.random() < true_ctr)
	if coin_toss_result:
		#if heads, a adds 1
		a += 1
	else:
		#if tails, b adds 1
		b += 1

	if t in show:
		plot(a, b, t+1, true_ctr)

#we see that as our number of samples increase, the varience in them decreases
#so our distribution gets skinnier and taller
#it also is more confident and the mode is closer to the true mean
#output to console
'''
samples taken =  1 | true rate = 0.3 | mean so far = 0.33
samples taken =  6 | true rate = 0.3 | mean so far = 0.12
samples taken =  11 | true rate = 0.3 | mean so far = 0.15
samples taken =  26 | true rate = 0.3 | mean so far = 0.32
samples taken =  51 | true rate = 0.3 | mean so far = 0.32
samples taken =  101 | true rate = 0.3 | mean so far = 0.33
samples taken =  201 | true rate = 0.3 | mean so far = 0.29
samples taken =  301 | true rate = 0.3 | mean so far = 0.27
samples taken =  501 | true rate = 0.3 | mean so far = 0.29
samples taken =  701 | true rate = 0.3 | mean so far = 0.29
samples taken =  1001 | true rate = 0.3 | mean so far = 0.29
samples taken =  1501 | true rate = 0.3 | mean so far = 0.3
'''
