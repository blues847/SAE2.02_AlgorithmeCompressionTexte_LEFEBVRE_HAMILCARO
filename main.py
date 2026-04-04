from NoeudHuffman import NoeudHuffman


def main():
    # 1. Texte de test
    texte = "J'ai pas d'inspiration pour le test"

    print("TEST HUFFMAN")
    print("Texte original :")
    print(texte)
    print()

    # 2. Comptage des occurrences
    dico = NoeudHuffman.compte_Occurrences(texte)
    print("Occurrences :")
    print(dico)
    print()

    # 3. Construction de l'arbre de Huffman
    racine = NoeudHuffman.concatenation(dico)
    print("Arbre de Huffman :")
    print(racine)
    print()

    # 4. Génération des codes
    codes = NoeudHuffman.generer_codes(racine)
    print("Codes de Huffman :")
    print(codes)
    print()

    # 5. Compression
    texte_compresse = NoeudHuffman.compresser(texte, codes)
    print("Texte compressé :")
    print(texte_compresse)
    print()

    # 6. Décompression
    texte_decompresse = NoeudHuffman.decompresser(texte_compresse, racine)
    print("Texte décompressé :")
    print(texte_decompresse)
    print()

    # 7. Vérification
    if texte == texte_decompresse:
        print("Décompression correcte : le texte est identique")
    else:
        print("Une erreur c'est produite")


# Point d'entrée du programme
if __name__ == "__main__":
    main()