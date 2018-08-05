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
        break

##Cette version 1.5 de chessboard affiche une ligne de carrés isométriques blanc et noir
##pour ce faire la boucle while partage les carrés, blanc puis noir,
##comme paires et impaires
