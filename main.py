import sys
import os
from NoeudHuffman import NoeudHuffman
from data import nettoyer_ascii

def compresser_texte(chemin_fichier):
    """
    Fonction qui applique l'algorithme d'Huffman à un fichier.
    Renvoie les éléments clés. Prend en paramètre le chemin du fichier.
    """
    dico = NoeudHuffman.compte_Occurences(texte)
    racine = NoeudHuffman.concatenation(dico)
    codes = NoeudHuffman.generer_codes(racine)
    texte_compresse = NoeufHuffman.compresser(texte, codes)
    return texte_compresse, racine

def afficher_stat():
    """
    Calcule / affiche les tailles avant et après compression (taux de compression).
    """
    
def verifier_decompression():
    """
    Décompresse le texte et vérifie qu'il correspond à l'original.
    Ne renvoie rien.
    """
    # 5. Décompression (vérification)
    texte_decompresse = NoeudHuffman.decompresser(texte_compresse, racine)
    print()
    
    # 6. Vérification finale
    if texte == texte_decompresse:
        print("TEST OK : texte avant / après compression cohérent")
    else:
        print("ERREUR : incohérence.s après décompression")
    
def traiter_fichier(chemin_fichier):
    """
    Appelle les focntions pour gérer le traitement complet d'un fichier."
    """
    # 2. Nettoyage ASCII (OBLIGATOIRE)
    texte = nettoyer_ascii(texte_original)
    
def main():


if __name__ == "__main__":
    main()