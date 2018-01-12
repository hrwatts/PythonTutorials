#pygame.text.py
#working with text in pygame
#with help from
#https://stackoverflow.com/questions/20550743/pygame-how-to-write-text-onto-a-specific-location-also-how-to-use-coordinate

import pygame

#start pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

# Initialize the font system and create the font and font renderer
pygame.font.init()
#using the defualt font
default_font = pygame.font.get_default_font()
#object that will generate surfaces, arguments are font and font size
font_renderer = pygame.font.Font(default_font, 8)

#create a surface which will be the text
#"string" what you want the text to say
#boolean with or without anti aliasing (True is with)
#then RGB color
white = (255,255,255)
label = font_renderer.render("Some Text",1,white)

#blit the surface with text to the surface you use as the screen
#and the location you want it to be (x,y) top left corner
screen.blit(label,(0,0))


#main loop
done = False

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done=True

        pygame.display.flip()
        
        clock.tick(1)
