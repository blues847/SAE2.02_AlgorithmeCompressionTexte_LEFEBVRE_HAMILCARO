class NoeudHuffman(NoeudBinaire):
    """Implémente un noeud pour un arbre de Huffman."""

    def __init__(self, chaine=None, poids=None, gauche=None, droit=None):
        """Initialise un noeud de Huffman avec une chaîne et un poids."""
        super().__init__((chaine, poids), gauche, droit)

    # Getters
    def getChaine(self):
        """Retourne la chaîne de caractères du noeud."""
        return self.valeur[0]

    def getPoids(self):
        """Retourne le poids du noeud."""
        return self.valeur[1]

    # Setters
    def setValeur(self, chaine_, poids_):
        """Définit la valeur (chaîne, poids) du noeud."""
        self.valeur = (chaine_, poids_)

    def setChaine(self, chaine_):
        """Définit la chaîne de caractères du noeud."""
        self.valeur = (chaine_, self.valeur[1])

    def setPoids(self, poids_):
        """Définit le poids du noeud."""
        self.valeur = (self.valeur[0], poids_)

    @staticmethod
    def compte_Occurrences(chaine):
        """Compte les occurrences de chaque caractère dans une chaîne."""
        frequence = {}
        for caractere in chaine:
            frequence[caractere] = frequence.get(caractere, 0) + 1
        
        # Tri par fréquence pour la construction de l'arbre
        return dict(sorted(frequence.items(), key=lambda item: item[1]))

    @staticmethod
    def concatenation(dico_occur):
        """Construit l'arbre de Huffman à partir d'un dictionnaire de fréquences."""
        # Création des feuilles initiales
        noeuds = [NoeudHuffman(car, poids) for car, poids in dico_occur.items()]

        # Fusion des noeuds jusqu'à obtenir la racine
        while len(noeuds) > 1:
            noeuds.sort(key=lambda n: n.getPoids())
            
            gauche = noeuds.pop(0)
            droite = noeuds.pop(0)

            # Création du noeud parent
            chaine_parent = gauche.getChaine() + droite.getChaine()
            poids_parent = gauche.getPoids() + droite.getPoids()
            parent = NoeudHuffman(chaine_parent, poids_parent, gauche, droite)
            
            noeuds.append(parent)

        return noeuds[0]

    @staticmethod
    def generer_codes(racine):
        """Génère les codes binaires pour chaque caractère à partir de l'arbre."""
        codes = {}

        def parcours(noeud, code_actuel):
            if noeud.estFeuille():
                codes[noeud.getChaine()] = code_actuel
                return

            if noeud.gauche:
                parcours(noeud.gauche, code_actuel + "0")
            if noeud.droit:
                parcours(noeud.droit, code_actuel + "1")

        parcours(racine, "")
        return codes

    @staticmethod
    def compresser(chaine, codes):
        """Compresse une chaîne en utilisant les codes de Huffman."""
        return "".join(codes[caractere] for caractere in chaine)

    @staticmethod
    def decompresser(binaire, racine):
        """Décompresse une chaîne binaire en utilisant l'arbre de Huffman."""
        resultat = ""
        noeud_actuel = racine
        for bit in binaire:
            noeud_actuel = noeud_actuel.gauche if bit == "0" else noeud_actuel.droit
            if noeud_actuel.estFeuille():
                resultat += noeud_actuel.getChaine()
                noeud_actuel = racine
        return resultat
    
    def get_representation_arbre(self):
        """Construit une représentation textuelle de l'arbre pour l'affichage."""
        lignes = []
        
        def construire_lignes(noeud, prefixe="", est_gauche=True, est_racine=True):
            if noeud is None:
                return

            valeur_str = repr(noeud.valeur)

            if est_racine:
                lignes.append(valeur_str)
                nouveau_prefixe = ""
            else:
                bit = "0" if est_gauche else "1"
                connecteur = f"|--{bit}-- "
                lignes.append(prefixe + connecteur + valeur_str)
                nouveau_prefixe = prefixe + ("|       " if est_gauche else "        ")

            if noeud.gauche or noeud.droit:
                construire_lignes(noeud.gauche, nouveau_prefixe, True, False)
                construire_lignes(noeud.droit, nouveau_prefixe, False, False)

        construire_lignes(self)
        return lignes

