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
   
   
   
   
