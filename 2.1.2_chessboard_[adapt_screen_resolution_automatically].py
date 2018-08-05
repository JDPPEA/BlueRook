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

    pygame.draw.rect(screen, colour_case, [position_x, position_y, 50, 50])
    position_x += 50
    side_x += 1
    pygame.display.update()

    if side_x == 8 and side_y == 7:
        side_y += 1
    
    elif side_x == 8:
        position_y += 50
        position_x += -400
        pygame.draw.rect(screen, colour_case, [position_x, position_y, 50, 50])
        side_x = 0
        side_y += 1
        pygame.display.update()
        
##La fonction set_screen_prop() permet d'adapter l'écran
##de plus elle donne sa taille en info
