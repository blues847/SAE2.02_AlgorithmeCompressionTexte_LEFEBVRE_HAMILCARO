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
    """
    Construire un arbre de Huffman à partir d'une chaîne de caractères reçue en paramètre :
        - Compter le nombre d'occurence de chaque caractère (stocker)
        - Trier caractère en ordre décroissant d'occurence (stocker)
        - Par pair (et deux pairs par deux pairs) concaténer les caractères
            et additionner leurs poids
        - Ajouter à l'arbre au moment de la concaténation les caractères seuls
            et leurs nouveaux parents (niveau 1)
        - Continuer ainsi jusqu'à avoir la chaine entière en racine
        - permettre l'affichage de cet arbre
        
    A partir d'une chaine de caractères et d'un arbre d'Huffman associé,
    calculer le nouvel encodage après compression de chaque caractère :
        - Utiliser l'arbre (et les relation noeud - sous-arbre) pour retracer l'encodage (stocker)
        - Potentiellement le rendre disponible à l'aide des différents parcours?
        
    A partir d'une chaine de caractères et d'un encodage d'Huffman associé,
    construire et renvoyer la chaîne de caracère obtenu après compression :
        - Fonction qui encode une chaine avec un encodage prédéfini?
        
    Bonus :
        - afficher les 0 et les 1 dans l'affichage de l'arbre d'Huffman
    """
    
    def compteOccurrences(chaine):
        frequence = dict()
        for caractere in chaine:
            if caractere in frequence.keys():
                frequence[caractere] += 1
            else:
                frequence[caractere] = 1
        return frequence

   
#Tests
    #Initialisation d'un arbre (exemple tiré du cahier technique)
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

    #Constructeur, getters, setters
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
print(a.__str__())