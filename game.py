import pygame
from constantes import *
from maze_map import Maze


def check_collide(sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


def launch(macgyver, guardian, maze):
    # Initialisation de Pygame & création de la fenetre avec son fond d'ecran.
    pygame.init()
    pygame.display.set_caption("MacGyver GO GO GO")
    screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))
    background = pygame.image.load("images/background.png")

    # Géneration de la structure du labyrinthe et enregistrement des cases.
    maze.generate()
    maze.structure_rect()
    maze.get_structure()


    running = True
    while running:
        # On applique les images à notre jeu
        screen.blit(background, (0, 0))
        screen.blit(macgyver.image, (macgyver.x, macgyver.y))
        screen.blit(guardian.image, guardian.rect)
        # Affichage des murs par Pygame
        maze.print_maze(screen)

        # Rafraichissement de l'écran.
        pygame.display.flip()
        # Gestion des évenements dans Pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and macgyver.x + 55 < 845:
                    macgyver.move_right()
                elif event.key == pygame.K_LEFT and macgyver.x - 55 > 0:
                    macgyver.move_left()
                elif event.key == pygame.K_UP and macgyver.y - 55 > 0:
                    macgyver.move_up()
                elif event.key == pygame.K_DOWN and macgyver.y + 55 < 845:
                    macgyver.move_down()


