class NoeudBinaire:
    """
    Cette classe implémente un noeud appartenant à un arbre binaire.
    """
    
    #Constructeur
    def __init__(self, valeur, gauche_ = None, droite_ = None):
        self.courant = valeur
        self.gauche = gauche_
        self.droite = droite_
    
    #Getters
    def getValeur(self):
        return self.courant
    
    def getGauche(self):
        return self.gauche
    
    def getDroite(self):
        return self.droite
    
    #Setters
    def setValeur(self, valeur_):
        self.courant = valeur_
        
    def setGauche(self, gauche_):
        self.gauche = gauche_
        
    def setDroite(self, droite_):
        self.droite = droite_
        
    #Méthodes
        #Sous-arbre gauche
    def aGauche(self):
        if self.gauche is not None:
            return 1
        else:
            return 0
        
        #Sous-arbre droit
    def aDroite(self):
        if self.droite is not None:
            return 1
        else:
            return 0
        
        #Est une feuille
    def estFeuille(self):
        if aGauche == 0 and aDroite == 0:
            return 1
        else:
            return 0
        
        #Est un arbre vide
    def estVide(self):
        if aGauche == 0 and aDroite == 0 and self.courant is None:
            return 1
        else:
            return 0
        
        #Hauteur
    #def hauteur(self):
        
        #Affichage de l'arbre
    def __str__(self, fleche=0, espace=""):
        if fleche > 0:
            print(espace + "|--> " + self.courant)
        else:
            print(self.courant)
            
        if self.gauche is not None:
            if fleche == 0:
                self.gauche.__str__(fleche + 1, "")
            else:
                self.gauche.__str__(fleche + 1, espace + "     ")
            
        if self.droite is not None:
            if fleche == 0:
                self.droite.__str__(fleche + 1, "")
            else:
                self.droite.__str__(fleche + 1, espace + "     ")
        
        return ""
                
        
        #Parcours préfixe
        
        #Parcours suffixe
        
        #Parcours infixe
        
        #Parcours largeur
        
        #Parcours profondeur
        
g = NoeudBinaire('G', None, None) # Arbre de valeur 'G', sans sous-arbre (feuille)
# Arbre de valeur 'F'. Sous-arbre gauche : g. Pas sous-arbre droit.
f = NoeudBinaire('F', g, None)
# Arbre de valeur 'E'. Pas de sous-arbre gauche. Sous-arbre droit : f
e = NoeudBinaire('E', None, f)
d = NoeudBinaire('D', None, None) # Arbre de valeur 'D', sans sous-arbres (feuille)
c = NoeudBinaire('C', None, None) # Arbre de valeur 'C', sans sous-arbres (feuille)
# Arbre de valeur 'B', sous-arbre gauche : c. Sous-arbre droit : d.
b = NoeudBinaire('B', c, d)
# Arbre de valeur 'A', sous-arbre gauche : b. Sous-arbre droit : e.
a = NoeudBinaire('A', b, e)
a.__str__()