#pygame_map.py
#backgrounds and drawing polygons in pygame
#made with help from
#https://mail.python.org/pipermail/tutor/2005-November/043001.html

import pygame

pygame.init()
pygame.display.set_caption("pygame_map.py")
clock = pygame.time.Clock()

#set a background for the screen
background = pygame.image.load("board.bmp")
size = background.get_size()
screen = pygame.display.set_mode(size)
backgroundRect = background.get_rect()
screen.blit(background, backgroundRect)

white = (255,255,255)
red = (255,0,0)

#pygame.draw.circle(Surface, color, pos, radius)
positions = [
    (80,120), #alask
    (220,140), #nw ter
    (440,100), #greenland
    (180,180), #alber
    (240,200), #ontar
    (340,200), #queb
    (200,260), #w us
    (280,270), #e us
    (235,320), #mex
    (355,370), #ven
    (430,430), #bra
    (355,440), #peru
    (370,500), #arg
    (520,320), #n af
    (620,305), #egy
    (640,345), #e af
    (610,390), #congo
    (610,460), #s af
    (690,450), #mada
    (930,390), #indo
    (1030,405), #new g
    (960,470), #west aus
    (1050,480), #e aus
    (490,150), #iceland
    (515,200), #g brit
    (570,150), #swed
    (650,190), #russ
    (570,210), #n eu
    (610,240), #south e
    (515,250), #w eu
    (680,280), #mid e
    (750,230), #afghan
    (800,150), #ural
    (860,110), #siberia
    (980,110), #yak
    (1120,130), #kam
    (920,180), #irk
    (960,230), #mongol
    (1030,260), #jap
    (920,280), #china
    (800,310), #india
    (885,330) #siam
    ]

[pygame.draw.circle(screen,white,(x,y),14, 0) for x,y in positions]
    

done = False
index = 0

while not done:
    for event in pygame.event.get():
        
        pygame.draw.circle(screen,red,positions[index%42],14, 0)

        index+=1

        if event.type == pygame.QUIT:
            done=True

        pygame.display.flip()
        
        clock.tick(1)
    
