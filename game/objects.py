#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module is for the generation of the objects.

"""

import pygame
import random

from game.constantes import taille_sprite, taille_objet
from game.maze_map import Maze


class Objects(pygame.sprite.Sprite):
    """
    When we generate a object, it is checking the structure of the maze, to know if its empty or a wall.
    For each objects, the letter of the box change. ( I choose "*1", "*2", "*3" ...)
    """

    def __init__(self, maze: Maze, image: "Image path", name: str):
        super().__init__()
        self.name = name
        self.maze = maze
        self.image = image
        self.image = pygame.transform.scale(self.image, (taille_objet, taille_objet))
        self.rect = self.image.get_rect()
        empty_position = False
        while not empty_position:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.maze.structure[self.case_y][self.case_x] == "O":
                self.maze.structure[self.case_y][self.case_x] = name
                self.x = self.case_x * taille_sprite
                self.y = self.case_y * taille_sprite
                empty_position = True
            else:
                continue
