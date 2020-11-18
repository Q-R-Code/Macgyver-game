from characters import Macgyver, Guardian
from game import launch
from maze_map import Maze


def main():
    # On charge MacGyver, le Gardien et le labyrinthe.
    macgyver = Macgyver()
    guardian = Guardian()
    maze = Maze()

    # Initialisation du jeu.
    launch(macgyver, guardian, maze)

if __name__ == '__main__':
    main()
