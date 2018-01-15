'''
Run this to play the GUIless version of Risk RL
'''

import config
import risk_environment as risk
import human
import agent

debug = True

def main():
    '''start a game of Risk'''

    #settings
    players, deal, steal_cards = config.console_players()
    turn_order = config.turn_order(players)
    trade_values = config.console_trade_vals()
    player_list = config.console_get_players(players)

    if debug:
        print("Turn order is:",turn_order)

    #generate the environment with settings
    env = risk.Risk(turn_order,trade_values,steal_cards)

    #set up pre-game territory allocation
    if deal:
        env.deal_territories()
    else:
        #players are prompted by turn order for a territory selection
        valid = list(range(42))
        for index in range(42):
            current_player = player_list[turn_order[index%len(turn_order)]]
            chosen, env.state = current_player.pick_initial_territories(valid, env.state)
            valid.remove(chosen)

    #place the remaining troops
    #here************************************

    if debug:
        [print(x) for x in env.state]

    #initializing some variables
    turn_count = 0 #this is how many times any player has taken a turn

    #main game loop
    while not env.winner(debug):

        #whose turn is it?
        turn = turn_order[turn_count%players]

        #is this player defeated? If so skip turn
        while env.defeated(turn, debug):
            turn_count+=1
            turn = turn_order[turn_count%players]

        #get undefeated player
        current_player = player_list[turn]


        #recruitment phase
        current_player, env = recruitment_phase(current_player, env)

        #attack phase
        current_player, env = attack_phase(current_player, env)

        #reinforce phase
        current_player, env = reinforce_phase(current_player, env)

        #update current player back into player list
        player_list[turn_order[turn_count%players]] = current_player

        #increase turn count
        turn_count+=1
 
def recruitment_phase(current_player, env):
    '''perform recruitment phase'''
    #recruit troops for turn
    recruited = current_player.recruit_troops(env.state, env.continents)

    #place recruited troops, update the game state to reflect placement
    env.state = current_player.place_troops(env.state,recruited)

    #does agent have a valid card trade in set?
    set_list,card_count = current_player.get_sets(env.state, env.card_faces)

    #if agent does, prompt them for whether or not they want to trade in a set
    while len(set_list)!=0:
        recruited = current_player.trade_in(env.state, env.trade_vals, set_list, count)
        if recruited!=0:
            #increase number of trade ins
            env.state[-1]+=1

            #place newly recruited troops
            env.state = current_player.place_troops(recruited)
        else:
            set_list=[]

    #recruitment phase is over
    return (current_player, env)

def attack_phase(current_player, env):
    '''perform attack phase'''

    return (current_player, env)

def reinforce_phase(current_player, env):
    '''perform reinforcement phase (Turn phase not RL)'''

    return (current_player, env)

#----------------------------------------------------------------------
# Main
#----------------------------------------------------------------------
if __name__ == "__main__":
    # execute only if run as a script
    main()
