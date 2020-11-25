import pygame
from constantes import taille_fenetre
from objects import Objects

"""
Classe Game :
Cette classe gere les ecrans de jeu, divisé en 3 méthodes. 
Elle initialise Pygame.

Def launch_home :
    L'ecran d'acceuil.
Def launch_maze : 
    Generation du labyrinthe, des trois objets, du fond d'ecran du niveau.
    La boucle du jeu : 
        Elle gere les deplacements, elle vérifie si MacGyver passe sur un objet
        et si il est sur la case de sortie. 
Def launch_end : 
    L'ecran de fin. 
    On vérifie dans un premier temps le compteur de MacGyver : si 3 objets, Victoire
    sinon : Défaite.
    Possibilité de quitter graçe à ECHAP ou relancer avec F1.

"""


class Game:

    def __init__(self, macgyver, guardian, maze):
        self.macgyver = macgyver
        self.guardian = guardian
        self.maze = maze
        pygame.init()
        pygame.display.set_caption("MacGyver GO GO GO")
        self.screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))

    def launch_home(self):
        home = pygame.image.load("images/accueil.png")
        running_home = True
        while running_home:
            self.screen.blit(home, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_home = False
                    pygame.quit()
                    print("Fermeture du jeu.")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running_home = False
                        self.launch_maze()
            pygame.display.flip()

    def launch_maze(self):
        # On ajoute l'image du fond d'ecran.
        background = pygame.image.load("images/background.png")
        # Géneration de la structure du labyrinthe et enregistrement des cases.
        self.maze.generate()
        # Generation des trois objets.
        item1 = pygame.image.load("images/objet1.png")
        item2 = pygame.image.load("images/objet2.png")
        item3 = pygame.image.load("images/objet3.png")
        objet1 = Objects(self.maze, item1, name="*1")
        objet2 = Objects(self.maze, item2, name="*2")
        objet3 = Objects(self.maze, item3, name="*3")

        running_maze = True

        while running_maze:
            # On applique les images à notre jeu
            self.screen.blit(background, (0, 0))
            self.screen.blit(self.macgyver.image, (self.macgyver.x, self.macgyver.y))
            self.screen.blit(self.guardian.image, self.guardian.rect)
            self.screen.blit(objet1.image, (objet1.x, objet1.y))
            self.screen.blit(objet2.image, (objet2.x, objet2.y))
            self.screen.blit(objet3.image, (objet3.x, objet3.y))

            # Affichage des murs par Pygame
            self.maze.print_maze(self.screen)
            self.macgyver.check_obejct(objet1, objet2, objet3)

            # On vérifie si macgyver est sur la case de la sortie, si oui, on lance la fin.
            if self.maze.structure[self.macgyver.case_y][self.macgyver.case_x] == "B":
                running_maze = False
                self.launch_end()
            else:
                pass

            # Gestion des évenements dans Pygame.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_maze = False
                    pygame.quit()
                    print("Fermeture du jeu.")

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.macgyver.x + 55 < 845:
                        self.macgyver.move_right()
                    elif event.key == pygame.K_LEFT and self.macgyver.x - 55 > 0:
                        self.macgyver.move_left()
                    elif event.key == pygame.K_UP and self.macgyver.y - 55 > 0:
                        self.macgyver.move_up()
                    elif event.key == pygame.K_DOWN and self.macgyver.y + 55 < 845:
                        self.macgyver.move_down()
            # Rafraichissement de l'écran.
            pygame.display.flip()

    def launch_end(self):
        victory = pygame.image.load("images/WIN.png")
        loose = pygame.image.load("images/loose.png")

        running_end = True

        while running_end:
            if self.macgyver.compteur.count("*") == 3:
                self.screen.blit(victory, (0, 0))
            elif self.macgyver.compteur.count("*") != 3:
                self.screen.blit(loose, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_end = False
                    pygame.quit()
                    print("Fermeture du jeu.")

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running_end = False
                        pygame.quit()
                        print("Fermeture du jeu.")
                    elif event.key == pygame.K_F1:
                        self.launch_home()
                        running_end = False
                    else:
                        pass
            pygame.display.flip()
