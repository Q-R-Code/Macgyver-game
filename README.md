# Projet 3 : Aidez MAcGyver à s'échapper!
***********************************************

## But du jeu :

*MacGyver évolue dans un labyrinthe en 2D, il doit récupérer les trois objets
disposés aléatoirement dans le niveau puis se présenter au gardien.*

************************************************

## Présentation du projet :

Le projet est réalisé en python, l'interface graphique se fait grâce au module Pygame.
Concernant le labyrinthe, il sera généré depuis un fichier texte, il n'y a qu'un seul niveau.


Toutes les images de ce jeu ont été réalisées par le Youtubeur / Graphiste,
[Bienvenue chez les fous](https://www.youtube.com/channel/UCIBuhfY5I16cNh36wFXc6zA "Lien vers la chaine du fou!"),
merci à lui ! 

****************************************

## Modules : 

- main.py : Permet l'initialisation du jeu et le lancement.


- game.py : Ce module gère les differents écrans du jeu grâce aux boucles et Pygame. 


- maze_map.py : Récupération du fichier texte contenant le labyrinthe, création d'une liste de listes dans python
                pour enregistrer la structure. Initialise les sprites des murs par Pygame. 


- characters.py : Création de Macgyver, ses déplacements, son compteur. Création du Gardien.


- objects.py : Ce module permet de générer un objet en lui attribuant une image lors de l'instanciation.
               Les coordonnées sont définies aléatoirement grâce au module Random.

********************************************************

## Installation & lancement : 

Installation des modules nécessaires :

    pip install -r requirements.txt
    
Lancement du jeu : 

    python3 main.py
    
*********************************************************

### Versions :

- 1.0 : Première version fonctionnelle du jeu.

- 2.0 : Prochainement !
Nouveaux niveaux, musique, refont graphique...
  
    

