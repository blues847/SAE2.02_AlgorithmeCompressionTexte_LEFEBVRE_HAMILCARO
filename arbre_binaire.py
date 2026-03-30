# Ici ce trouve les codes pour manipuler/afficher les donners des arbres
class NoeudBinaire:
    def __init__(self, valeur=None, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
    def est_vide(self):
        return self.valeur is None
    
    def est_feuille(self):
        return self.gauche is None and self.droit is None
    
    def a_gauche(self):
        return self.gauche is not None
    
    def a_droit(self):
        return self.droit is not None
    
    def hauteur(self):
        if self.est_feuille():
            return 1
        h_g = self.gauche.hauteur() if self.a_gauche else 0
        h_d = self.droit.hauteur() if self.a_droit else 0
        return 1+max(h_g, h_d)
    
    def parcours_prefixe(self):
        res=[self.valeur]
        if self.a_gauche():
            res += self.gauche.parcours_prefixe()
        if self.a_droit():
            res += self.droit.parcours_prefixe()
        return res
    
    def parcours_infixe(self):
        res=[]
        if self.a_gauche():
            res += self.gauche.parcours_infixe()
        res.append(self.valeur)
        if self.a_droit():
            res += self.droit.parcours_infixe()
        return res
    
    def parcours_suffixe(self):
        res=[]
        if self.a_gauche():
            res += self.gauche.parcours_suffixe()
        if self.a_droit():
            res += self.droit.parcours_suffixe()
        res.append(self.valeur)
        return res
    
    def __str__(self, niveau=0):
        ret=""
        if self.a_droit():
            ret += self.droit.__str__(niveau + 1)
        ret += "\t" * niveau + repr(self.valeur) + "\n"
        if self.a_gauche():
            ret += self.gauche.__str__(niveau + 1)
        return ret


gauche_gauche = NoeudBinaire("C")
gauche_droit = NoeudBinaire("D")
droite = NoeudBinaire("E")

# Sous-arbres
gauche = NoeudBinaire("B", gauche_gauche, gauche_droit)
racine = NoeudBinaire("A", gauche, droite)

print(racine)
