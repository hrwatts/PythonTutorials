'''
This class is testing for genetic algorithmns for neural networks

As such I purposely pad out the output layer with invalid moves,
as I am testing its effect on the agent
'''
import warnings
warnings.filterwarnings("ignore")

from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.callbacks import EarlyStopping
import numpy as np
import sys

class NNAgent(object):
    def __init__(self, player_one, epsilon=0.1, alpha=0.5):
        self.p = {True:1,False:4}[player_one]
        self.state_history = []
        self.move_history = []
        self.recent_state_history = []
        self.recent_move_history = []
        self.input = 9 #size of input layer
        self.output = 15 #size of output layer
        self.nodes = 24 #node mult constant
        self.model = self.create_nn()
        self.v_flag = False

    def reset_history(self):
        self.recent_state_history = []
        self.recent_move_history = []

    def move(self, env, h, verbose):

        #shape = (9,)
        state = np.array([env.board])

        #move shape = (15,)
        move = self.model.predict(state)

        #find max prediction
        max_move = np.argmax(move)

        valid = env.valid_moves()

        while max_move not in valid:
            #update the NN since it chose wrong
            self.bad_move(state, valid)

            #choose again
            move = self.model.predict(state)
            max_move = max_move = np.argmax(move)

        #record moves made this turn game
        self.update_history(state, move)

        #actually make the move and change the state
        env.board[max_move]=self.p

        if verbose:
            print("NN Agent move:")
            env.draw_board(h, [0]*9)

    def update_history(self, state, move_layer="not NN player"):
        if isinstance(move_layer,str):
            pass
        else:
            self.recent_state_history.append(state)
            self.recent_move_history.append(move_layer)

    def update(self, env):
        #reward is 1 if this agent wins, 0 is this agent looses
        if self.p==1:
            #you are player one
            reward=env.reward(True)
        else:
            #you are p2
            reward=env.reward(False)
        
        def re(ry, reward):
            if reward>0:
                ret = np.zeros(ry.shape)
                ret[0, np.argmax(ry)]=1
            else:
                ret = np.empty(ry.shape)
                ret.fill(0.5)
                ret[0, np.argmax(ry)] = 0

            return np.mean([ret, ry], axis=0)

        self.recent_move_history = [re(ry, reward) for ry in self.recent_move_history]

        self.state_history += self.recent_state_history
        self.move_history += self.recent_move_history

        self.state_history = self.state_history[-15:]
        self.move_history = self.move_history[-15:]

        X = np.vstack(self.state_history)
        y = np.vstack(self.move_history)
        

        monitor = EarlyStopping(patience=2)
        self.model.fit(X, y, epochs=6, callbacks=[monitor], verbose=self.v_flag)
        
        self.reset_history()

##########################################################################
######################--------------------################################
######################--Genetic Specific--################################
######################--------------------################################
##########################################################################

    def create_nn(self):
        '''
        Builds a neural network
        '''

        #build model
        model = Sequential()
        model.add(Dense(self.nodes, activation='sigmoid', input_shape=(self.input,)))
        model.add(Dense(int(self.nodes*0.75), activation='sigmoid'))
        model.add(Dense(self.output, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        return model

    def bad_move(self, state, valid):
        '''
        for the moves that are valid, put 1 in their place
        for invalid moves, put 0
        '''
        layer = np.array([[0]*self.output])
        for pos in valid:
            layer[0, pos] = 1
        self.model.fit(state, layer, verbose=False)
