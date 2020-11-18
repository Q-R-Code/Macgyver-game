import pygame
from constantes import *
from maze_map import Maze


def launch(macgyver, guardian, maze):
    #Initialisation de Pygame & création de la fenetre avec son fond d'ecran.
    pygame.init()
    pygame.display.set_caption("MacGyver GO GO GO")
    screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))
    background = pygame.image.load("images/background.png")
    #Dictionnaire pour le deplacement de macgyver
    pressed = {}
    #Géneration de la structure du labyrinthe et enregistrement des cases.
    maze.generate()
    maze.structure_rect()


    running = True
    while running:
        # On applique les images à notre jeu
        screen.blit(background, (0, 0))
        screen.blit(macgyver.image, macgyver.rect)
        screen.blit(guardian.image, guardian.rect)
        #Affichage des murs par Pygame
        maze.print_maze(screen)

        # Déplacement de Macgyver
        if pressed.get(pygame.K_RIGHT) and macgyver.rect.x + 60 < 900:
            macgyver.move_right()
        elif pressed.get(pygame.K_LEFT) and macgyver.rect.x > 0:
            macgyver.move_left()
        elif pressed.get(pygame.K_UP) and macgyver.rect.y > 0:
            macgyver.move_up()
        elif pressed.get(pygame.K_DOWN) and macgyver.rect.y + 60 < 900:
            macgyver.move_down()
        #Rafraichissement de l'écran.
        pygame.display.flip()
        #Gestion des évenements dans Pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu.")
            elif event.type == pygame.KEYDOWN:
                pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                pressed[event.key] = False



