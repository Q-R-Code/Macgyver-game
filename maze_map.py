import pygame
from constantes import *


class Maze(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.wall = pygame.image.load("images/wall.png")
        self.rect = self.wall.get_rect()

    def generate(self):
        maze_files = open("maze.txt", "r")
        maze_structure = []
        for ligne in maze_files:
            maze_ligne = []
            for letters in ligne:
                if letters != "\n":
                    maze_ligne.append(letters)
            maze_structure.append(maze_ligne)
        self.structure = maze_structure

    def print_maze(self, screen):
        numb_ligne = 0
        spawn = 0
        end = 0
        for ligne in self.structure:
            numb_colonne = 0
            for letters in ligne:
                x = numb_colonne * taille_sprite
                y = numb_ligne * taille_sprite
                if letters == "O":
                    pass
                elif letters == "W":
                    screen.blit(self.wall, (x, y))
                elif letters == "A":
                    spawn += 1
                elif letters == "B":
                    end += 1
                else:
                    pass
                numb_colonne += 1
            numb_ligne += 1

    def check_collision(self, macgyver):
        return pygame.sprite.spritecollide(macgyver,self.wall, False, pygame.sprite.collide_mask)
