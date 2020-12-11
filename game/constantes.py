"""
Les constantes de notre jeu pour un labyrinthe de 15 cases sur 15.
J'ai fais le choix de partir sur une résolution de 900x900 donc chaques sprites =  60x60
Les personnages et objets font 55x55.

"""
import pygame

nombre_sprite = 15
taille_sprite = 60
taille_perso = taille_sprite - 5
taille_objet = taille_sprite - 5
taille_fenetre = nombre_sprite * taille_sprite

macgyver_right = pygame.image.load("resources/images/macgyver_right.png")
macgyver_left = pygame.image.load("resources/images/macgyver_left.png")
macgyver_up = pygame.image.load("resources/images/macgyver_up.png")
macgyver_down = pygame.image.load("resources/images/macgyver_down.png")

guardian = pygame.image.load("resources/images/gardien.png")

backpack = pygame.image.load("resources/images/backpack.png")
number_0 = pygame.image.load("resources/images/number_0.png")
number_1 = pygame.image.load("resources/images/number_1.png")
number_2 = pygame.image.load("resources/images/number_2.png")
number_3 = pygame.image.load("resources/images/number_3.png")

wall = pygame.image.load("resources/images/wall.png")


item1 = pygame.image.load("resources/images/objet1.png")
item2 = pygame.image.load("resources/images/objet2.png")
item3 = pygame.image.load("resources/images/objet3.png")

background_screen = pygame.image.load("resources/images/background.png")
home_screen = pygame.image.load("resources/images/accueil.png")
victory_screen = pygame.image.load("resources/images/WIN.png")
loose_screen = pygame.image.load("resources/images/loose.png")
