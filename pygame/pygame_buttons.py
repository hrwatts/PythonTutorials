#pygame_buttons.py
#Demo the use of buttons in pygame
#Made from a tutorial I got here
#https://pythonprogramming.net/pygame-buttons-part-1-button-rectangle/
#and
#http://www.nerdparadise.com/programming/pygame/part1

import pygame

#must initialize pygame
#It initializes all the modules required for PyGame.
pygame.init()

#display pixels (width,height)
display_dimensions = (800,600)

#colors are RGB tuples
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)

#to create the display give the x,y params as a tuple
#This will launch a window of the desired size. The return value is a Surface 
screen = pygame.display.set_mode(display_dimensions)

#set the text that appears on the top of the window
pygame.display.set_caption("Demo Game Title")

#pygame will run as fast as your computer can make it
#which is probably really fast
#instead, we can set the clock frame rate using
#this to make a more workable rate
clock = pygame.time.Clock()

#there aren't any keywords that start pygame, at this point it is already running
#so you can interact with the display by sending things to the display

#this is the basic game-loop

done = False
colored_red = True
x=0
y=0

while not done:

    #this empties the event queue.
    #If you do not call this, the windows messages will start to pile up
    #and it will become unresponsive
    #NOTE: this also means an event must take place before the game
    #will run any code in this loop
    for event in pygame.event.get():


        #you would run content here <-
        #such as drawing this rectangle

        #screen is the Surface object from pygame.display.set_mode(display_dimensions)
        #then the color (defined above)
        #and then pygame.Rect(X,Y,H,W) X and Y are the coords for top left corner
        #H and W are the height and Width of the rectangle

        #I also added this if statement to change the color
        #and made it move
        x+=10
        y+=9
        if colored_red:
            pygame.draw.rect(screen, red, pygame.Rect(x%600, y%600, 60, 60))
            colored_red=False
        else:
            pygame.draw.rect(screen, green, pygame.Rect(x%600, y%600, 60, 60))
            colored_red=True
        

        #if the event is pygame.QUIT()
        #then this will set the var that will end the while loop
        if event.type == pygame.QUIT:
            
            done = True

    #PyGame is double-buffered. This swaps the buffers.
    #All you need to know is that this call is required
    #in order for any updates that you make to the
    #game screen to become visible.
    pygame.display.flip()

    #this is what will adjust the framerate
    #it will block execution for 1/60th of a second will
    #have passed, making it 60fps
    clock.tick(600)
