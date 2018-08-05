import pygame
pygame.init()

size = (1920,1080)
pink = 201,100,100

screen = pygame.display.set_mode(size)
screen.fill(pink)
pygame.display.update()

##Cette version 1.1 permet d'afficher une fenêtre à taille[size] et couleurs[système RGB] modulables
