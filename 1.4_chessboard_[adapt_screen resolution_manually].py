import pygame
pygame.init()

resolution = (1534,720)
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

##essai :[resolution] a été manuellement adapter à l'écran de mon laptop
