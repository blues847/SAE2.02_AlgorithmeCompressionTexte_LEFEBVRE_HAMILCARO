import os
from NoeudHuffman import NoeudHuffman

class Data:
    @staticmethod
    def nettoyer_texte(texte):
        """
        Nettoie et normalise un texte pour le rendre purement ASCII,
        en essayant de préserver le sens au maximum.
        """
        try:
            from unidecode import unidecode
            texte_nettoye = unidecode(texte)
        except ModuleNotFoundError:
            print("\n[AVERTISSEMENT] La bibliothèque 'unidecode' n'est pas installée.")
            print("Le nettoyage du texte sera moins précis (accents et symboles).")
            print("Pour une meilleure qualité, installez-la avec : pip install unidecode")
            remplacements = {
                '€': ' euros ', '£': ' livres ', '$': ' dollars ',
                '&': ' et ', '@': ' a ',
                'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
                'à': 'a', 'â': 'a', 'ä': 'a',
                'ù': 'u', 'û': 'u', 'ü': 'u',
                'î': 'i', 'ï': 'i',
                'ô': 'o', 'ö': 'o',
                'ç': 'c', 'œ': 'oe',
                'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
                'À': 'A', 'Â': 'A', 'Ä': 'A',
                'Ù': 'U', 'Û': 'U', 'Ü': 'U',
                'Î': 'I', 'Ï': 'I',
                'Ô': 'O', 'Ö': 'O',
                'Ç': 'C', 'Œ': 'OE'
            }
            texte_nettoye = texte
            for original, remplacement in remplacements.items():
                texte_nettoye = texte_nettoye.replace(original, remplacement)
        texte_final = texte_nettoye.encode('ascii', 'ignore').decode('ascii')
        return texte_final

    @staticmethod
    def compresser_texte(texte):
        dico = NoeudHuffman.compte_Occurrences(texte)
        racine = NoeudHuffman.concatenation(dico)
        codes = NoeudHuffman.generer_codes(racine)
        texte_compresse = NoeudHuffman.compresser(texte, codes)
        return texte_compresse, racine, codes

    @staticmethod
    def afficher_arbre_console(racine):
        print("\nArbre de Huffman :")
        lignes_arbre = racine.get_representation_arbre()
        for ligne in lignes_arbre:
            try:
                print(ligne)
            except UnicodeEncodeError:
                print(ligne.encode('ascii', 'ignore').decode('ascii'))
        print("-" * 30)

    @staticmethod
    def sauvegarder_infos_arbre(racine, codes, nom_fichier_base):
        nom_fichier_arbre = f"arbre_{nom_fichier_base}.txt"
        try:
            with open(nom_fichier_arbre, "w", encoding="utf-8") as f:
                lignes_arbre = racine.get_representation_arbre()
                for ligne in lignes_arbre:
                    f.write(ligne + "\n")
                f.write("\n\n" + "="*30 + "\n")
                f.write("Table des codes de Huffman :\n")
                f.write("="*30 + "\n")
                for caractere, code in sorted(codes.items()):
                    f.write(f"   {repr(caractere):<10} -> {code}\n")
            print(f"\nArbre et codes sauvegardés dans : '{nom_fichier_arbre}'")
        except Exception as e:
            print(f"\nErreur lors de la sauvegarde du fichier : {e}")

        print("\nTable des codes de Huffman (console):")
        for caractere, code in sorted(codes.items()):
            try:
                print(f"   {repr(caractere):<10} -> {code}")
            except UnicodeEncodeError:
                print(f"   {'[char non affichable]':<10} -> {code}")
        print("=" * 30 + "\n")

    @staticmethod
    def afficher_stat(texte_propre, texte_compresse):
        taille_init = len(texte_propre) * 8
        taille_compressee = len(texte_compresse)
        print(f"Taille initiale : {taille_init} bits.")
        print(f"Taille compressée : {taille_compressee} bits.")
        if taille_init > 0:
            taux = (1 - taille_compressee / taille_init) * 100
            print(f"Taux de compression : {taux:.2f}%")
        else:
            print("Fichier vide, pas de compression.\n")

    @staticmethod
    def verifier_decompression(texte_propre, texte_compresse, racine):
        texte_decompresse = NoeudHuffman.decompresser(texte_compresse, racine)
        print()
        if texte_propre == texte_decompresse:
            print("TEST OK : texte avant / après compression cohérent")
        else:
            print("ERREUR : incohérence.s après décompression")

    @staticmethod
    def traiter_fichier(chemin_fichier):
        print(f" ----- Fichier : {os.path.basename(chemin_fichier)}")
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as file:
                texte_original = file.read()
        except Exception as e:
            print(f"Erreur de lecture : {e}")
            return
        
        texte_propre = Data.nettoyer_texte(texte_original)
        if not texte_propre:
            print("Le fichier est vide ou non compatible.")
            return
        
        texte_compresse, racine, codes = Data.compresser_texte(texte_propre)
        
        Data.afficher_stat(texte_propre, texte_compresse)
        Data.afficher_arbre_console(racine)
        Data.sauvegarder_infos_arbre(racine, codes, os.path.basename(chemin_fichier).replace('.txt', ''))
        Data.verifier_decompression(texte_propre, texte_compresse, racine)
        
        print("=" * 30 + "\n")
