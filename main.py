#!/usr/bin/env python
# -*- coding: utf-8 -*-


from characters import Macgyver, Guardian
from game import Game
from maze_map import Maze


def main():
    """
     Initialize the game and launch the first loop.
    """
    maze = Maze()
    macgyver = Macgyver(maze)
    guardian = Guardian()

    game = Game(macgyver, guardian, maze)
    game.launch_home()


if __name__ == '__main__':
    main()
