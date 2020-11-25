from characters import Macgyver, Guardian
from game import launch
from maze_map import Maze
from objects import Objects



def main():
    # On charge MacGyver, le Gardien et le labyrinthe.
    maze = Maze()
    macgyver = Macgyver(maze)
    guardian = Guardian(maze, macgyver)

    # Initialisation du jeu.
    launch(macgyver, guardian, maze)

if __name__ == '__main__':
    main()
