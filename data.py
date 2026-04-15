import os
from NoeudHuffman import NoeudHuffman

class Data:
    """
    Classe utilitaire contenant toutes les méthodes pour le traitement
    et l'affichage des données de compression.
    """

    # --- Méthodes de traitement pur ---

    @staticmethod
    def nettoyer_texte(texte):
        """Nettoie et normalise un texte pour le rendre purement ASCII."""
        try:
            from unidecode import unidecode
            texte_nettoye = unidecode(texte)
        except ModuleNotFoundError:
            print("\n[AVERTISSEMENT] 'unidecode' non installe, le nettoyage sera basique.")
            remplacements = {
                'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a', 'ä': 'a',
                'ù': 'u', 'û': 'u', 'ü': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o',
                'ç': 'c', 'œ': 'oe', 'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E', 'À': 'A',
                'Â': 'A', 'Ä': 'A', 'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Î': 'I', 'Ï': 'I',
                'Ô': 'O', 'Ö': 'O', 'Ç': 'C', 'Œ': 'OE', '€': 'euros', '£': 'livres',
                '$': 'dollars', '&': 'et', '@': 'a'
            }
            texte_nettoye = texte
            for original, remplacement in remplacements.items():
                texte_nettoye = texte_nettoye.replace(original, remplacement)
        return texte_nettoye.encode('ascii', 'ignore').decode('ascii')

    @staticmethod
    def compresser_texte(texte):
        """Compresse un texte via l'algorithme de Huffman."""
        if not texte:
            return "", None, {}
        dico = NoeudHuffman.compte_Occurrences(texte)
        racine = NoeudHuffman.concatenation(dico)
        codes = NoeudHuffman.generer_codes(racine)
        texte_compresse = NoeudHuffman.compresser(texte, codes)
        return texte_compresse, racine, codes

    @staticmethod
    def decompresser_texte(texte_compresse, racine):
        """Decompresse une chaîne binaire avec l'arbre de Huffman."""
        if not texte_compresse or racine is None:
            return ""
        return NoeudHuffman.decompresser(texte_compresse, racine)

    # --- Méthodes d'affichage ---

    @staticmethod
    def afficher_stat(texte_propre, texte_compresse):
        """Affiche les statistiques de compression."""
        taille_init = len(texte_propre.encode('utf-8')) * 8
        taille_compressee = len(texte_compresse)
        print(f"\n--- Statistiques ---")
        print(f"Taille initiale : {taille_init} bits")
        print(f"Taille compressee : {taille_compressee} bits")
        if taille_init > 0:
            taux = (1 - taille_compressee / taille_init) * 100
            print(f"Taux de compression : {taux:.2f}%")
        else:
            print("Taux de compression : N/A (fichier vide)")
        print("-" * 20)

    @staticmethod
    def afficher_arbre_console(racine):
        """Affiche l'arbre de Huffman de manière lisible."""
        if racine is None:
            print("\nArbre de Huffman : (vide)")
            return
        print("\n--- Arbre de Huffman ---")
        lignes = racine.get_representation_arbre()
        for ligne in lignes:
            print(ligne)
        print("-" * 24)

    @staticmethod
    def afficher_table_codes(codes):
        """Affiche la table des codes de Huffman."""
        print("\n--- Table des Codes ---")
        for caractere, code in sorted(codes.items()):
            print(f"  {repr(caractere):<10} -> {code}")
        print("-" * 23)
        
    @staticmethod
    def verifier_decompression(texte_propre, texte_decompresse):
        """Vérifie si le texte décompressé correspond au texte propre."""
        print("\n--- Vérification ---")
        if texte_propre == texte_decompresse:
            print("TEST OK : Le texte décompressé est identique au texte propre.")
        else:
            print("ERREUR : Le texte décompressé est différent du texte propre.")
        print("-" * 20)
