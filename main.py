import sys
import os
from NoeudHuffman import NoeudHuffman
from data import Data 
 
def main():
    """
    Cette fonction se charge d'activer le programme de compression et est le lien
    entre le terminal et les fonctions python.
    """
    # Vérification que l'utilisateur fourni un argument
    if len(sys.argv) != 2:
        print("Mauvaise saisie!")
        print("Utilisation : python main.py <dossier_input>")
        
    # Récupération du chemin (argument)
    dossier_input = sys.argv[1]
    if not os.path.isdir(dossier_input):
        print(f"ERREUR : le dossier n'existe pas.")
        return
    
    # Parcours de la liste de tous les fichiers / dossiers
    for nom_fichier in os.listdir(dossier_input):
        if nom_fichier.endswith('.txt'): #Si c'est un fichier texte
            chemin_complet = os.path.join(dossier_input, nom_fichier)
            #Lancement du programme en soi
            traiter_fichier(chemin_complet)


if __name__ == "__main__":
    main()