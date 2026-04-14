import sys
import os
from NoeudHuffman import NoeudHuffman
from data import nettoyer_ascii

def compresser_texte(texte):
    """
    Fonction qui applique l'algorithme d'Huffman à un fichier.
    Renvoie les éléments clés. Prend en paramètre le texte
    sous forme d'un chaîne de caractères.
    """
    dico = NoeudHuffman.compte_Occurences(texte)
    racine = NoeudHuffman.concatenation(dico)
    codes = NoeudHuffman.generer_codes(racine)
    texte_compresse = NoeufHuffman.compresser(texte, codes)
    return texte_compresse, racine

def afficher_stat(texte_propre, texte_compresse):
    """
    Calcule / affiche les tailles avant et après compression (taux de compression).
    """
    taille_init = len(texte_propre) * 8
    taille_compressee = len(texte_compresse)
    
    #A afficher ailleurs que dans la console? (une page séparée? un fichier de bilan?)
    print(f"Taille initiale : {taille_init} bits.")
    print(f"Taille compressée : {taille_compressee} bits.")
    
    if taille_init > 0:
        #Calcul du taux de compression (formule)
        taux = (1 - taille_compressee / taille_initiale) * 100
        print(f"Taux de compression : {}")
    else:
        print("Fichier vide, pas de compression.\n")
    
def verifier_decompression(texte_propre, texte_compresse, racine):
    """
    Décompresse le texte et vérifie qu'il correspond à l'original.
    Ne renvoie rien.
    """
    # Décompression
    texte_decompresse = NoeudHuffman.decompresser(texte_compresse, racine)
    print()
    
    # Vérification
    if texte_propre == texte_decompresse:
        print("TEST OK : texte avant / après compression cohérent")
    else:
        print("ERREUR : incohérence.s après décompression")
    
def traiter_fichier(chemin_fichier):
    """
    Appelle les focntions pour gérer le traitement complet d'un fichier.
    Prends en paramètres le chemin du fichier."
    """
    # Nettoyage ASCII
    texte = nettoyer_ascii(texte_original)
    
def main():


if __name__ == "__main__":
    main()