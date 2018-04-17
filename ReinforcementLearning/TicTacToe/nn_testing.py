from tic_tac_toe_human import Board, Player, Human, play_game
from nn_player import NNAgent
import random
import numpy as np


class RandPlayer(object):

    def __init__(self, player_one, epsilon=0.1, alpha=0.5):
        if player_one:
            self.p = 1
        else:
            self.p = 4

    def reset_history(self):
        pass

    def move(self, env, h, verbose):
        m = random.choice(env.valid_moves())
        env.board[m] = self.p

        if verbose:
            print("Random Agent move:")
            env.draw_board(h, [0]*9)

    def update_history(self, state):
        pass

    def update(self, env):
        pass
            
    


p1 = NNAgent(True)
bp2 = Player(False, epsilon = 0.2)

play = "yes"
while play=="yes":

    p2 = bp2

    if input("Switch?: ") == 'y':
        p2 = RandPlayer(False)

    games = int(input("Games: "))

    results = np.empty(games)

    for num in range(games):

        if num == games-1:
            p1.v_flag = True
        
        env = Board()
        results[num] = play_game(p1, p2, env, verbose=False)

        p1.v_flag = False

    print("P1 win ratio:",round(results.mean()*100,2),"%")

    hum = int(input("Human? 2/0: "))
    env = Board()
    play_game(p1, p2, env, human=hum)

    

    play = input("Would you like to do this again with same agents? (yes/no) ")
