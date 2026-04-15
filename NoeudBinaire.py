class NoeudBinaire:
    """Implémente un noeud pour un arbre binaire."""
    
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
    
    # Setters
    def setValeur(self, valeur_):
        """Définit la valeur du noeud."""
        self.valeur = valeur_
        
    def setGauche(self, gauche_):
        """Définit le sous-arbre gauche."""
        self.gauche = gauche_
        
    def setDroit(self, droit_):
        """Définit le sous-arbre droit."""
        self.droit = droit_
        
    # Méthodes
    def a_gauche(self):
        """Vérifie l'existence d'un sous-arbre gauche."""
        return self.gauche is not None
        
    def a_droit(self):
        """Vérifie l'existence d'un sous-arbre droit."""
        return self.droit is not None
    
    def estFeuille(self):
        """Vérifie si le noeud est une feuille."""
        return self.gauche is None and self.droit is None and self.valeur is not None
        
    def estVide(self):
        """Vérifie si l'arbre est vide."""
        return self.valeur is None

    def hauteur(self):
        """Calcule la hauteur de l'arbre."""
        if self.estFeuille():
            return 1
        elif self.gauche is None:
            return 1 + self.droit.hauteur()
        elif self.droit is None:
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())
    
    def __str__(self, prefix="", is_left=True, is_root=True):
        """Représentation textuelle de l'arbre pour l'affichage."""
        res = ""

        if is_root:
            res += repr(self.valeur) + "\n"
            new_prefix = ""
        else:
            connector = "├── " if is_left else "└── "
            res += prefix + connector + repr(self.valeur) + "\n"
            new_prefix = prefix + ("|   " if is_left else "    ")

        if self.gauche:
            res += self.gauche.__str__(new_prefix, True, False)
        elif self.droit:
            res += new_prefix + "├── .\n"  # Marqueur pour fils manquant

        if self.droit:
            res += self.droit.__str__(new_prefix, False, False)
        elif self.gauche:
            res += new_prefix + "└── .\n"  # Marqueur pour fils manquant

        return res

    def parcours_largeur(self):
        """Parcours de l'arbre en largeur."""
        res = []
        file = [self]
        
        while file:
            noeud = file.pop(0)
            res.append(noeud.valeur)
            
            if noeud.a_gauche():
                file.append(noeud.gauche)
            if noeud.a_droit():
                file.append(noeud.droit)
        
        return res
        
    def parcours_prefixe(self):
        """Parcours préfixe (racine, gauche, droit)."""
        res = [self.valeur]
        if self.a_gauche():
            res += self.gauche.parcours_prefixe()
        if self.a_droit():
            res += self.droit.parcours_prefixe()
        return res
    
    def parcours_infixe(self):
        """Parcours infixe (gauche, racine, droit)."""
        res = []
        if self.a_gauche():
            res += self.gauche.parcours_infixe()
        res.append(self.valeur)
        if self.a_droit():
            res += self.droit.parcours_infixe()
        return res
    
    def parcours_suffixe(self):
        """Parcours suffixe (gauche, droit, racine)."""
        res = []
        if self.a_gauche():
            res += self.gauche.parcours_suffixe()
        if self.a_droit():
            res += self.droit.parcours_suffixe()
        res.append(self.valeur)
        return res
