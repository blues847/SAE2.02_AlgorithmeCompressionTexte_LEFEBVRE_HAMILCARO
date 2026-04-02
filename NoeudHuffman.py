from NoeudBinaire import NoeudBinaire
class NoeudHuffman(NoeudBinaire):
    
    def compter_occurrences(texte):
        freqs = {}
        for c in texte:
            freqs[c] = freqs.get(c, 0) + 1
   
print("A")