import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Summer Cards')
#pygame.display.set_icon('Assets/icon.png')

while True:
    screen.fill((255, 127, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()