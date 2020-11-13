#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from maze_map import Maze
from constantes import *
from characters import Macgyver, Guardian

pygame.init()
pygame.display.set_caption("MacGyver GO GO GO")
screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))
background = pygame.image.load("images/background.png")

macgyver = Macgyver()
pressed = {}

guardian = Guardian()

running = True

while running:
    screen.blit(background, (0, 0))
    screen.blit(macgyver.image, macgyver.rect)
    screen.blit(guardian.image, guardian.rect)
    maze = Maze()
    maze.generate()
    maze.print(screen)
    pygame.display.flip()

    if pressed.get(pygame.K_RIGHT) and macgyver.rect.x != maze.print(wall):
        macgyver.move_right()


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")
