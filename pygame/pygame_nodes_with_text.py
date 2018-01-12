#pygame_nodes_with_text.py
#just a combination of drawing polygons and text to screen

import pygame

pygame.init()
pygame.display.set_caption("pygame_nodes_with_text.py")
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

#fonts
pygame.font.init()
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 12)

#colors
black = (0,0,0)
white = (255,255,255)

#nodes
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
pos_dict = dict(zip(range(42),positions))


#main loop
done = False
count = 0

while not done:
    for event in pygame.event.get():

        #should draw circles so as to white out old text
        [pygame.draw.circle(screen,white,(x,y),14, 0) for x,y in positions]

        #draw black text to positions
        label = font_renderer.render(str(count),1,black)

        for x,y in positions:
            screen.blit(label,(x-12,y-6))

        count+=50

        if event.type == pygame.QUIT:
            done=True

        pygame.display.flip()
        
        clock.tick(1)
