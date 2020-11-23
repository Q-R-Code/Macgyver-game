import pygame
import random
from constantes import taille_sprite

"""
Classe permettant de creer un Objet avec un emplacement aleatoire dans notre structure définit dans Maze_map.
Utilisation de Random pour lui donner un x et un y compris entre 0 et 14 ( notre structure comporte 15 listes 
de 15 caractéres). Une boucle pour vérifier si cet emplacement est vide.

"""


class Objects(pygame.sprite.Sprite):

    def __init__(self, maze, image):
        super().__init__()
        self.maze = maze
        self.image = image
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        empty_position = False
        while empty_position == False:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.maze.structure[self.case_y][self.case_x] == "O":
                self.maze.structure[self.case_y][self.case_x] = "*"
                self.x = self.case_x * taille_sprite
                self.y = self.case_y * taille_sprite
                empty_position = True
            else:
                continue
        print(f"la structure est {self.maze.structure}.")
