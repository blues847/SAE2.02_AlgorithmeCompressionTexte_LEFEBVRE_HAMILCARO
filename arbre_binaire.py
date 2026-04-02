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
            res += new_prefix + "├── .\n"

        # -------- Sous-arbre droit --------
        if self.droit:
            res += self.droit.__str__(new_prefix, False, False)
        elif self.gauche:
            res += new_prefix + "└── .\n"

        return res


# Niveau 4
J = NoeudBinaire("J")

# Niveau 3
G = NoeudBinaire("G")
H = NoeudBinaire("H", None, J)
I = NoeudBinaire("I")

# Niveau 2
D = NoeudBinaire("D")                # pas d'enfant
E = NoeudBinaire("E", G, None)       # un seul enfant
F = NoeudBinaire("F", H, I)          # deux enfants

# Niveau 1
B = NoeudBinaire("B", D, E)
C = NoeudBinaire("C", None, F)

# Racine
A = NoeudBinaire("A", B, C)

# Affichage
print(A)
