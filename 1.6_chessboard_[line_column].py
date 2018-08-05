import pygame
pygame.init()

resolution = (1534,720)
pink = 201,100,100
black = 0,0,0
white = 255,255,255
position_x = 50
position_y = 50
colour_case = black
side_x = 0
side_y = 0

screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
screen.fill(pink)



while side_y < 8:
    if (side_x + side_y)%2 == 0:
        colour_case = white
    else:
        colour_case = black

    pygame.draw.rect(screen, colour_case, [position_x, position_y, 50, 50])
    position_x += 50
    side_x += 1
    pygame.display.update()
    
    if side_x == 8:
        position_y += 50
        position_x += -400
        pygame.draw.rect(screen, colour_case, [position_x, position_y, 50, 50])
        side_x = 0
        side_y += 1
        pygame.display.update()

##Cette version 1.6 apporte par le [if] supplémentaire le reste de l'échiquier
##les lignes se crées en serpent, en reculant lignes 7, 5, 3, 1
##Il reste encore une case à patcher
        
