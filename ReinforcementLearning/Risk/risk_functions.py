#risk_functions.py

def gen_board():
    """
    Generates the initial state of a game of World Domination Risk
    Possibly for certain other kinds as well
    Returns 4 things in a single tuple:
    1) initializes the risk board as a graph using dictionaries
    2) initializes the continents with their value and nodes
    3) initializes a pre-game state of the board
    """
    board = {
        #North America
        "Alaska":["NW_Territory","Alberta","Kamchatka"],
        "NW_Territory":["Greenland","Alberta","Ontario"],
        "Greenland":["E_Canada","NW_Territory","Ontario","Iceland"],
        "Alberta":["Alaska","Ontario","NW_Territory","W_US"],
        "Ontario":["NW_Territory","Greenland","Alberta","E_Canada","W_US","E_US"],
        "E_Canada":["Greenland","Ontario","E_US"],
        "W_US":["Alberta","Ontario","E_US","C_America"],
        "E_US":["E_Canada","Ontario","W_US","C_America"],
        "C_America":["W_US","E_US","Venezuela"],
        #South America
        "Venezuela":["C_America","Brazil","Peru"],
        "Brazil":["Venezuela","Argentina","Peru","N_Africa"],
        "Peru":["Brazil","Argentina","Venezuela"],
        "Argentina":["Brazil","Peru"],
        #Africa
        "N_Africa":["Brazil","Egypt","C_Africa","S_Europe","W_Europe","E_Africa"],
        "Egypt":["N_Africa","C_Africa","S_Europe","W_Europe"],
        "E_Africa":["N_Africa","C_Africa","S_Africa","Egypt","Mid_East","Madagascar"],
        "C_Africa":["N_Africa","E_Africa","S_Africa"],
        "S_Africa":["C_Africa","E_Africa","Madagascar"],
        "Madagascar":["S_Africa","E_Africa"],
        #Australia
        "Indonesia":["Siam","New_Guinea","W_Australia"],
        "New_Guinea":["E_Australia","W_Australia","Indonesia"],
        "W_Australia":["E_Australia","Indonesia","New_Guinea"],
        "E_Australia":["New_Guinea","W_Australia"],
        #Europe
        "Iceland":["Greenland","Great_Britain","Scandanavia"],
        "Great_Britain":["Iceland","Scandanavia","N_Europe", "W_Europe"],
        "Scandanavia":["Iceland","N_Europe","Russia", "Great_Britain"],
        "Russia":["Scandanavia","N_Europe","S_Europe","Mid_East","Afghanistan","Ural"],
        "N_Europe":["Russia","S_Europe","W_Europe","Scandanavia","Great_Britain"],
        "S_Europe":["W_Europe","N_Europe","Russia", "Mid_East","N_Africa", "Egypt"],
        "W_Europe":["N_Africa","S_Europe","N_Europe", "Great_Britain"],
        #Asia
        "Mid_East":["Afghanistan","India","Egypt","E_Africa","Russia","S_Europe"],
        "Afghanistan":["Ural","Mid_East","Russia","India","China"],
        "Ural":["Afghanistan","Russia","Siberia","China"],
        "Siberia":["","",""],
        "Yakutsk":["","",""],
        "Kamchatka":["","",""],
        "Irkutsk":["","",""],
        "Mongolia":["","",""],
        "Japan":["","",""],
        "China":["","",""],
        "India":["","",""],
        "Siam":["","",""]
        }

    #Continent name as key, with a list containing continent value and territories
    continents = {
        "N_America":[
            5,
            "Alaska",
            "NW_Territory",
            "Greenland",
            "Alberta",
            "Ontario",
            "E_Canada",
            "W_US",
            "E_US",
            "C_America"],
        "S_America":[
            2,
            "Venezuela",
            "Argentina",
            "Brazil",
            "Peru"],
        "Africa":[
            3,
            "Egypt",
            "Madagascar",
            "N_Africa",
            "E_Africa",
            "C_Africa",
            "S_Africa"],
        "Asia":[
            7,
            "Mid_East",
            "Afghanistan",
            "Ural",
            "Siberia",
            "Yakutsk",
            "Kamchatka",
            "Irkutsk",
            "Mongolia",
            "Japan",
            "China",
            "India",
            "Siam"],
        "Europe":[
            5,
            "Iceland",
            "Great_Britain",
            "Scandanavia",
            "Russia",
            "N_Europe",
            "S_Europe",
            "W_Europe"],
        "Australia":[
            2,
            "Indonesia",
            "New_Guinea",
            "W_Australia",
            "E_Australia"]
        }

    #initializes the initial state of the game
    #the game state is all the nodes, node owner, and army size per node
    territories = {
        #North America
        "Alaska":[0,0],
        "NW_Territory":[0,0],
        "Greenland":[0,0],
        "Alberta":[0,0],
        "Ontario":[0,0],
        "E_Canada":[0,0],
        "W_US":[0,0],
        "E_US":[0,0],
        "C_America":[0,0],
        #South America
        "Venezuela":[0,0],
        "Brazil":[0,0],
        "Peru":[0,0],
        "Argentina":[0,0],
        #Africa
        "N_Africa":[0,0],
        "Egypt":[0,0],
        "E_Africa":[0,0],
        "C_Africa":[0,0],
        "S_Africa":[0,0],
        "Madagascar":[0,0],
        #Australia
        "Indonesia":[0,0],
        "New_Guinea":[0,0],
        "W_Australia":[0,0],
        "E_Australia":[0,0],
        #Europe
        "Iceland":[0,0],
        "Great_Britain":[0,0],
        "Scandanavia":[0,0],
        "Russia":[0,0],
        "N_Europe":[0,0],
        "S_Europe":[0,0],
        "W_Europe":[0,0],
        #Asia
        "Mid_East":[0,0],
        "Afghanistan":[0,0],
        "Ural":[0,0],
        "Siberia":[0,0],
        "Yakutsk":[0,0],
        "Kamchatka":[0,0],
        "Irkutsk":[0,0],
        "Mongolia":[0,0],
        "Japan":[0,0],
        "China":[0,0],
        "India":[0,0],
        "Siam":[0,0]
        }

    #initializes the cards pre-start of game with their owner 'Y' is unused
    cards = {
        #North America
        "Alaska":'Y',
        "NW_Territory":'Y',
        "Greenland":'Y',
        "Alberta":'Y',
        "Ontario":'Y',
        "E_Canada":'Y',
        "W_US":'Y',
        "E_US":'Y',
        "C_America":'Y',
        #South America
        "Venezuela":'Y',
        "Brazil":'Y',
        "Peru":'Y',
        "Argentina":'Y',
        #Africa
        "N_Africa":'Y',
        "Egypt":'Y',
        "E_Africa":'Y',
        "C_Africa":'Y',
        "S_Africa":'Y',
        "Madagascar":'Y',
        #Australia
        "Indonesia":'Y',
        "New_Guinea":'Y',
        "W_Australia":'Y',
        "E_Australia":'Y',
        #Europe
        "Iceland":'Y',
        "Great_Britain":'Y',
        "Scandanavia":'Y',
        "Russia":'Y',
        "N_Europe":'Y',
        "S_Europe":'Y',
        "W_Europe":'Y',
        #Asia
        "Mid_East":'Y',
        "Afghanistan":'Y',
        "Ural":'Y',
        "Siberia":'Y',
        "Yakutsk":'Y',
        "Kamchatka":'Y',
        "Irkutsk":'Y',
        "Mongolia":'Y',
        "Japan":'Y',
        "China":'Y',
        "India":'Y',
        "Siam":'Y',
        #Wild cards
        "Wild_1":'Y',
        "Wild_2":'Y'
        }
    return (board, continents, territories, cards)

def parse_state_string(state_string):
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

def get_state_string(state):
    '''
    gets the state representation string from the state
    '''

    #the game state consist of 3 things
    #1) each territory's owner, and # of troops in them
    #2) the owner of each card
    #3) the number of Risk card sets that have been traded in 
    territories,cards,trade_ins = state

    #that state string will just be a really long string that
    #is all the things concatenated using
    #':' as a delimiter for categories
    #'!' between elements
    #'.' between parts of key-value pairs
    state_string = ""

    for key in territories:
        one,two = territories[key]
        state_string = state_string + key + "." + str(one) + "." + str(two) + "!"

    #remove the last '!'
    state_string = state_string[:-1]
    
    state_string = state_string + ":"
    for key in cards:
        state_string = state_string + key + "." + cards[key] + "!"

    #remove the last '!'
    state_string = state_string[:-1]

    state_string = state_string + ":" + trade_ins

    return state_string
