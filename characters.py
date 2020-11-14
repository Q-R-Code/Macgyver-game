import pygame
from maze_map import *


class Macgyver(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/macgyver_right.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 840
        self.velocity = 5


    def move_right(self):
        self.image = pygame.image.load("images/macgyver_right.png")
        self.image = self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect.x += self.velocity

    def move_left(self):
        self.image = pygame.image.load("images/macgyver_left.png")
        self.image = self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect.x -= self.velocity

    def move_up(self):
        self.image = pygame.image.load("images/macgyver_up.png")
        self.image = self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect.y -= self.velocity

    def move_down(self):
        self.image = pygame.image.load("images/macgyver_down.png")
        self.image = self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect.y += self.velocity


class Guardian(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/gardien.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 840
        self.rect.y = 0
