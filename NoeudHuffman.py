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
    
    @staticmethod
    def compte_Occurrences(chaine):
        """
        Cette méthode prend en paramètre une chaîne de caractère
        et renvoie un dictionnaire ayant pour clé chaque caractère (sans doublons)
        et pour valeur le nombre d'apparition de ce caractère dans la chaîne.
        Le dictionnaire est trié par ordre croissant de valeur (pas de clé).
        """
        frequence = dict()
        for caractere in chaine:
            if caractere not in frequence.keys():
                frequence[caractere] = 1
            else:
                frequence[caractere] += 1
        frequence = dict(sorted(frequence.items(), key=lambda item: item[1]))
        return frequence
    
    @staticmethod
    def concatenation(dico_occur):
        """
        Cette méthode reçoit en paramètre un dictionnaire des
        occurences des caractères dans une chaîné trié par ordre croissant.
        Il créé des NoeudHuffman selon la logique de l'arbre d'Huffman.
        """
        cara_prec = ""
        val_prec = 0
        while len(dico_occur) != 1:
            for c in dico_occur.keys():
                if cara_prec == "":
                    cara_prec = c
                    val_prec = dico_occur[c]
                else:
                    cara_nv = cara_prec + c
                    val_nv = val_prec + dico_occur[c]
                    dico_occur[cara_nv] = val_nv
                    dico_occur = dict(sorted(dico_occur.items(), key=lambda item: item[1]))
                    cara_prec = c
                    val_prec = dico_occur[c]
                    break
        return dico_occur #JE N'Y ARRIVE PAs
            
   
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

    #Deuxième arbre plus complexe ("Quelque chose")
A = NoeudHuffman("s", 1, None, None)
B = NoeudHuffman("o", 1, None, None)
C = NoeudHuffman("h", 1, None, None)
D = NoeudHuffman("c", 1, None, None)
E = NoeudHuffman("q", 1, None, None)
F = NoeudHuffman("l", 1, None, None)
G = NoeudHuffman(" ", 1, None, None)
H = NoeudHuffman("Q", 1, None, None)
I = NoeudHuffman("u", 2, None, None)
K = NoeudHuffman("so", 2, A, B)
L = NoeudHuffman("hc", 2, C, D)
M = NoeudHuffman("ql", 2, E, F)
N = NoeudHuffman(" Q", 2, G, H)
J = NoeudHuffman("e", 3, None, None)
O = NoeudHuffman("uso", 4, I, K)
P = NoeudHuffman("hcql", 4, L, M)
Q = NoeudHuffman(" Qe", 5, N, J)
R = NoeudHuffman("usohcql", 8, O, P)
S = NoeudHuffman(" Qeusohcql", 13, Q, R)

    #Constructeur, getters, setters
print("===[Tests] : constructeur, getters, setters===")
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

    #Méthodes
print("===[Tests] : méthodes===")
dico_ex2 = NoeudHuffman.compte_Occurrences('Quelque chose')
print(f"\nDictionnaire des occurences d'un caractère dans une chaîne : \n{dico_ex2}")
print(f"Nouveau dico : {NoeudHuffman.concatenation(dico_ex2)}")