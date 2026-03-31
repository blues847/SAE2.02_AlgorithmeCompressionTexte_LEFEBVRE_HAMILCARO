class NoeudBinaire:
    """Classe qui implémente un noeud dans un arbre binaire"""

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
    def setValeur(self, valeur):
        self.courant = valeur

    def setGauche(self, gauche_):
        self.gauche = gauche_

    def setDroite(self, droite_):
        self.droite = droite_

    #Méthodes
        #Sous-arbre gauche
    def aArbreGauche(self):
        if self.gauche != None:
            return 1
        else:
            return 0
            
        #Sous-arbre droit
    def aArbreDroit(self):
        if self.droite != None:
            return 1
        else:
            return 0
        
        #Est une feuille
    def estFeuille(self):
        if self.aArbreGauche() == 0 and self.aArbreDroit() == 0 and self.courant != None:
            return 1
        else:
            return 0
        
        #Est un arbre vide
    def estVide(self):
        if self.aArbreGauche() == 0 and self.aArbreDroit() == 0 and self.courant == None:
            return 1
        else:
            return 0
        
        #Hauteur
    def hauteur(self):
        if self.estFeuille() == 1:
            return 1
        elif self.gauche == None:
            return 1 + self.droite.hauteur()
        elif self.droite == None:
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur(), self.droite.hauteur())
    
        #Affichage de l'arbre dans le terminal
    def __str__(self, fleche=0, espace=""):
        #Gestion de la racine qui a un affichage unique,
        #fleche représente les "niveaux" de l'arbre
        if fleche > 0:
            print(espace + "|--> " + self.courant)
        else:
            print(self.courant)
        
        #Gestion de l'arbre gauche récursivement
        if self.gauche is not None:
            if fleche == 0:
                self.gauche.__str__(fleche + 1, "")
            else:
                self.gauche.__str__(fleche + 1, espace + "     ")
        elif self.droite is not None:
            # Pas de gauche mais un droite
            if fleche == 0:
                print("|--> .")
            else:
                print(espace + "     " + "|--> .")
            
        #Gestion de l'arbre droit récursivement (même logique)
        if self.droite is not None:
            if fleche == 0:
                self.droite.__str__(fleche + 1, "")
            else:
                self.droite.__str__(fleche + 1, espace + "     ")
        elif self.gauche is not None:
            # Pas de droite mais un gauche
            if fleche == 0:
                print("|--> .")
            else:
                print(espace + "     " + "|--> .")
        
        return

        #Parcours préfixe
    def parcoursPrefixe(self, liste=[]):
        
        
        #Parcours suffixe
        
        #Parcours infixe
        
        #Parcours en largeur
        
        #Parcours en profondeur
    
    
    
#Rapides tests intermédiaires   
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
print(a.hauteur())