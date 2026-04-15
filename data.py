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

    @staticmethod
    def compresser_texte(texte):
        """
        Fonction qui applique l'algorithme d'Huffman à un fichier.
        Renvoie les éléments clés. Prend en paramètre le texte
        sous forme d'un chaîne de caractères.
        """
        # Création du dictionnaire d'occurences des caractères
        dico = NoeudHuffman.compte_Occurrences(texte)
        
        # Création de l'arbre de Huffman
        racine = NoeudHuffman.concatenation(dico)
        
        # Création du nouvel encodage
        codes = NoeudHuffman.generer_codes(racine)
        
        # Compression du texte
        texte_compresse = NoeudHuffman.compresser(texte, codes)
        
        return texte_compresse, racine, codes

    @staticmethod
    def afficher_infos(racine, codes):
        """
        Affiche l'arbre et les encodages selon la logique d'Huffman.
        Reçoit en paramètre la racine d'un arbre d'Huffman (objet NoeudHuffman)
        et les codes servant à l'encodage des caractères.
        """
        print("\n=== Informations ===")
        print("Arbre de Huffman généré :") #Affichage de l'arbre
        print(racine)
        print("\nTable des codes de Huffman :") #Affichage des codes
        for caractere, code in sorted(codes.items()):
            print(f"   {repr(caractere):<10} -> {code}")
        print("=" * 20 + "\n")
        
    @staticmethod        
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
            taux = (1 - taille_compressee / taille_init) * 100
            print(f"Taux de compression : {taux}")
        else:
            print("Fichier vide, pas de compression.\n")
        
    @staticmethod        
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
      
    @staticmethod      
    def traiter_fichier(chemin_fichier):
        """
        Appelle les focntions pour gérer le traitement complet d'un fichier.
        Prends en paramètres le chemin du fichier."
        """
        print(f" ----- Fichier : {os.path.basename(chemin_fichier)}")
        
        # Lecture du fichier, gestion d'une potentielle erreur
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as file:
                texte_original = file.read()
        except Exception as e:
            print(f"Erreur de lecture : {e}")
            return
        
        # Nettoyage ASCII
        texte_propre = nettoyer_ascii(texte_original)
        if not texte_propre:
            print("Le fichier est vide ou non compatible.")
            return
        
        # Compression
        texte_compresse, racine, codes = compresser_texte(texte_propre)
        
        # Affichage des résultats
        afficher_stat(texte_propre, texte_compresse)
        
        # Affichage des informations complémentaires
        afficher_infos(racine, codes)
        
        # Vérification
        verifier_decompression(texte_propre, texte_compresse, racine)
        
        #Barre de fin (séparation dans la console)
        print("=" * 30 + "\n")
