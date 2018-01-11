#risk.py
#Christian Watts

import sys
import risk_functions as rf
import Agent
import random

def parse_test():
    '''
    test the ability to parse state representations
    it also test the amount of memory it takes to
    store the state representation
    '''
    
    test = "Hello World!"
    print(test,sys.getsizeof(test), "bytes")

    board, continents, trade_vals, card_faces, territories, cards = rf.gen_board()

    #sets troops to a random number 1-2,000,000 for each territory
    for key in territories:
        territories[key][1]=random.randrange(1,2000000)

    state = (territories, cards, 0)
    st_string = rf.get_state(state)
    state_2 = rf.parse_state(st_string, debug=True)
    st_string_2 = rf.get_state(state_2)

    print("State String Size:",sys.getsizeof(st_string),st_string)

    print("State String 2 Size:",sys.getsizeof(st_string_2),st_string_2)


    #this compares state->rep rep->state lossless conversion
    return st_string==st_string_2

def player_test():
    '''
    test player creation of BaseAgent
    '''

    #get some initial environment
    board, continents, trade_vals, card_faces, territories, cards = rf.gen_board()

    #create agent as player 1 and go first
    agent = Agent.BaseAgent(0,0)

    print(agent)
    print("Class Vars (player)",agent.player, "(turn order)",agent.order)

    #test sets
    #([cards owned],[correct sets])
    #2 (1,5,10)s
    test_sets = [
        ([0,1,2,3,4,5],[[0,2,1],[3,4,5]]),
        ([0,1,2,3,4,43], [[0, 2, 1], [0, 3, 43], [2, 4, 43], [0, 2, 43], [0, 1, 43], [1, 2, 43]]),
        ([0,1,3,4,6],[[0,3,6],[0,4,1]])]

    test_success = True
    for s in test_sets:
        data,ans = s
        print("data:",data)
        temp_cards = dict(cards)
        for c in data:
            temp_cards[c]=agent.player
        sets  = agent.get_sets(temp_cards, card_faces, debug=True)

        print("Sets detected:",sets)
        print("Sets supposed:",ans)
        
        for i,s in enumerate(sets):
            ts = ans[i]
            #print(s)
            #print(ts)
            for i2,e in enumerate(s):
                if e!=ts[i2]:
                    test_success=False
    return test_success

#****************************************************************
print("Parse Test successful?", parse_test(),"*"*50,"\n\n")
print("Agent Test successful?", player_test(),"*"*50,"\n\n")
