import pygame,ctypes
pygame.init()
user32 = ctypes.windll.user32

size = (user32.GetSystemMetrics(0),user32.GetSystemMetrics(1))#pour adapter la taille de l'écran et l'affichage pour tous ordis
pink = 201,100,100
black = 0,0,0
white = 255,255,255
position_x = 95
position_y = 95
square_x = position_x
square_y = position_y
colour_case = black
meter_x = 0
meter_y = 0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill(pink)
pygame.display.update()


while meter_y < 8:
    if (meter_x + meter_y)%2 == 0:
        colour_case = white
    else:
        colour_case = black

    pygame.draw.rect(screen, colour_case, [position_x, position_y, square_x, square_y])
    position_x += square_x
    meter_x += 1
    pygame.display.update()

    if meter_x == 8 and meter_y == 7:
        meter_y += 1
    
    elif meter_x == 8:
        position_y += square_y
        position_x += -(8*square_x)
        pygame.draw.rect(screen, colour_case, [position_x, position_y, 50, 50])
        meter_x = 0
        meter_y += 1
        pygame.display.update()
##Cette version 2.1.1 permet par ctypes d'adapter automatiquement la resolution et la taille de l'écran
##à la fenêtre
