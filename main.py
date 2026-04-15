import sys
import os
from data import Data

def main():
     """Point d'entrée principal pour l'outil de compression."""
    # Gestion des arguments de la ligne de commande
    if len(sys.argv) == 3:
        # Cas 1: Traitement d'un fichier spécifique dans un dossier
        dossier_input = sys.argv[1]
        nom_fichier_specifique = sys.argv[2]
        
        if not os.path.isdir(dossier_input):
            print(f"ERREUR : Le dossier '{dossier_input}' n'existe pas.")
            return

        chemin_complet = os.path.join(dossier_input, nom_fichier_specifique)
        if os.path.exists(chemin_complet) and nom_fichier_specifique.endswith('.txt'):
                Data.traiter_fichier(chemin_complet)
        else:
            print(f"ERREUR : Le fichier '{nom_fichier_specifique}' est introuvable ou n'est pas un .txt dans le dossier '{dossier_input}'.")

    elif len(sys.argv) == 2:
        # Cas 2: Traitement de tous les fichiers .txt d'un dossier
        dossier_input = sys.argv[1]
        if not os.path.isdir(dossier_input):
            print(f"ERREUR : Le dossier '{dossier_input}' n'existe pas.")
            return
        
        # Parcours et traitement de chaque fichier
        for nom_fichier in os.listdir(dossier_input):
            if nom_fichier.endswith('.txt'):
                chemin_complet = os.path.join(dossier_input, nom_fichier)
                Data.traiter_fichier(chemin_complet)
    else:
        # Erreur si le nombre d'arguments est incorrect
        print("Mauvaise saisie!")
        print("Utilisation : python main.py <dossier_input> [<nom_fichier_specifique>]")


if __name__ == "__main__":
    main()
