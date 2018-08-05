import pygame
pygame.init()

resolution = (640,480)
pink = 201,100,100
black = 0,0,0
position_x = 50
position_y = 50
colour_case = black


screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
screen.fill(pink)
pygame.display.update()


pygame.draw.rect(screen, colour_case, [position_x, position_y, 50, 50])
pygame.display.update()

##Cette version 1.3 permet d'afficher le premier [square] au-dessus de [screen]
##On notera que [size] à été remplacé, comme expliqué dans v 1.2
