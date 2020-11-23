import pygame
from constantes import *

"""
Class MacGyver :
Genere notre joueur.
4 méthodes pour les differentes directions possible.
Pour chaque méthode, il vérifie la case de destination pour savoir si c'est un mur.

Class Guardian:

Genere notre gardien. 

"""


class Macgyver(pygame.sprite.Sprite):

    def __init__(self, maze):
        super().__init__()
        self.maze = maze
        self.image = pygame.image.load("images/macgyver_right.png")
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.case_x = 0
        self.case_y = 14
        self.x = 0
        self.y = 845
        self.compteur = []



    def move_right(self):
        if self.maze.structure[self.case_y][self.case_x + 1] != "W":
            self.case_x += 1
            self.image = pygame.image.load("images/macgyver_right.png")
            self.image = self.image = pygame.transform.scale(self.image, (55, 55))
            self.x = self.case_x * taille_sprite

    def move_left(self):
        if self.maze.structure[self.case_y][self.case_x - 1] != "W":
            self.image = pygame.image.load("images/macgyver_left.png")
            self.image = pygame.transform.scale(self.image, (55, 55))
            self.case_x -= 1
            self.x = self.case_x * taille_sprite

    def move_up(self):
        if self.maze.structure[self.case_y - 1][self.case_x] != "W":
            self.image = pygame.image.load("images/macgyver_up.png")
            self.image = pygame.transform.scale(self.image, (55, 55))
            self.case_y -= 1
            self.y = self.case_y * taille_sprite


    def move_down(self):
        if self.maze.structure[self.case_y + 1][self.case_x] != "W":
            self.image = pygame.image.load("images/macgyver_down.png")
            self.image = pygame.transform.scale(self.image, (55, 55))
            self.case_y += 1
            self.y = self.case_y * taille_sprite



class Guardian(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/gardien.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 840
        self.rect.y = 0
