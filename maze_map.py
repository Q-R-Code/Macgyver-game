import pygame
from pygame.locals import *
from constantes import *


class Maze(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def generate(self):
        maze_files = open("maze.txt", "r")
        maze_structure = []
        for ligne in maze_files:
            maze_ligne = []
            for letters in ligne:
                if letters != "\n":
                    maze_ligne.append(letters)
            maze_structure.append(maze_ligne)
        #print(maze_structure)
        self.structure = maze_structure

    def print(self, screen):
        numb_ligne = 0
        numb_O = 0
        numb_W = 0
        spawn = 0
        end = 0
        wall = pygame.image.load("images/wall.png")
        for ligne in self.structure:
            numb_colonne = 0
            for letters in ligne:
                x = numb_colonne * taille_sprite
                y = numb_ligne * taille_sprite
                if letters == "O":
                    numb_O += 1
                elif letters == "W":
                    screen.blit(wall, (x, y))
                    numb_W += 1
                elif letters == "A":
                    spawn += 1
                elif letters == "B":
                    end += 1
                else:
                    pass
                numb_colonne += 1
            numb_ligne += 1
        # print(numb_ligne, numb_colonne)
        # print(numb_W, numb_O)
