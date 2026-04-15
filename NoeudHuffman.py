from NoeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """Implemente un noeud pour un arbre de Huffman."""

    def __init__(self, chaine=None, poids=None, gauche=None, droit=None):
        """Initialise un noeud de Huffman avec une chaine et un poids."""
        super().__init__((chaine, poids), gauche, droit)

    def getChaine(self):
        """Retourne la chaine de caracteres du noeud."""
        return self.valeur[0]

    def getPoids(self):
        """Retourne le poids du noeud."""
        return self.valeur[1]

    @staticmethod
    def compte_Occurrences(chaine):
        """Compte les occurrences de chaque caractere dans une chaine."""
        frequence = {}
        for caractere in chaine:
            frequence[caractere] = frequence.get(caractere, 0) + 1
        return dict(sorted(frequence.items(), key=lambda item: item[1]))

    @staticmethod
    def concatenation(dico_occur):
        """Construit l'arbre de Huffman a partir d'un dictionnaire de frequences."""
        noeuds = [NoeudHuffman(car, poids) for car, poids in dico_occur.items()]
        while len(noeuds) > 1:
            noeuds.sort(key=lambda n: n.getPoids())
            gauche = noeuds.pop(0)
            droite = noeuds.pop(0)
            chaine_parent = gauche.getChaine() + droite.getChaine()
            poids_parent = gauche.getPoids() + droite.getPoids()
            parent = NoeudHuffman(chaine_parent, poids_parent, gauche, droite)
            noeuds.append(parent)
        return noeuds[0]

    @staticmethod
    def generer_codes(racine):
        """Genere les codes binaires pour chaque caractere a partir de l'arbre."""
        codes = {}
        def parcours(noeud, code_actuel):
            if noeud.estFeuille():
                codes[noeud.getChaine()] = code_actuel
                return
            if noeud.gauche:
                parcours(noeud.gauche, code_actuel + "0")
            if noeud.droit:
                parcours(noeud.droit, code_actuel + "1")
        if racine:
            parcours(racine, "")
        return codes

    @staticmethod
    def compresser(chaine, codes):
        """Compresse une chaine en utilisant les codes de Huffman."""
        return "".join(codes.get(caractere, "") for caractere in chaine)

    @staticmethod
    def decompresser(binaire, racine):
        """Decompresse une chaine binaire en utilisant l'arbre de Huffman."""
        resultat = ""
        noeud_actuel = racine
        for bit in binaire:
            if noeud_actuel is None: break
            noeud_actuel = noeud_actuel.gauche if bit == "0" else noeud_actuel.droit
            if noeud_actuel and noeud_actuel.estFeuille():
                resultat += noeud_actuel.getChaine()
                noeud_actuel = racine
        return resultat
