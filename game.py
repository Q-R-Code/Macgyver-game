import pygame
from constantes import taille_fenetre
from objects import Objects

"""

Def launch : 
Initialise le jeu.
-Lance Pygame
-Genere la Labyrinthe
-Genere les objets

Lance la boucle du jeu. 

"""


def launch(macgyver, guardian, maze):
    # Initialisation de Pygame & création de la fenetre avec son fond d'ecran.
    pygame.init()
    pygame.display.set_caption("MacGyver GO GO GO")
    screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))
    background = pygame.image.load("images/background.png")

    # Géneration de la structure du labyrinthe et enregistrement des cases.
    maze.generate()

    # Generation des trois objets.
    item1 = pygame.image.load("images/objet1.png")
    item2 = pygame.image.load("images/objet2.png")
    item3 = pygame.image.load("images/objet3.png")
    objet1 = Objects(maze, item1, name="*1")
    objet2 = Objects(maze, item2, name="*2")
    objet3 = Objects(maze, item3, name="*3")

    running = True
    while running:
        # On applique les images à notre jeu
        screen.blit(background, (0, 0))
        screen.blit(macgyver.image, (macgyver.x, macgyver.y))
        screen.blit(guardian.image, guardian.rect)
        screen.blit(objet1.image, (objet1.x, objet1.y))
        screen.blit(objet2.image, (objet2.x, objet2.y))
        screen.blit(objet3.image, (objet3.x, objet3.y))
        # Affichage des murs par Pygame
        maze.print_maze(screen)
        macgyver.check_obejct(objet1, objet2, objet3)

        guardian.check_victory()

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
