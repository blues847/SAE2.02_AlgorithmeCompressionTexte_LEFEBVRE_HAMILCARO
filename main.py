from NoeudHuffman import NoeudHuffman
from data import nettoyer_ascii


def main():
    # -------------------------------
    # 1. Texte original
    # -------------------------------
    texte_original = "J'ai toujours aucune idée pour le têst"

    print("Texte original :")
    print(texte_original)
    print()

    # -------------------------------
    # 2. Nettoyage ASCII (OBLIGATOIRE)
    # -------------------------------
    texte = nettoyer_ascii(texte_original)

    print("Texte après nettoyage ASCII :")
    print(texte)
    print()

    # -------------------------------
    # 3. Huffman (à partir du texte nettoyé)
    # -------------------------------
    dico = NoeudHuffman.compte_Occurrences(texte)
    print("Occurrences :")
    print(dico)
    print()

    racine = NoeudHuffman.concatenation(dico)
    print("Arbre de Huffman :")
    print(racine)
    print()

    codes = NoeudHuffman.generer_codes(racine)
    print("Codes de Huffman :")
    print(codes)
    print()

    # -------------------------------
    # 4. Compression
    # -------------------------------
    texte_compresse = NoeudHuffman.compresser(texte, codes)
    print("Texte compressé :")
    print(texte_compresse)
    print()

    # -------------------------------
    # 5. Décompression (vérification)
    # -------------------------------
    texte_decompresse = NoeudHuffman.decompresser(texte_compresse, racine)
    print("Texte décompressé :")
    print(texte_decompresse)
    print()

    # -------------------------------
    # 6. Vérification finale
    # -------------------------------
    if texte == texte_decompresse:
        print("TEST OK : compression / décompression cohérentes")
    else:
        print("ERREUR : incohérence après décompression")


if __name__ == "__main__":
    main()