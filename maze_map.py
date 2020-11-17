import pygame
from constantes import *

"""
Classe permettant de générer le labyrinthe.
def generate :
    Ouvre le fichier texte contenant le labyrinthe, créer un liste global pour la structure,
    et ensuite, pour chaques lignes, creer une liste de celle ci.
def print_maze :
    parcours notre structure, si c'est un "W", y applique l'image d'un mur en 60x60.

"""


class Maze(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

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
        num_ligne = 0
        for ligne in self.structure:
            num_colonne = 0
            for letters in ligne:
                x = num_colonne * taille_sprite
                y = num_ligne * taille_sprite
                if letters == "O":
                    pass
                elif letters == "W":
                    screen.blit(self.image,(x, y))
                else:
                    pass
                num_colonne += 1
            num_ligne += 1
