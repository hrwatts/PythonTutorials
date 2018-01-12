"""
This is the "World Domination" version of Risk
use this to set up and play the game
"""

import random

def config():
    '''used to gather user configuration settings for game'''
    
    players = int(input("How many players? "))

    if input("Deal territories to players? y/n "):
        deal=True
    else:
        deal=False

    return (players, deal)

def turn_order(players, debug=False):
    '''
    assigns the turn order randomly
    by picking one player and then going sequencially
    '''
    p_list = list(range(players))
    op_list = list(p_list)
    
    order=[]

    clockwise = input("Clockwise, highest roll, or input order? c/r/i ")
    
    if clockwise.lower()=="c":
        
        first = random.choice(p_list)
        order = [player if player<=players-1 else p_list[player-players] for player in range(first, players+first)]

        if debug:
            print("the first player should be",first)
        
    elif clockwise.lower()=="r":

        for player in range(players):
            chosen = random.choice(p_list)
            p_list.remove(chosen)
            order.append(chosen)
        
    else:

        order = [int(x)-1 for x in input("Enter the order by space seperated intergers example: \"1 2 3\" ").split()]

    if debug:
        print("the order decided was",order)

    if sum([True for p in order if p in op_list])==players:
        if debug:
            return True
    else:
        raise ValueError("Error generating player order... " + str(order))
    
    return order
