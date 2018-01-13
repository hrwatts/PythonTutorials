'''
Generates the graphics for Risk game
Note: this is not needed to play
'''

import pygame
import risk_environment as risk

class Game(object):
    '''a game object is the graphics for the reinforcement learning agent Risk game'''

    def __init__(self, init_state):
        self.state = init_state
        self.play()
        
    def play(self):
        '''begins the game'''

        pygame.init()

        #name game window
        pygame.display.set_caption("Risk Reinforcement Learning Project")

        #load image and make background
        background = pygame.image.load("board.bmp")
        size = background.get_size()
        screen = pygame.display.set_mode(size)
        backgroundRect = background.get_rect()
        screen.blit(background, backgroundRect)

        #get fonts working
        pygame.font.init()
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, 12)

        #get game clock
        clock = pygame.time.Clock()

        #get some colors
        colors = gen_colors()

        #get positions
        positions = gen_positions()

        #get colors per player id
        p2c = player_colors()

        done = False
        while not done:

            #when update is called, this part will pull most up to date info
            order, territories, cards, trade_ins = self.state

            #color nodes by owner, and place troop text in node
            for ter_id in territories:
                #coords
                x,y = positions[ter_id]
                
                #color
                player,troops = territories[ter_id]
                pygame.draw.circle(screen,colors[p2c[player]],(x,y),14, 0)

                #text
                label = font_renderer.render(str(troops),1,black)
                screen.blit(label,(x-12,y-6))
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done=True

            #update display, and moderate frame rate to 1fps
            pygame.display.flip()
            clock.tick(1)

    def update(self,state):
        '''used in conjucture with game environment to update display'''
        self.state=state

    def gen_positions(self):
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

    def gen_colors(self):
        '''returns a dictionary of RGB colors to be used in game'''

        colors = {
            "red":(255,0,0),
            "green":(0,255,0),
            "blue":(0,0,255),
            "yellow":(255,255,0),
            "purple":(255,0,255),
            "orange":(255,128,0),
            "white":(255,255,255),
            "black":(0,0,0)
            }

        return colors

    def player_colors():
        '''assigned players colors for the game'''

        p2c = {0:"red",1:'green',2:'blue',3:'yellow',4:'purple',5:'orange'}

        return p2c
