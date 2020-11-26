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

    # Initialisation du jeu.
    game = Game(macgyver, guardian, maze)
    game.launch_home()


if __name__ == '__main__':
    main()
