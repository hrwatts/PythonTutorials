#risk.py
#Christian Watts

import sys
import risk_environment as risk
import agent
import random
import world_domination as wd

def config_test():
    '''testing the game config from world_domination.py'''

    players, deal = wd.config()
    if deal:
        order = wd.turn_order(players, debug=True)

    return order
    

def parse_test():
    '''
    test the ability to parse state representations
    it also test the amount of memory it takes to
    store the state representation
    '''
    
    test = "Hello World!"
    print(test,sys.getsizeof(test), "bytes")

    env = risk.Risk()
    territories, cards, trade_ins = env.state

    #sets troops to a random number 1-2,000,000 for each territory
    for key in territories:
        territories[key][1]=random.randrange(1,2000000)

    state = (territories, cards, trade_ins)
    st_string = env.get_state(state)
    state_2 = env.parse_state(st_string, debug=True)
    st_string_2 = env.get_state(state_2)

    print("State String Size:",sys.getsizeof(st_string),st_string)

    print("State String 2 Size:",sys.getsizeof(st_string_2),st_string_2)


    #this compares state->rep rep->state lossless conversion
    return st_string==st_string_2

def player_test():
    '''
    test player creation of BaseAgent
    '''

    #get some initial environment
    env = risk.Risk()
    territories, cards, trade_ins = env.state

    #create agent as player 1 and go first
    agent_demo = agent.BaseAgent(0,0)

    print(agent_demo)
    print("Class Vars (player)",agent_demo.player, "(turn order)",agent_demo.order)

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
            temp_cards[c]=agent_demo.player
        sets  = agent_demo.get_sets(temp_cards, env.card_faces, debug=True)

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

def node_test():
    '''test the nodes dictionaries'''

    env = risk.Risk()
    
    node2name,name2node = env.id_names()

    ids = list(node2name.keys())
    for i_d in ids:
        if i_d != name2node[node2name[i_d]] :
            print("ID",i_d,"is not",name2node[node2name[i_d]])
            return False

    positions = env.pygame_positions()
    for num in range(42):
        print("Name:",node2name[num],"\tID:",num,"Position",positions[num])

    return True


#****************************************************************
if input("Run node test? y/n ").lower() == "y":
    print("Node Test successful?", node_test(),"*"*50,"\n\n")    
if input("Run parse test? y/n ").lower() == "y":
    print("Parse Test successful?", parse_test(),"*"*50,"\n\n")
if input("Run agent test? y/n ").lower() == "y":
    print("Agent Test successful?", player_test(),"*"*50,"\n\n")
if input("Run game config test? y/n ").lower() == "y":
    print("Config Test successful?", config_test(),"*"*50,"\n\n")
