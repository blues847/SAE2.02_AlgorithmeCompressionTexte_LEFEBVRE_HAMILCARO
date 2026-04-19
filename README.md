# SAÉ 2.02 — Compression de texte avec l’algorithme de Huffman

Ce projet a été réalisé dans le cadre de la SAÉ 2.02. Il consiste à implémenter en Python l’algorithme de compression de Huffman appliqué à des fichiers texte. L’objectif est de compresser des fichiers .txt, de réduire leur taille, de pouvoir les décompresser et d’analyser l’efficacité de la compression.

## Fonctionnalités

Le programme permet de lire un ou plusieurs fichiers texte, de nettoyer le texte afin de le rendre strictement ASCII, de compter les occurrences des caractères, de construire un arbre de Huffman, de générer les codes binaires associés, de compresser et décompresser le texte, de vérifier la cohérence entre le texte compressé et le texte décompressé, de calculer la taille avant et après compression ainsi que le taux de compression, et d’exporter automatiquement les résultats dans un fichier CSV. Une interface utilisateur interactive sous forme de menu est proposée.

## Organisation du projet

├── input/  
│   └── fichiers .txt à compresser  
├── NoeudBinaire.py  
├── NoeudHuffman.py  
├── data.py  
├── main.py  
├── resultats_compression.csv  
└── README.md  

NoeudBinaire.py définit la structure générique d’un arbre binaire et fournit les méthodes nécessaires à sa manipulation.  
NoeudHuffman.py implémente l’algorithme de Huffman en s’appuyant sur l’arbre binaire.  
data.py regroupe les fonctions utilitaires : nettoyage ASCII, compression, calcul et affichage des statistiques, et export des données vers un fichier CSV.  
main.py est le point d’entrée du programme et gère le menu interactif ainsi que les choix de l’utilisateur.

## Utilisation

Les fichiers texte à compresser doivent être placés dans le dossier input/. Le programme se lance avec la commande suivante :

python main.py , tout en etant à la racine du projet

Un menu s’affiche alors et permet soit de compresser un fichier précis, soit de compresser l’ensemble des fichiers du dossier (mode résumé). Dans le cas d’un fichier unique, un sous-menu permet d’afficher les statistiques, l’arbre de Huffman, la table des codes, le texte original, le texte nettoyé et le texte décompressé.

## Export CSV

À chaque exécution du programme, le fichier resultats_compression.csv est réinitialisé. Une ligne est ajoutée pour chaque fichier compressé, que ce soit en mode fichier unique ou en mode résumé. Le fichier CSV contient le nom du fichier, la taille avant compression en bits, la taille après compression en bits, le taux de compression en pourcentage, le nombre de caractères, le nombre de symboles distincts et la longueur du texte compressé.


## Conclusion

Ce projet met en œuvre les arbres binaires, la programmation orientée objet et un algorithme de compression. Il permet d’analyser concrètement l’efficacité de l’algorithme de Huffman sur différents fichiers texte et de vérifier la cohérence entre la compression et la décompression.