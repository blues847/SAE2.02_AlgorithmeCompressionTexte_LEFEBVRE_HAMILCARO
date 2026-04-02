from NoeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Classe qui implémente un arbre d'Huffman, utilisant la classe NoeudBinaire.
    """
    #Constructeur
    def __init__(self, chaine = None, poids = None, gauche = None, droit = None):
        super().__init__((chaine, poids), gauche, droit)
        
    #Getters
    def getChaine(self):
        return self.valeur[0]
    
    def getPoids(self):
        return self.valeur[1]
    
    #Setters
    def setValeur(self, chaine_, poids_):
        self.valeur = (chaine_, poids_)
        
    def setChaine(self, chaine_):
        poids_ = self.valeur[1]
        self.valeur = (chaine_, poids_)
        
    def setPoids(self, poids_):
        chaine_ = self.valeur[0]
        self.valeur = (chaine_, poids_)
        
    #Méthodes
    def compter_occurrences(texte):
        freqs = {}
        for c in texte:
            freqs[c] = freqs.get(c, 0) + 1
   
   
#Tests
v = NoeudHuffman("r", 2, None, None)
w = NoeudHuffman("n", 2, None, None)
x = NoeudHuffman("b", 2, None, None)
y = NoeudHuffman("nr", 4, w, v)
z = NoeudHuffman("nrb", 6, y, x)
k = NoeudHuffman("j", 1, None, None)
j = NoeudHuffman("i", 1, None, None)
i = NoeudHuffman("u", 1, None, None)
h = NoeudHuffman("s", 1, None, None)
g = NoeudHuffman("ij", 2, j, k)
f = NoeudHuffman("su", 2, h, i)
d = NoeudHuffman("ijsu", 4, f, g)
c = NoeudHuffman("o", 2, None, None)
b = NoeudHuffman("oijsu", 6, c, d)
a = NoeudHuffman("oijsunrb", 14, b, z)

print("La valeur de la racine est : ", a.getValeur())
print("Sa chaîne est : ", a.getChaine())
print("Son poids est : ", a.getPoids())
print("Test : changer son poids, puis sa chaîne, pour enfin les remettre aux valeurs initiales.")
print("Test de setValeur()")
a.setValeur("reussite", 200)
print("Sa nouvelle valeur est donc : ", a.getValeur())
print("Test de setChaine() et de setPoids()")
a.setChaine("oijsunrb")
a.setPoids(14)
print("Sa nouvelle valeur est donc : ", a.getValeur())