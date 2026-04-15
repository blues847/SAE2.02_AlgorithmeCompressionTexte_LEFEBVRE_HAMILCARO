class Data:
    """
    Classe utilitaire pour calculer les tailles
    avant et après compression Huffman.
    """

    @staticmethod
    def taille_ascii_bits(texte):
        """
        Taille d'un texte ASCII en bits.
        Règle : 1 caractère ASCII = 8 bits.
        """
        return len(texte) * 8

    @staticmethod
    def taille_huffman_bits(chaine_binaire):
        """
        Taille d'une chaîne compressée Huffman en bits.
        Chaque caractère '0' ou '1' représente 1 bit.
        """
        return len(chaine_binaire)

    @staticmethod
    def taux_compression(taille_initiale, taille_compressee):
        """
        Calcule le taux de compression.
        Exemple : 0.5 = 50 % de la taille initiale.
        """
        if taille_initiale == 0:
            return 0
        return taille_compressee / taille_initiale
    
    @staticmethod
    def nettoyer_ascii(texte, utiliser_unidecode=True):
    """
    Nettoie un texte pour le rendre ASCII.
    - Essaie unidecode si demandé et disponible
    - Sinon utilise une méthode de secours
    """

    if utiliser_unidecode:
        try:
            from unidecode import unidecode
            return unidecode(texte)
        except ModuleNotFoundError:
            print("[INFO] unidecode non disponible, utilisation du programme de secours.")

    # --- Méthode de secours (toujours exécutée si unidecode échoue ou est désactivé)
    remplacements = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a',
        'ù': 'u', 'û': 'u',
        'î': 'i', 'ï': 'i',
        'ô': 'o',
        'ç': 'c',
        'É': 'E', 'È': 'E', 'À': 'A', 'Ç': 'C'
    }

    for car, rep in remplacements.items():
        texte = texte.replace(car, rep)

    return texte


# =====================================================
# Tests locaux (optionnels)
# =====================================================
if __name__ == "__main__":
    texte = "éàç Être sûr à Noël"

    print("Texte original :", texte)
    print("Texte ASCII   :", nettoyer_ascii(texte))

    ascii_bits = Data.taille_ascii_bits(texte)
    print("Taille ASCII (bits) :", ascii_bits)

    huff = "010011010101"
    huff_bits = Data.taille_huffman_bits(huff)
    print("Taille Huffman (bits) :", huff_bits)

    print("Taux de compression :", Data.taux_compression(ascii_bits, huff_bits))
