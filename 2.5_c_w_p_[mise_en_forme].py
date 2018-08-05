#------IMPORT--------:
import pygame,ctypes

#------VARIABLES-----:
#ECRAN:
pink = 201,100,100
black = 0,0,0
white = 255,255,255
#CASES
position_x = 88
position_y = 88

#--------------------------------FONCTION---------------------------------------------------------------------------:
def set_screen_prop():  #fct pour adapter la fenetre à l'écran sous Window
    user32 = ctypes.windll.user32
    screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screenSize)
    size = (screenSize)
    pygame.display.set_caption("Window")
    return pygame.display.set_mode((size) , pygame.FULLSCREEN)

def chessboard():
    global position_x, position_y
    position_x = 88
    position_y = 88
    square_x = position_x
    square_y = position_y
    colour_case = black
    side_x = 0
    side_y = 0

    while side_y < 8:
        if (side_x + side_y)%2 == 0:
            colour_case = white
        else:
            colour_case = black

        pygame.draw.rect(screen, colour_case, [position_x, position_y, square_x, square_y])
        position_x += square_x
        side_x += 1

        if side_x == 8 and side_y == 7:
            side_y += 1
        
        elif side_x == 8:
            position_y += square_y
            position_x += -(8*square_x)
            pygame.draw.rect(screen, colour_case, [position_x, position_y, square_x, square_y])
            side_x = 0
            side_y += 1


#-------DEMARRAGE--------:
pygame.init()               
screen = set_screen_prop()    

#----------------CHARGEMENT-IMAGES-PIECES-----------------:
black_rook = pygame.image.load("black_rook.png")

#----------------SET-UP-------------------:
screen.fill(pink)
chessboard()
pygame.display.update()

#---------AFFICHAGE-PIECES-------:
screen.blit(black_rook, (88,88))
pygame.display.update()

#Cette version 2.5 est une remise en page pour une meilleur lisibilité

