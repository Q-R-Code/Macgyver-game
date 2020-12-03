#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module is for the differents loops of the game and the initialize of Pygame.
"""
import pygame

from game.characters import Macgyver, Guardian
from game.constantes import taille_fenetre
from game.maze_map import Maze
from game.objects import Objects


class Game:
    """
    This class allows to create the 3 screens. The home, the maze and the end.
    """

    def __init__(self, macgyver: Macgyver, guardian: Guardian, maze: Maze):
        self.macgyver = macgyver
        self.guardian = guardian
        self.maze = maze
        pygame.init()
        pygame.display.set_caption("MacGyver GO GO GO")
        self.screen = pygame.display.set_mode((taille_fenetre, taille_fenetre))

    def launch_home(self):
        """
        First screen of the game, with a simple loop for pygame. press space will launch the next part.

        """
        home = pygame.image.load("resources/images/accueil.png")
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
        """
        The main loop of this game, import the maze's structure, generate the walls from it and generate the objects.


        """
        background = pygame.image.load("resources/images/background.png")

        self.maze.generate()

        item1 = pygame.image.load("resources/images/objet1.png")
        item2 = pygame.image.load("resources/images/objet2.png")
        item3 = pygame.image.load("resources/images/objet3.png")
        objet1 = Objects(self.maze, item1, name="*1")
        objet2 = Objects(self.maze, item2, name="*2")
        objet3 = Objects(self.maze, item3, name="*3")

        running_maze = True
        while running_maze:
            # Adding the sprites to our surface "screen".
            self.screen.blit(background, (0, 0))
            self.screen.blit(self.macgyver.image, (self.macgyver.x, self.macgyver.y))
            self.screen.blit(self.guardian.image, self.guardian.rect)
            self.screen.blit(objet1.image, (objet1.x, objet1.y))
            self.screen.blit(objet2.image, (objet2.x, objet2.y))
            self.screen.blit(objet3.image, (objet3.x, objet3.y))

            self.maze.print_maze(self.screen)
            self.macgyver.check_object(objet1, objet2, objet3)

            # check if Macgyver is on the exit (B).
            if self.maze.structure[self.macgyver.case_y][self.macgyver.case_x] == "B":
                running_maze = False
                self.end_screen()
            else:
                pass
            # Events for closing the window or events on the keyboard.
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
            # Refresh the screen
            pygame.display.flip()

    def end_screen(self):
        """
        The last loop of the game, generates a screen based on the victory or defeat.
        Allows to exit with ESCAPE or rerun the game with F1.

        """
        victory = pygame.image.load("resources/images/WIN.png")
        loose = pygame.image.load("resources/images/loose.png")

        running_end = True
        while running_end:
            if self.macgyver.counter.count("*") == 3:
                self.screen.blit(victory, (0, 0))
            elif self.macgyver.counter.count("*") != 3:
                self.screen.blit(loose, (0, 0))
            pygame.display.flip()
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
                        self.macgyver = Macgyver(self.maze)
                        self.launch_home()
                        running_end = False
                    else:
                        pass
