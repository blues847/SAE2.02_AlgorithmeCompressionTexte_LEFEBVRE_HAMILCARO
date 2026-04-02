class NoeudBinaire:
    """
    Cette classe implémente un noeud appartenant à un arbre binaire.
    """
    
    #Constructeur
    def __init__(self, valeur_ = None, gauche_ = None, droit_ = None):
        self.valeur = valeur_
        self.gauche = gauche_
        self.droit = droit_

    #Getters
    def getValeur(self):
        return self.valeur
    
    def getGauche(self):
        return self.gauche
    
    def getDroit(self):
        return self.droit
    
    #Setters
    def setValeur(self, valeur_):
        self.valeur = valeur_
        
    def setGauche(self, gauche_):
        self.gauche = gauche_
        
    def setDroit(self, droit_):
        self.droit = droit_
        
    #Méthodes
        #Sous-arbre gauche
    def a_gauche(self):
        return self.gauche is not None
        
        #Sous-arbre droit
    def a_droit(self):
        return self.droit is not None
    
        #Est une feuille
    def estFeuille(self):
        return self.gauche is None and self.droit is None and self.valeur is not None
        
        #Est un arbre vide
    def estVide(self):
        return self.valeur is None

        #Hauteur
    def hauteur(self):
        if self.estFeuille():
            return 1
        elif self.gauche == None:
            return 1 + self.droit.hauteur()
        elif self.droit == None:
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())
    
        #Affichage de l'arbre dans le terminal
    def __str__(self, prefix="", is_left=True, is_root=True):
        res = ""

        # -------- Racine --------
        if is_root:
            res += repr(self.valeur) + "\n"
            new_prefix = ""
        else:
            connector = "├── " if is_left else "└── "
            res += prefix + connector + repr(self.valeur) + "\n"
            new_prefix = prefix + ("│   " if is_left else "    ")

        # -------- Sous-arbre gauche --------
        if self.gauche:
            res += self.gauche.__str__(new_prefix, True, False)
        elif self.droit:
            # Pas de fils gauche → remplacer par point mais garder le trait
            res += new_prefix + "├── .\n"

        # -------- Sous-arbre droit --------
        if self.droit:
            res += self.droit.__str__(new_prefix, False, False)
        elif self.gauche:
            # Pas de fils droit → point avec trait bas
            res += new_prefix + "└── .\n"

        return res

        #Parcours en largeur
    def parcours_largeur(self):
        res = []
        file = [self]  # File d'attente, on commence par la racine
        
        while file:
            noeud = file.pop(0)  # On retire le premier élément
            res.append(noeud.valeur)
            
            if noeud.a_gauche():
                file.append(noeud.gauche)
            if noeud.a_droit():
                file.append(noeud.droit)
        
        return res
        
        #Parcours en profondeur
            #Parcours préfixe
    def parcours_prefixe(self):
        res=[self.valeur]
        if self.a_gauche():
            res += self.gauche.parcours_prefixe()
        if self.a_droit():
            res += self.droit.parcours_prefixe()
        return res
    
            #Parcours infixe
    def parcours_infixe(self):
        res=[]
        if self.a_gauche():
            res += self.gauche.parcours_infixe()
        res.append(self.valeur)
        if self.a_droit():
            res += self.droit.parcours_infixe()
        return res
    
            #Parcours suffixe
    def parcours_suffixe(self):
        res=[]
        if self.a_gauche():
            res += self.gauche.parcours_suffixe()
        if self.a_droit():
            res += self.droit.parcours_suffixe()
        res.append(self.valeur)
        return res
    
    
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

"""
print("=== Tests ===")
print("Schema de l'arbre:\n", a.__str__())
print("Valeur de a:", a.getValeur())              						# A
print("Valeur de son sous-arbre gauche:", a.getGauche().getValeur())    # B
print("Valeur de son sous-arbre droit:", a.getDroit().getValeur())    	# A
print("a a un gauche?", a.a_gauche())             						# True
print("a a un droit?", a.a_droit())               						# True
print("g est feuille?", g.estFeuille())           						# True
print("a est feuille?", a.estFeuille())           						# False
print("a est vide?", a.estVide())                 						# False
print("Hauteur depuis a:", a.hauteur())               					# 4

print("\n=== Parcours ===")
print("Préfixe:", a.parcours_prefixe())       	# ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print("Infixe:", a.parcours_infixe())          	# ['C', 'B', 'D', 'A', 'E', 'G', 'F']
print("Suffixe:", a.parcours_suffixe())       	# ['C', 'D', 'B', 'G', 'F', 'E', 'A']
print("Largeur:", a.parcours_largeur()) 		# ['A', 'B', 'E', 'C', 'D', 'F', 'G']
"""