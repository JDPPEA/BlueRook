import pygame
pygame.init()

size = (640,480)
pink = 201,100,100

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill(pink)
pygame.display.update()


##Cette version 1.2 permet d'afficher la fenêtre en grand écran sur l'ordinateur
##par la méthode pygame.FULLSCREEN
##par cette méthode [size] devient la résolution de la fenêtre
