from characters import Macgyver, Guardian
from game import Game
from maze_map import Maze


def main():
    # On charge MacGyver, le Gardien et le labyrinthe.
    maze = Maze()
    macgyver = Macgyver(maze)
    guardian = Guardian(maze, macgyver)

    # Initialisation du jeu.
    game = Game(macgyver, guardian, maze)
    game.launch_home()


if __name__ == '__main__':
    main()
