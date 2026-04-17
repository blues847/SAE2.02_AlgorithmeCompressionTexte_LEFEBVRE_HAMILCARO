class NoeudBinaire:
    """Implemente un noeud pour un arbre binaire."""
    
    # Constructeur
    def __init__(self, valeur=None, gauche=None, droit=None):
        """Initialise un noeud."""
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    # Getters
    def getValeur(self):
        """Retourne la valeur du noeud."""
        return self.valeur
    
    def getGauche(self):
        """Retourne le sous-arbre gauche."""
        return self.gauche
    
    def getDroit(self):
        """Retourne le sous-arbre droit."""
        return self.droit
    
    # Méthodes
    def estFeuille(self):
        """Verifie si le noeud est une feuille."""
        return self.gauche is None and self.droit is None

    def __str__(self):
        """Construit une representation textuelle de l'arbre pour l'affichage."""
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
        return '\n'.join(lignes)
