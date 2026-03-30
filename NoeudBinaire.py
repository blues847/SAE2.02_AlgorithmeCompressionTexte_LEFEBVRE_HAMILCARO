class NoeudBinaire:
    """
    """
    
    #Constructeur
    def __init__(self, valeur):
        self.courant = valeur
        self.gauche = None
        self.droite = None
    
    #Getters
    def getValeur(self):
        return self.courant
    
    def getGauche(self):
        return self.gauche
    
    def getDroite(self):
        return self.droite
    
    #Setters
    def setValeur(self, valeur_):
        self.courant = valeur_
        
    def setGauche(self, gauche_):
        self.gauche = gauche_
        
    def setDroite(self, droite_):
        self.droite = droite_
        

    