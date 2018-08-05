#------IMPORT--------:
import pygame,ctypes
from pygame.locals import*# ajout pour QUIT

#------VARIABLES-----:
#ECRAN:
blue = 9,44,198
brown = 125,88,76
white = 237,235,235
#CASES
empty = 0
position_x = 95
position_y = 95
square_x = position_x
square_y = position_y
#_PIECES:
br1x = 95
br1y = 95

#---------------------------------FONCTION-------------------------------------------------:
def set_screen_prop():  #fct pour adapter la fenetre à l'écran sous Window
    user32 = ctypes.windll.user32
    screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screenSize)
    size = (screenSize)
    pygame.display.set_caption("Window")
    return pygame.display.set_mode((size) , pygame.FULLSCREEN)

def chessboard():
    global position_x, position_y
    position_x = 95
    position_y = 95
    square_x = position_x
    square_y = position_y
    colour_case = brown 
    side_x = 0
    side_y = 0

    while side_y < 8:
        if (side_x + side_y)%2 == 0:
            colour_case = white
        else:
            colour_case = brown

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

def refresh():
    screen.fill(blue)
    chessboard()
    screen.blit(black_rook_r, (br1x,br1y))
    screen.blit(black_rook_l,square["h8"])
    screen.blit(black_knight_r,square["b8"])
    screen.blit(black_knight_l,square["g8"])
    screen.blit(black_bishop_r,square["c8"])
    screen.blit(black_bishop_l,square["f8"])
    screen.blit(black_queen,square["d8"])
    screen.blit(black_king,square["e8"])
    screen.blit(black_pawn_1,square["h7"])
    screen.blit(black_pawn_2,square["g7"])
    screen.blit(black_pawn_3,square["f7"])
    screen.blit(black_pawn_4,square["e7"])
    screen.blit(black_pawn_5,square["d7"])
    screen.blit(black_pawn_6,square["c7"])
    screen.blit(black_pawn_7,square["b7"])
    screen.blit(black_pawn_8,square["a7"])

    screen.blit(white_rook_r, square["a1"])
    screen.blit(white_rook_l,square["h1"])
    screen.blit(white_knight_r,square["b1"])
    screen.blit(white_knight_l,square["g1"])
    screen.blit(white_bishop_r,square["c1"])
    screen.blit(white_bishop_l,square["f1"])
    screen.blit(white_queen,square["d1"])
    screen.blit(white_king,square["e1"])
    screen.blit(white_pawn_1,square["h2"])
    screen.blit(white_pawn_2,square["g2"])
    screen.blit(white_pawn_3,square["f2"])
    screen.blit(white_pawn_4,square["e2"])
    screen.blit(white_pawn_5,square["d2"])
    screen.blit(white_pawn_6,square["c2"])
    screen.blit(white_pawn_7,square["b2"])
    screen.blit(white_pawn_8,square["a2"])
        
    pygame.display.update()

#-------DEMARRAGE--------:
pygame.init()               
screen = set_screen_prop()   

#----------------CHARGEMENT-IMAGES-PIECES-----------------:
black_rook_r = pygame.image.load("black_rook.png")
black_rook_l = pygame.image.load("black_rook.png")
black_bishop_r = pygame.image.load("black_bishop.png")
black_bishop_l = pygame.image.load("black_bishop.png")
black_knight_r = pygame.image.load("black_knight.png")
black_knight_l = pygame.image.load("black_knight.png")
black_queen = pygame.image.load("black_queen.png")
black_king = pygame.image.load("black_king.png")
black_pawn_1 = pygame.image.load("black_pawn.png")
black_pawn_2 = pygame.image.load("black_pawn.png")
black_pawn_3 = pygame.image.load("black_pawn.png")
black_pawn_4 = pygame.image.load("black_pawn.png")
black_pawn_5 = pygame.image.load("black_pawn.png")
black_pawn_6 = pygame.image.load("black_pawn.png")
black_pawn_7 = pygame.image.load("black_pawn.png")
black_pawn_8 = pygame.image.load("black_pawn.png")
white_rook_r= pygame.image.load("white_rook.png")
white_rook_l = pygame.image.load("white_rook.png")
white_bishop_r = pygame.image.load("white_bishop.png")
white_bishop_l = pygame.image.load("white_bishop.png")
white_knight_r = pygame.image.load("white_knight.png")
white_knight_l = pygame.image.load("white_knight.png")
white_queen = pygame.image.load("white_queen.png")
white_king = pygame.image.load("white_king.png")
white_pawn_1 = pygame.image.load("white_pawn.png")
white_pawn_2 = pygame.image.load("white_pawn.png")
white_pawn_3 = pygame.image.load("white_pawn.png")
white_pawn_4 = pygame.image.load("white_pawn.png")
white_pawn_5 = pygame.image.load("white_pawn.png")
white_pawn_6 = pygame.image.load("white_pawn.png")
white_pawn_7 = pygame.image.load("white_pawn.png")
white_pawn_8 = pygame.image.load("white_pawn.png")

