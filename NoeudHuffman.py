from NoeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Classe qui implémente un arbre d'Huffman, utilisant la classe NoeudBinaire.
    """

    # Constructeur
    def __init__(self, chaine=None, poids=None, gauche=None, droit=None):
        # La valeur stockée est un couple (chaine, poids)
        super().__init__((chaine, poids), gauche, droit)

    # Getters
    def getChaine(self):
        return self.valeur[0]

    def getPoids(self):
        return self.valeur[1]

    # Setters
    def setValeur(self, chaine_, poids_):
        self.valeur = (chaine_, poids_)

    def setChaine(self, chaine_):
        self.valeur = (chaine_, self.valeur[1])

    def setPoids(self, poids_):
        self.valeur = (self.valeur[0], poids_)

    #======= Méthodes =======
    # Comptage des occurrences
    @staticmethod
    def compte_Occurrences(chaine):
        """
        Cette méthode prend en paramètre une chaîne de caractères
        et renvoie un dictionnaire ayant pour clé chaque caractère
        et pour valeur le nombre d'apparitions de ce caractère.
        Le dictionnaire est trié par ordre croissant de fréquence.
        """
        frequence = {}
        for caractere in chaine:
            if caractere not in frequence:
                frequence[caractere] = 1
            else:
                frequence[caractere] += 1

        # Tri par fréquence croissante
        frequence = dict(sorted(frequence.items(), key=lambda item: item[1]))
        return frequence

    # Construction de l'arbre de Huffman
    @staticmethod
    def concatenation(dico_occur):
        """
        Cette méthode reçoit en paramètre un dictionnaire des
        occurrences des caractères dans une chaîne trié par ordre croissant.
        Elle construit l'arbre de Huffman et renvoie la racine.
        """

        # Création des feuilles
        noeuds = []
        for caractere, poids in dico_occur.items():
            noeuds.append(NoeudHuffman(caractere, poids, None, None))

        # Construction progressive de l'arbre
        while len(noeuds) > 1:
            # Trie la liste noeuds en utilisant comme critère le poids de chaque noeud et pas la clé
            noeuds.sort(key=lambda n: n.getPoids())

            # Prendre les deux plus petits
            gauche = noeuds.pop(0)
            droite = noeuds.pop(0)

            # Créer le noeud parent
            nouvelle_chaine = gauche.getChaine() + droite.getChaine()
            nouveau_poids = gauche.getPoids() + droite.getPoids()

            parent = NoeudHuffman(nouvelle_chaine,nouveau_poids,gauche,droite)

            # Réinsérer le noeud parent
            noeuds.append(parent)

        # Le dernier noeud est la racine
        return noeuds[0]

    # Génération des codes de Huffman
    @staticmethod
    def generer_codes(racine):
        """
        Génère le code de Huffman de chaque caractère
        à partir de l'arbre de Huffman.
        """
        codes = {}

        def parcours(noeud, code):
            if noeud.estFeuille():
                codes[noeud.getChaine()] = code
                return

            if noeud.gauche:
                parcours(noeud.gauche, code + "0")
            if noeud.droit:
                parcours(noeud.droit, code + "1")

        parcours(racine, "")
        return codes

    # Compression
    @staticmethod
    def compresser(chaine, codes):
        """
        Compresse une chaîne de caractères à l'aide
        du dictionnaire de codes Huffman.
        """
        resultat = ""
        for caractere in chaine:
            resultat += codes[caractere]
        return resultat

    # Décompression
    @staticmethod
    def decompresser(binaire, racine):
        """
        Décompresse une chaîne binaire à l'aide
        de l'arbre de Huffman.
        """
        resultat = ""
        noeud = racine

        for bit in binaire:
            if bit == "0":
                noeud = noeud.gauche
            else:
                noeud = noeud.droit

            if noeud.estFeuille():
                resultat += noeud.getChaine()
                noeud = racine

        return resultat
    
    def __str__(self, prefix="", is_left=True, is_root=True):
        res = ""
        
        # -------- Racine --------
        if is_root:
            res += repr(self.valeur) + "\n"
            new_prefix = ""
        else:
            bit = "0" if is_left else "1"
            connector = f"├──{bit}── " if is_left else f"└──{bit}── "
            res += prefix + connector + repr(self.valeur) + "\n"
            new_prefix = prefix + ("|     " if is_left else "      ")
            
        # -------- Sous-arbre gauche --------
        if self.gauche is not None:
            res += self.gauche.__str__(new_prefix, True, False)
        elif self.droit is not None:
            res += new_prefix + "├──0── .\n"
            
        # -------- Sous-arbre droit --------
        if self.droit is not None:
            res += self.droit.__str__(new_prefix, False, False)
        elif self.gauche is not None:
            res += new_prefix + "└──1── .\n"
            
        return res


def get_printable_representation(self):
    """
    Construit une représentation de l'arbre sous forme de liste de lignes
    pour un affichage sécurisé.
    """
    lines = []
    
    # Fonction récursive interne pour ne pas exposer les paramètres
    def build_lines(noeud, prefix="", is_left=True, is_root=True):
        if noeud is None:
            return
        
        # Sécurisation de la valeur du noeud pour l'affichage
        try:
            valeur_str = repr(noeud.valeur)
        except Exception:
            valeur_str = "(Erreur d'encodage)"
            
        # Construction de la ligne actuelle
        if is_root:
            lines.append(valeur_str)
            new_prefix = ""
        else:
            bit = "0" if is_left else "1"
            connector = f"├──{bit}── " if is_left else f"└──{bit}── "
            lines.append(prefix + connector + valeur_str)
            new_prefix = prefix + ("|     " if is_left else "      ")
            
        # Appel récursif sur les enfants
        if noeud.gauche or noeud.droit:
            build_lines(noeud.gauche, new_prefix, True, False)
            build_lines(noeud.droit, new_prefix, False, False)
        # Gestion des points pour les enfants uniques (si nécessaire)
        # Pour l'instant, on simplifie en n'affichant rien si l'enfant est None
        
    build_lines(self)
    return lines