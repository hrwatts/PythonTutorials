"""
this is the base agent for playing the
World Domination version of Risk
you can't really play the game with this
see it's sub-classes for actual functionality
"""

class BaseAgent(object):
    """A base agent for Risk"""

    def __init__(self, player, order):
        '''
        you must initialize a Risk player
        with a small amount of info
        (player) what player they are
        (order) what turn order they are (0-># of players-1)
        '''
        
        self.player = player
        self.order = order

    def recruit_troops(self, territories, continents):
        '''
        this calculates and returns the number of troops the player
        recieves at the beginning of their turn not including card sets
        '''

        recuit = 0

        #get the territories this player controls
        t_owned = [t for t in territories if territories[t][0]==self.player]

        #count them
        t_count = len(t_owned)

        #Risk rules then floor divide by 3
        t_count = t_count//3

        #and you always get at least 3 troops from this
        if t_count<3:
            t_count=3

        #now add to amount recruited
        recuit+=t_count

        #calculate for continents
        for continent in continents:
            c_owned=True
            for territory in continents[continent][1:]:
                if territory not in t_owned:
                    c_owned=False

            #if you own the continent, then get the troops
            #allocated for that continent (stored in position 0)
            if c_owned:
                recuit += continents[continent][0]

        return recuit

    def get_sets(self, cards, card_faces, debug=False):

        #now you have the total troops recruited from these areas
        #but there is still the trade ins to consider
        #what this will return is any combination of cards
        #the player owns that may be traded in
        #valid sets are
        #any 3 of same kind
        #1 for 1,5,10
        #any 2 and a wild
        c_owned = [c for c in cards if cards[c]==self.player]

        if debug:
            print("DEBUG C_O:", c_owned)

        set_list = []

        one = []
        five = []
        ten = []
        wild = []
        for card in c_owned:
            if card_faces[card] == 1:
                one.append(card)
            elif card_faces[card] == 5:
                five.append(card)
            elif card_faces[card] == 10:
                ten.append(card)
            else:
                wild.append(card)

        if debug:
            print("DEBUG 1s:", one)
            print("DEBUG 5s:", five)
            print("DEBUG 10s:", ten)
            print("DEBUG Wilds:", wild)

        #this calculates 3 of same kind
        if len(one)>=3:
            #in cases such as these there is no need to consider 3+
            #since any 1 is as good as another 1
            #append the first 3, if there are more than 3
            #deal with it else where
            set_list.append(one[:3])
        if len(five)>=3:
            set_list.append(five[:3])
        if len(ten)>=3:
            set_list.append(ten[:3])

        #calculates one of each kind
        if len(one)>=2 and len(five)>=2 and len(ten)>=2:
            #either you have two
            set_list.append([one[0],five[0],ten[0]])
            set_list.append([one[1],five[1],ten[1]])
        elif len(one)>=1 and len(five)>=1 and len(ten)>=1:
            #or you have just one
            set_list.append([one[0],five[0],ten[0]])

        #calculates wildcard sets
        for wc in wild:
            if len(one)>=2:
                #two of ones
                set_list.append([one[0], one[1], wc])
            if len(five)>=2:
                #two of fives
                set_list.append([five[0], five[1], wc])
            if len(ten)>=2:
                #two of tens
                set_list.append([ten[0], ten[1], wc])
            if len(one)!=0 and len(five)!=0:
                #one 1 and one 5
                set_list.append([one[0], five[0], wc])
            if len(one)!=0 and len(ten)!=0:
                #one 1 and one 10
                set_list.append([one[0], ten[0], wc])
            if len(ten)!=0 and len(five)!=0:
                #one 5 and one 10
                set_list.append([ten[0], five[0], wc])

        return set_list
