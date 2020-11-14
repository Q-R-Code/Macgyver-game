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
    maze.print_maze(screen)
    pygame.display.flip()

    if pressed.get(pygame.K_RIGHT) and macgyver.rect.x + 60 < 900:
        macgyver.move_right()
    elif pressed.get(pygame.K_LEFT) and macgyver.rect.x > 0:
        macgyver.move_left()
    elif pressed.get(pygame.K_UP) and macgyver.rect.y > 0:
        macgyver.move_up()
    elif pressed.get(pygame.K_DOWN) and macgyver.rect.y + 60 < 900:
        macgyver.move_down()


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")

        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pressed[event.key] = False
