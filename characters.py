import pygame
from constantes import *

"""
Class MacGyver :

Genere notre joueur.
4 méthodes pour les differentes directions possible.
Pour chaque méthode, il vérifie la case de destination pour savoir si c'est un mur.

Une méthode afin de vérifier si sur la case il y a un objet. Si un objet est présent, ajoute "*" au compteur,
retire l'objet. 

Class Guardian:

Genere notre gardien et une méthode afin de vérifier si le compteur de Macgyver est bien de 3 objets pour la
victoire! 

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
            self.rect = self.image.get_rect()

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

    def check_obejct(self, object1, object2, object3):
        if self.maze.structure[self.case_y][self.case_x] == "*1":
            self.maze.structure[self.case_y][self.case_x] = "O"
            object1.image = pygame.transform.scale(self.image, (0, 0))
            self.compteur.append("*")
        elif self.maze.structure[self.case_y][self.case_x] == "*2":
            self.maze.structure[self.case_y][self.case_x] = "O"
            object2.image = pygame.transform.scale(self.image, (0, 0))
            self.compteur.append("*")
        elif self.maze.structure[self.case_y][self.case_x] == "*3":
            self.maze.structure[self.case_y][self.case_x] = "O"
            object3.image = pygame.transform.scale(self.image, (0, 0))
            self.compteur.append("*")


class Guardian(pygame.sprite.Sprite):

    def __init__(self, maze, macgyver):
        super().__init__()
        self.maze = maze
        self.macgyver = macgyver
        self.image = pygame.image.load("images/gardien.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 840
        self.rect.y = 0

    def check_victory(self):
        if self.maze.structure[self.macgyver.case_y][self.macgyver.case_x] == "B":
            if self.macgyver.compteur.count("*") == 3:
                print("YOU WIN")
            else:
                print("YOU DIE")
