import pygame,ctypes


def set_screen_prop():
    user32 = ctypes.windll.user32
    screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screenSize)
    size = (screenSize)
    pygame.display.set_caption("Window")
    return pygame.display.set_mode((size) , pygame.FULLSCREEN)

pygame.init()

screen = set_screen_prop()
pink = 201,100,100
black = 0,0,0
white = 255,255,255
position_x = 50
position_y = 50
square_x = position_x
square_y = position_y
colour_case = black
side_x = 0
side_y = 0

screen.fill(pink)
pygame.display.update()


while side_y < 8:
    if (side_x + side_y)%2 == 0:
        colour_case = white
    else:
        colour_case = black

    pygame.draw.rect(screen, colour_case, [position_x, position_y, square_x, square_y])
    position_x += square_x
    side_x += 1
    pygame.display.update()

    if side_x == 8 and side_y == 7:
        side_y += 1
    
    elif side_x == 8:
        position_y += square_y
        position_x += -(8*square_x)
        pygame.draw.rect(screen, colour_case, [position_x, position_y, square_x, square_y])
        side_x = 0
        side_y += 1
        pygame.display.update()

##remplacement des 50 lignes 36 et 47, par square_x et square_y
