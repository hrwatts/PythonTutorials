#risk_functions.py

def gen_board():
    """
    Generates the environment and initial state of the game
    """
    names = [
        #North America
        "Alaska","NW_Territory","Greenland","Alberta",
        "Ontario","E_Canada","W_US","E_US","C_America",
        #South America
        "Venezuela","Brazil","Peru","Argentina",
        #Africa
        "N_Africa","Egypt","E_Africa","C_Africa","S_Africa","Madagascar",
        #Australia
        "Indonesia","New_Guinea","W_Australia","E_Australia",
        #Europe
        "Iceland","Great_Britain","Scandanavia",
        "Russia","N_Europe","S_Europe","W_Europe",
        #Asia
        "Mid_East","Afghanistan","Ural","Siberia",
        "Yakutsk","Kamchatka","Irkutsk","Mongolia",
        "Japan","China","India","Siam"]

    node2name = {}
    for num, name in enumerate(names):
        node2name[num]=name

    name2node = {}
    for num, name in enumerate(names):
        name2node[name]=num
    
    board = {
        0:[1,3,35],1:[2,3,4],2:[5,1,4,23],3:[0,4,1,6],4:[1,2,3,5,6,7],
        5:[2,4,7],6:[3,4,7,8],7:[5,4,6,8],8:[6,7,9],9:[8,10,11],
        10:[9,12,11,13],11:[10,12,9],12:[10,11],13:[10,14,16,28,29,15],
        14:[13,16,28,29],15:[13,16,17,14,30,18],16:[13,15,17],17:[16,15,18],
        18:[17,15],19:[41,20,21],20:[22,21,19],21:[22,19,20],22:[20,21],
        23:[2,24,25],24:[23,25,27,29],25:[23,27,26,24],26:[25,27,28,30,31,32],
        27:[26,28,29,25,24],28:[29,27,26,30,13,14],29:[13,28,27,24],
        30:[31,40,14,15,26,28],31:[32,30,26,40,39],32:[31,26,33,39],
        33:[32,39,37,34,36],34:[33,36,35],35:[38,34,36,0],36:[35,34,33,37],
        37:[36,38,39,33,35],38:[35,37],39:[31,37,33,41,40,32],40:[39,41,31,30],
        41:[39,40,19]
        }

    #Continent name as key, with a list containing
    #continent value as 1st element, and then nodes
    continents = {
        "Europe":[5,23,24,25,26,27,28,29],
        "N_America":[5,0,1,2,3,4,5,6,7,8],
        "Africa":[3,14,18,13,15,16,17],
        "Australia":[2,19,20,21,22],
        "Asia":[7,30,31,32,33,34,35,36,37,38,39,40,41],
        "S_America":[2,9,12,10,11]
        }

    #initializes the initial state of the game
    #the game state is all the nodes, node owner, and army size per node
    territories = {
        0:[0,0],1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0],7:[0,0],8:[0,0],
        9:[0,0],10:[0,0],11:[0,0],12:[0,0],13:[0,0],14:[0,0],15:[0,0],16:[0,0],
        17:[0,0],18:[0,0],19:[0,0],20:[0,0],21:[0,0],22:[0,0],23:[0,0],24:[0,0],
        25:[0,0],26:[0,0],27:[0,0],28:[0,0],29:[0,0],30:[0,0],31:[0,0],32:[0,0],
        33:[0,0],34:[0,0],35:[0,0],36:[0,0],37:[0,0],38:[0,0],39:[0,0],40:[0,0],
        41:[0,0]
        }

    #initializes the cards pre-start of game with their owner '8' is unused
    cards = {
        0:8,1:8,2:8,3:8,4:8,5:8,6:8,7:8,8:8,9:8,
        10:8,11:8,12:8,13:8,14:8,15:8,16:8,17:8,18:8,19:8,
        20:8,21:8,22:8,23:8,24:8,25:8,26:8,27:8,28:8,29:8,
        30:8,31:8,32:8,33:8,34:8,35:8,36:8,37:8,38:8,39:8,
        40:8,41:8,42:8,43:8
        }

    return (board, continents, territories, cards, node2name, name2node)

def parse_state(state_string):
    '''
    gets the state from the state representation string
    '''

    board, continents, territories, cards = gen_board()
    ter_string, cards_string, trade_string = state_string.split(':')

    #parse territories string
    for ter in ter_string.split('!'):
        key, one, two = ter.split('.')
        territories[key]=[one,int(two)]

    #parse card string
    for card in cards_string.split('!'):
        key, val = card.split('.')
        cards[key]=val

    #cast to int
    trade_ins = int(trade_string)

    return (territories, cards, trade_ins)

def get_state(state):
    '''
    gets the state representation string from the state
    '''

    #the game state consist of 3 things
    #1) each territory's owner, and # of troops in them
    #2) the owner of each card
    #3) the number of Risk card sets that have been traded in 
    territories,cards,trade_ins = state

    state_string = ""

    for key in territories:
        one,two = territories[key]
        state_string = state_string + str(key) + "."
        state_string = state_string + str(one) + "." + str(two) + "!"

    #remove the last '!'
    state_string = state_string[:-1]
    
    state_string = state_string + ":"
    for key in cards:
        state_string = state_string + str(key) + "." + str(cards[key]) + "!"

    #remove the last '!'
    state_string = state_string[:-1]

    state_string = state_string + ":" + str(trade_ins)

    return state_string