#---------------DICTIONNAIRES-----------------------------------:
#CASES:
square = {
          "a8":(95,95),  "b8":(190,95),  "c8":(285,95),  "d8":(380,95),  "e8":(475,95),  "f8":(570,95),  "g8":(665,95),  "h8":(760,95),
          "a7":(95,190), "b7":(190,190), "c7":(285,190), "d7":(380,190), "e7":(475,190), "f7":(570,190), "g7":(665,190), "h7":(760,190),
          "a6":(95,285), "b6":(190,285), "c6":(285,285), "d6":(380,285), "e6":(475,285), "f6":(570,285), "g6":(665,285), "h6":(760,285),
          "a5":(95,380), "b5":(190,380), "c5":(285,380), "d5":(380,380), "e5":(475,380), "f5":(570,380), "g5":(665,380), "h5":(760,380),
          "a4":(95,475), "b4":(190,475), "c4":(285,475), "d4":(380,475), "e4":(475,475), "f4":(570,475), "g4":(665,475), "h4":(760,475),
          "a3":(95,570), "b3":(190,570), "c3":(285,570), "d3":(380,570), "e3":(475,570), "f3":(570,570), "g3":(665,570), "h3":(760,570),
          "a2":(95,665), "b2":(190,665), "c2":(285,665), "d2":(380,665), "e2":(475,665), "f2":(570,665), "g2":(665,665), "h2":(760,665),
          "a1":(95,760), "b1":(190,760), "c1":(285,760), "d1":(380,760), "e1":(475,760), "f1":(570,760), "g1":(665,760), "h1":(760,760)
          }

#PIECES-CASES:
piece_square = {
                "a8":black_rook_r, "b8":black_knight_r, "c8":black_bishop_r, "d8":black_queen,  "e8":black_king,   "f8":black_bishop_l, "g8":black_knight_l, "h8":black_rook_l,
                "a7":black_pawn_1, "b7":black_pawn_2,   "c7":black_pawn_3,   "d7":black_pawn_4, "e7":black_pawn_5, "f7":black_pawn_6,   "g7":black_pawn_7,   "h7":black_pawn_8,
                "a6":empty,        "b6":empty,          "c6":empty,          "d6":empty,        "e6":empty,        "f6":empty,          "g6":empty,          "h6":empty,
                "a5":empty,        "b5":empty,          "c5":empty,          "d5":empty,        "e5":empty,        "f5":empty,          "g5":empty,          "h5":empty,
                "a4":empty,        "b4":empty,          "c4":empty,          "d4":empty,        "e4":empty,        "f4":empty,          "g4":empty,          "h4":empty,
                "a3":empty,        "b3":empty,          "c3":empty,          "d3":empty,        "e3":empty,        "f3":empty,          "g3":empty,          "h3":empty,
                "a2":white_pawn_1, "b2":white_pawn_2,   "c2":white_pawn_3,   "d2":white_pawn_4, "e2":white_pawn_5, "f2":white_pawn_6,   "g2":white_pawn_7,   "h2":white_pawn_8,
                "a1":white_rook_r, "b1":white_knight_r, "c1":white_bishop_r, "d1":white_queen,  "e1":white_king,   "f1":white_bishop_l, "g1":white_knight_l, "h1":white_rook_l
                }
    
#----------------SET-UP-------------------:
refresh()

pygame.display.flip()

follow = 1
while follow:
    for event in pygame.event.get():
        if event.type == QUIT:
            follow == 0
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                br1x = event.pos[0]
                br1y = event.pos[1]
    refresh()           
    

#Cette version 3.2 simplifie le set up grâce au remplacement par refresh()

