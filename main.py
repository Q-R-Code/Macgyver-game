#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from maze_map import Maze
from constantes import *

pygame.init()

pygame.display.set_caption("MacGyver GO GO GO")

screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))
background = pygame.image.load("images/background.png")

running = True

while running:
    screen.blit(background, (0, 0))
    maze = Maze()
    maze.generate()
    maze.print(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")
