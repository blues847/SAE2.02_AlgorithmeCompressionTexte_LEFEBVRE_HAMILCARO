def nettoyer_ascii(texte, utiliser_unidecode=True):
    """
    Nettoie un texte pour le rendre ASCII.
    - Si utiliser_unidecode=True et que unidecode est disponible : on l'utilise
    - Sinon : on utilise une méthode de remplacement simple
    """

    if utiliser_unidecode:
        try:
            from unidecode import unidecode
            return unidecode(texte)
        except ModuleNotFoundError:
            print("[INFO] unidecode non disponible, utilisation du mode ASCII simple.")

    # Méthode de secours (sans bibliothèque)
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
if __name__ == "__main__":
    texte = "éàç Être sûr à Noël"
    print("Texte original :", texte)
    print("Texte nettoyé :", nettoyer_ascii(texte))
