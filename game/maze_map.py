#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module is for, the generation of the maze from a text files, and the sprites for Pygame.

"""

import pygame

from game.constantes import taille_sprite


class Maze:
    """
    with "generate" we create a list of list for saving the structure. ( lines and columns )

    """

    def __init__(self):
        self.structure = None

    def generate(self) -> list:
        """
        open a text files including 15 lines and 15 columns.
        A = the start
        B = the end
        O = empty box
        W = wall
        we create a list of list for saving the structure. ( lines and columns )

        """
        maze_file = open("resources/maze.txt", "r")
        maze_structure = []
        for lines in maze_file:
            maze_line = []
            for letters in lines:
                if letters != "\n":
                    maze_line.append(letters)
            maze_structure.append(maze_line)
        self.structure = maze_structure

    def print_maze(self, screen: "Pygame surface"):
        """
        check the structure, if its a W : add to it a wall sprite.

        """
        num_line = 0
        for lines in self.structure:
            num_column = 0
            for letters in lines:
                x = num_column * taille_sprite
                y = num_line * taille_sprite
                if letters == "W":
                    maze_sprite = MazeSprite(x, y)
                    screen.blit(maze_sprite.image, (x, y))
                else:
                    pass
                num_column += 1
            num_line += 1


class MazeSprite(pygame.sprite.Sprite):
    """
    Generate the sprite of a wall for pygame.
    """

    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load("resources/images/wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
