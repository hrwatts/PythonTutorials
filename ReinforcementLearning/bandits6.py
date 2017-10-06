#python3 ~/PythonTutorials/ReenforcementLearning/bandits6.py
#The Multi-Arm Bandit problem
#Re-enforcement learning, epsilon-greedy strategy
#Made from a class I got on Udemy
#"artificial intelligence reinforcement learning in python" by The LazyProgrammer

import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    '''
    bandit represents a slot machine
    m is the true win rate of the machine
    we will be using the mean to calculate the win rate
    since it is hidden from us
    and N is the number of times we've tried a machine
    '''
    def __init__(self, val_list):
        freq, period, max_N = val_list
        n = max_N
        ix = np.arange(n)
        self.signal = (np.sin(freq*(np.pi*ix/float(n/2) + period))+ 1)/2
        self.mean = 1
        self.N = 0
        self.m = self.signal[self.N]
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
        self.m = self.signal[self.N-1]

def run_experiment(m1,m2,m3,N):
    """
    give the parameters for 3 bandits
    an epsilon function to use for
    epsilon-greedy strategy
    and N, the number of times we play the game
    """
    bandits = [Bandit(m1),Bandit(m2),Bandit(m3)]
    
    #for PLOTTING ONLY
    #this is not needed for functioning
    data = np.empty(N)
    #play game N times
    for i in range(N):
        j = np.argmax([b.mean for b in bandits])
        #pull the one we chose
        x = bandits[j].pull()
        #whether explore or exploit, we update our knowledge
        bandits[j].update(x)
        #for PLOTTING
        data[i] = x
    #this is basically the rate your agent sees at the win rate per bandit
    #once the experiment is over
    cumulative_average = np.cumsum(data)/(np.arange(N)+1)
    plt.plot(cumulative_average)
    #just lines, like grid lines
    for b in bandits:
        plt.plot(b.signal)
        plt.title("Sin Bandits")
        #plt.xscale('log')
    plt.show()
    return cumulative_average

max_N = 100000
one = [.5, 0, max_N]
two = [1, 0, max_N]
three = [1, 1, max_N]

ran = run_experiment(one,two,three,max_N)
