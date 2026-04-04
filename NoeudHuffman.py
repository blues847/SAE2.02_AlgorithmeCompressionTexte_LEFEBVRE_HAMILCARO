from NoeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Classe qui implémente un arbre d'Huffman, utilisant la classe NoeudBinaire.
    """

    # Constructeur
    def __init__(self, chaine=None, poids=None, gauche=None, droit=None):
        # La valeur stockée est un couple (chaine, poids)
        super().__init__((chaine, poids), gauche, droit)

    # Getters
    def getChaine(self):
        return self.valeur[0]

    def getPoids(self):
        return self.valeur[1]

    # Setters
    def setValeur(self, chaine_, poids_):
        self.valeur = (chaine_, poids_)

    def setChaine(self, chaine_):
        self.valeur = (chaine_, self.valeur[1])

    def setPoids(self, poids_):
        self.valeur = (self.valeur[0], poids_)

    # Méthodes
    """
    Construire un arbre de Huffman à partir d'une chaîne de caractères reçue en paramètre :
        - Par pair (et deux pairs par deux pairs) concaténer les caractères
          et additionner leurs poids
        - Ajouter à l'arbre au moment de la concaténation les caractères seuls
          et leurs nouveaux parents
        - Continuer ainsi jusqu'à avoir la chaine entière en racine
        - Permettre l'affichage de cet arbre

    A partir d'une chaine de caractères et d'un arbre d'Huffman associé,
    calculer le nouvel encodage après compression de chaque caractère :
        - Utiliser l'arbre (relation noeud - sous-arbre) pour retracer l'encodage

    A partir d'une chaine de caractères et d'un encodage d'Huffman associé,
    construire et renvoyer la chaîne de caractères obtenue après compression

    Bonus :
        - afficher les 0 et les 1 dans l'affichage de l'arbre d'Huffman
    """

    # 1. Comptage des occurrences
    @staticmethod
    def compte_Occurrences(chaine):
        """
        Cette méthode prend en paramètre une chaîne de caractères
        et renvoie un dictionnaire ayant pour clé chaque caractère
        et pour valeur le nombre d'apparitions de ce caractère.
        Le dictionnaire est trié par ordre croissant de fréquence.
        """
        frequence = {}
        for caractere in chaine:
            if caractere not in frequence:
                frequence[caractere] = 1
            else:
                frequence[caractere] += 1

        # Tri par fréquence croissante
        frequence = dict(sorted(frequence.items(), key=lambda item: item[1]))
        return frequence

    # 2. Construction de l'arbre de Huffman
    @staticmethod
    def concatenation(dico_occur):
        """
        Cette méthode reçoit en paramètre un dictionnaire des
        occurrences des caractères dans une chaîne trié par ordre croissant.
        Elle construit l'arbre de Huffman et renvoie la racine.
        """

        # Création des feuilles
        noeuds = []
        for caractere, poids in dico_occur.items():
            noeuds.append(NoeudHuffman(caractere, poids, None, None))

        # Construction progressive de l'arbre
        while len(noeuds) > 1:
            # Trie la liste noeuds en utilisant comme critère le poids de chaque noeud et pas la clé
            noeuds.sort(key=lambda n: n.getPoids())

            # Prendre les deux plus petits
            gauche = noeuds.pop(0)
            droite = noeuds.pop(0)

            # Créer le noeud parent
            nouvelle_chaine = gauche.getChaine() + droite.getChaine()
            nouveau_poids = gauche.getPoids() + droite.getPoids()

            parent = NoeudHuffman(nouvelle_chaine,nouveau_poids,gauche,droite)

            # Réinsérer le noeud parent
            noeuds.append(parent)

        # Le dernier noeud est la racine
        return noeuds[0]

    # 3. Génération des codes de Huffman
    @staticmethod
    def generer_codes(racine):
        """
        Génère le code de Huffman de chaque caractère
        à partir de l'arbre de Huffman.
        """
        codes = {}

        def parcours(noeud, code):
            if noeud.estFeuille():
                codes[noeud.getChaine()] = code
                return

            if noeud.gauche:
                parcours(noeud.gauche, code + "0")
            if noeud.droit:
                parcours(noeud.droit, code + "1")

        parcours(racine, "")
        return codes

    # 4. Compression
    @staticmethod
    def compresser(chaine, codes):
        """
        Compresse une chaîne de caractères à l'aide
        du dictionnaire de codes Huffman.
        """
        resultat = ""
        for caractere in chaine:
            resultat += codes[caractere]
        return resultat

    # 5. Décompression
    @staticmethod
    def decompresser(binaire, racine):
        """
        Décompresse une chaîne binaire à l'aide
        de l'arbre de Huffman.
        """
        resultat = ""
        noeud = racine

        for bit in binaire:
            if bit == "0":
                noeud = noeud.gauche
            else:
                noeud = noeud.droit

            if noeud.estFeuille():
                resultat += noeud.getChaine()
                noeud = racine

        return resultat


# Tests temporaires
if __name__ == "__main__":
    texte = "J'ai pas d'inspiration pour le test"

    print("Texte :", texte)

    dico = NoeudHuffman.compte_Occurrences(texte)
    print("\nDictionnaire des occurrences :")
    print(dico)

    racine = NoeudHuffman.concatenation(dico)
    print("\nArbre de Huffman :")
    print(racine)

    codes = NoeudHuffman.generer_codes(racine)
    print("\nCodes de Huffman :")
    print(codes)

    compresse = NoeudHuffman.compresser(texte, codes)
    print("\nTexte compressé :")
    print(compresse)

    decompresse = NoeudHuffman.decompresser(compresse, racine)
    print("\nTexte décompressé :")
    print(decompresse)