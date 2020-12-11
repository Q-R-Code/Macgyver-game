#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines two classes :
* Macgyver, the hero, with 4 methods for the moves, and one for the counter and the objects.
* Guardian, the boss
"""

import pygame

from game.constantes import taille_perso, taille_sprite, macgyver_right, macgyver_left, macgyver_up, macgyver_down, \
    guardian
from game.maze_map import Maze
from game.objects import Objects


class Macgyver(pygame.sprite.Sprite):
    """
    We generate Macgyver directly with Pygame. For each moves, it checks if the next box is a  wall.
    """

    def __init__(self, maze: Maze):
        super().__init__()
        self.maze = maze
        self.image = macgyver_right
        self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))
        self.rect = self.image.get_rect()
        self.case_x = 0
        self.case_y = 14
        self.x = 0
        self.y = 845
        self.counter = []

    def move_right(self):
        if self.maze.structure[self.case_y][self.case_x + 1] != "W":
            self.case_x += 1
            self.image = macgyver_right
            self.image = self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))
            self.x = self.case_x * taille_sprite
            self.rect = self.image.get_rect()

    def move_left(self):
        if self.maze.structure[self.case_y][self.case_x - 1] != "W":
            self.image = macgyver_left
            self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))
            self.case_x -= 1
            self.x = self.case_x * taille_sprite

    def move_up(self):
        if self.maze.structure[self.case_y - 1][self.case_x] != "W":
            self.image = macgyver_up
            self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))
            self.case_y -= 1
            self.y = self.case_y * taille_sprite

    def move_down(self):
        if self.maze.structure[self.case_y + 1][self.case_x] != "W":
            self.image = macgyver_down
            self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))
            self.case_y += 1
            self.y = self.case_y * taille_sprite

    def check_object(self, object1: Objects, object2: Objects, object3: Objects):
        """
        If its an object, transform the objects sprite, replace the box as empty and add "*" to the counter list.

        """
        if self.maze.structure[self.case_y][self.case_x] == "*1":
            self.maze.structure[self.case_y][self.case_x] = "O"
            object1.image = pygame.transform.scale(self.image, (0, 0))
            self.counter.append("*")
        elif self.maze.structure[self.case_y][self.case_x] == "*2":
            self.maze.structure[self.case_y][self.case_x] = "O"
            object2.image = pygame.transform.scale(self.image, (0, 0))
            self.counter.append("*")
        elif self.maze.structure[self.case_y][self.case_x] == "*3":
            self.maze.structure[self.case_y][self.case_x] = "O"
            object3.image = pygame.transform.scale(self.image, (0, 0))
            self.counter.append("*")


class Guardian(pygame.sprite.Sprite):
    """
    Generate the sprite for the guardian in Pygame.
    Nothing else, just created if needed later.
    """

    def __init__(self):
        super().__init__()
        self.image = guardian
        self.image = pygame.transform.scale(self.image, (taille_perso, taille_perso))
        self.rect = self.image.get_rect()
        self.rect.x = 840
        self.rect.y = 0
