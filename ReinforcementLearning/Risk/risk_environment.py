'''
This class represents the game environment (the board)
of Risk using standard World Domination ruleset
See instructions https://www.hasbro.com/common/instruct/risk.pdf
'''

class Risk:
    '''Game Environment for Risk World Domination'''

    def __init__(self):     
        self.node2name, self.name2node = self.id_names()
        self.board, self.continents, self.trade_vals, self.card_faces = self.gen_board()
        self.state = self.gen_init_state()


    def id_names(self):
        """returns helpful 2-way dictionaries for territories"""
        
        names = [
            #North America
            "Alaska","NW_Territory","Greenland","Alberta",
            "Ontario","Quebec","W_US","E_US","C_America",
            #South America
            "Venezuela","Brazil","Peru","Argentina",
            #Africa
            "N_Africa","Egypt","E_Africa","Congo","S_Africa","Madagascar",
            #Australia
            "Indonesia","New_Guinea","W_Australia","E_Australia",
            #Europe
            "Iceland","Great_Britain","Scandanavia",
            "Ukraine","N_Europe","S_Europe","W_Europe",
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

        return (node2name,name2node)

    def gen_board(self):
        """
        Generates the environment of the board
        """
        
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


        #the army size presented on the front of the Risk card
        #99 is wild card
        card_faces = {0:1,1:10,2:5,3:1,4:5,5:10,6:1,7:10,8:5,9:10,10:10,
                      11:5,12:1,13:1,14:1,15:10,16:5,17:10,18:1,19:5,20:5,
                      21:10,22:1,23:1,24:5,25:10,26:10,27:5,28:5,29:1,30:10,
                      31:1,32:5,33:10,34:5,35:5,36:1,37:10,38:1,39:5,40:1,
                      41:10,42:99,43:99}

        trade_vals = [0,4,6,8,10,15,20,25,30,35,40,45,50,55,60]

        return (board, continents, trade_vals, card_faces)

    def gen_init_state(self):
        '''generates the initial state of the game'''
        
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

        #initializes the cards pre-start of game with their owner
        #6=unused card, 7=used card (max of 6 player per game)
        cards = {
            0:6,1:6,2:6,3:6,4:6,5:6,6:6,7:6,8:6,9:6,
            10:6,11:6,12:6,13:6,14:6,15:6,16:6,17:6,18:6,19:6,
            20:6,21:6,22:6,23:6,24:6,25:6,26:6,27:6,28:6,29:6,
            30:6,31:6,32:6,33:6,34:6,35:6,36:6,37:6,38:6,39:6,
            40:6,41:6,42:6,43:6
            }

        # 0 for number of card sets turned in
        return (territories, cards, 0)

    def parse_state(self, state_string, debug=False):
        '''
        gets the state from the state representation string
        set debug=True for debugging 
        '''

        territories = {}
        cards = {}
        trade_ins = 0

        state_string = str(state_string)
        #deconstruct the state_string
        for id_num in range(44):
            
            if debug:
                print("DEBUG ID:", id_num, state_string[:10])
                
            if id_num!=0:
                #remove the next id #, the leading 0 is implied
                state_string = state_string[len(str(id_num)):]
            if id_num<42:
                #parses the card owner, then territory owner, then troop count
                
                c_owner = state_string[0]
                t_owner = state_string[1]
                
                state_string = state_string[2:] #don't need them anymore

                #there is a slightly complicated way in which troop numbers need to be parsed
                #to avoid errors
                #for example if there were 102 troops in territory 2 then the beginning of the state string
                #may look like 1020200310234 is valid and it may
                #generate errors relying solely on my trailing 0 delimiter
                #NOTE: this does NOT eliminated the problems when parsing the state_string
                #merely reduces the chance of one from occuring

                troops=""

                unsolved = True

                while(unsolved):
                    nid=str(id_num+1)
                    nid_loc=state_string.find("0"+nid)
                    temp_c_owner = int(state_string[nid_loc+1+len(nid)])
                    temp_t_owner = int(state_string[nid_loc+2+len(nid)])
                    temp_non_zero = int(state_string[nid_loc+3+len(nid)])
                
                    if temp_c_owner<8 and temp_t_owner<6 and temp_non_zero!=0 and nid!="42":
                        #if this is true, then it is much more unlikely to have a bad parse
                        troops = troops + state_string[:nid_loc]
                        state_string = state_string[nid_loc+1:]
                        unsolved = False
                        
                    elif nid=="42":
                        #on id_num 41 nid = 42 which is a wild card and must be handed differently
                        if debug:
                            print("Debug ID:",id_num,"C_O:",temp_c_owner,"T_O:",temp_t_owner,"non0:",state_string[:10])
                        if temp_c_owner<8 and temp_t_owner==4 and temp_non_zero==3:
                            troops = troops + state_string[:nid_loc]
                            state_string = state_string[nid_loc+1:]
                            unsolved = False
                    else:
                        #this is the error handling part
                        #when a difficult parsing situation occurs, it's handled here
                        #it will go to the trouble location (what is throwing a false parse)
                        #and go ahead and add that to troops, then tries to parse again
                        if debug:
                            print("Debug ID:",id_num,"C_O:",temp_c_owner,"T_O:",temp_t_owner,"non0:",state_string[:10])
                        troops = troops + state_string[:nid_loc+1]
                        state_string = state_string[nid_loc+1:]

                troops = int(troops)
                territories[id_num] = [t_owner,troops]
                cards[id_num] = c_owner

            else:
                #must be a wild card (42/43)
                c_owner = int(state_string[0])
                state_string = state_string[1:]
                cards[id_num] = c_owner

        trade_ins=int(state_string) #if it parses correctly, this should be all that remains

        if trade_ins>15:
            #trade ins go up to 15 possibilities
            print(territories)
            print("*"*50)
            print(cards)
            print("*"*50)
            print(trade_ins)
            raise ValueError('Parsed incorrectly or impossible trade in value')

        return (territories, cards, trade_ins) #this is what a state consist of

    def get_state(self, state):
        '''
        gets the state representation from the state
        state = (territories, cards, trade_ins)
        '''

        territories, cards, trade_ins = state

        state_string = ""
        
        for key in range(44):
            if key in territories:
                t_owner,troops = territories[key]
                c_owner = cards[key]
                state_string = state_string + str(key)+str(c_owner)+str(t_owner)+str(troops)+"0"
            else:
                #must be wildcard (key 42/43)
                owner = cards[key]
                state_string = state_string + str(key)+str(owner)

        state_string = state_string + str(trade_ins)

        state_string = int(state_string)

        return state_string

    def pygame_positions(self):
        '''returns a dictionary that matches ID to node positions in pygame'''

        positions = [
            (80,120), (220,140), (440,100), (180,180), (240,200),
            (340,200), (200,260), (280,270), (235,320), (355,370),
            (430,430), (355,440), (370,500), (520,320), (620,305),
            (640,345), (610,390), (610,460), (690,450), (930,390),
            (1030,405), (960,470),(1050,480), (490,150), (515,200),
            (570,150), (650,190), (570,210), (610,240), (515,250),
            (680,280), (750,230), (800,150), (860,110), (980,110),
            (1120,130), (920,180),(960,230), (1030,260), (920,280),
            (800,310), (885,330)]

        return dict(zip(range(42),positions))