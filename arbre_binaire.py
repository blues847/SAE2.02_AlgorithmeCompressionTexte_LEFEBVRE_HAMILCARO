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
    
    def __str__(self, prefix="", is_root=True):
        res = ""
        if self.droit:
            res += self.droit.__str__(prefix + "    ", False)
        if is_root:
            res += repr(self.valeur) + "\n"
        else:
            res += prefix[:-4] + "|-- " + repr(self.valeur) + "\n"
        if self.gauche:
            res += self.gauche.__str__(prefix + "    ", False)
        return res

H = NoeudBinaire("H")
M = NoeudBinaire("M")
N = NoeudBinaire("N")
I = NoeudBinaire("I", M, N)
O = NoeudBinaire("O")

D = NoeudBinaire("D", H, I)
E = NoeudBinaire("E")
J = NoeudBinaire("J")
K = NoeudBinaire("K", None, O)
L = NoeudBinaire("L")

F = NoeudBinaire("F", J, None)
G = NoeudBinaire("G", K, L)

B = NoeudBinaire("B", D, E)
C = NoeudBinaire("C", F, G)

A = NoeudBinaire("A", B, C)

# Affichage
print(A)
