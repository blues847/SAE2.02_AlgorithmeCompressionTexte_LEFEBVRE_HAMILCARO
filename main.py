import sys
import os
from data import Data

def main():
    """Point d'entrée principal pour l'interface de compression interactive."""
    
    DOSSIER_INPUT = "input"

    while True:
        print("\n===== Interface de Compression Huffman =====")
        
        if not os.path.isdir(DOSSIER_INPUT):
            print(f"\nERREUR : Le dossier '{DOSSIER_INPUT}/' est introuvable.")
            return

        fichiers_txt = [f for f in os.listdir(DOSSIER_INPUT) if f.endswith('.txt')]

        if not fichiers_txt:
            print(f"\nAUCUN fichier .txt trouve dans '{DOSSIER_INPUT}/'.")
            return

        print("\nFichiers disponibles :")
        for i, nom_fichier in enumerate(fichiers_txt, 1):
            print(f"  {i}. {nom_fichier}")
        
        print("\nA. Compresser TOUS les fichiers (mode resume)")
        print("Q. Quitter")
        
        choix_principal = input("\nVotre choix : ").strip().upper()

        if choix_principal == 'Q':
            print("Au revoir !")
            break
        
        elif choix_principal == 'A':
            print("\n--- Traitement de tous les fichiers ---")
            for nom_fichier in fichiers_txt:
                chemin_complet = os.path.join(DOSSIER_INPUT, nom_fichier)
                print(f"\n----- Fichier : {nom_fichier} -----")
                print("Traitement en cours...")
                try:
                    with open(chemin_complet, 'r', encoding='utf-8') as f:
                        texte = f.read()
                    if not texte.strip():
                        print("Fichier vide.")
                        break
                    
                    texte_propre = Data.nettoyer_texte(texte)
                    texte_compresse, _, _ = Data.compresser_texte(texte_propre)
                    Data.afficher_stat(texte_propre, texte_compresse)
                    
                except Exception as e:
                    print(f"Une erreur est survenue : {e}")
            print("\n--- Fin du traitement de tous les fichiers ---")

        elif choix_principal.isdigit():
            try:
                index_choisi = int(choix_principal) - 1
                if not (0 <= index_choisi < len(fichiers_txt)):
                    print("Numero de fichier invalide.")
                    break

                nom_fichier_choisi = fichiers_txt[index_choisi]
                chemin_fichier = os.path.join(DOSSIER_INPUT, nom_fichier_choisi)

                print("\nTraitement en cours, veuillez patienter...")
                with open(chemin_fichier, 'r', encoding='utf-8') as file:
                    texte_original = file.read()

                if not texte_original.strip():
                    print("Le fichier est vide.")
                    break

                texte_propre = Data.nettoyer_texte(texte_original)
                texte_compresse, racine, codes = Data.compresser_texte(texte_propre)
                texte_decompresse = Data.decompresser_texte(texte_compresse, racine)

                print(f"\nFichier '{nom_fichier_choisi}' traite avec succes.")

                while True:
                    print(f"\n--- Menu d'actions pour : {nom_fichier_choisi} ---")
                    print("1. Afficher les statistiques")
                    print("2. Afficher l'arbre de Huffman")
                    print("3. Afficher la table des codes")
                    print("4. Afficher le texte original")
                    print("5. Afficher le texte nettoye")
                    print("6. Afficher le texte decompresse et verifier")
                    print("R. Revenir au menu principal")
                    
                    choix_action = input("Votre choix : ").strip().upper()

                    if choix_action == '1':
                        Data.afficher_stat(texte_propre, texte_compresse)
                    elif choix_action == '2':
                        Data.afficher_arbre_console(racine)
                    elif choix_action == '3':
                        Data.afficher_table_codes(codes)
                    elif choix_action == '4':
                        print("\n--- Texte Original ---\n" + texte_original)
                    elif choix_action == '5':
                        print("\n--- Texte Nettoye ---\n" + texte_propre)
                    elif choix_action == '6':
                        print("\n--- Texte Decompresse ---\n" + texte_decompresse)
                        Data.verifier_decompression(texte_propre, texte_decompresse)
                    elif choix_action == 'R':
                        break
                    else:
                        print("Choix invalide.")
            
            except (ValueError, FileNotFoundError) as e:
                print(f"Une erreur est survenue : {e}")
        
        else:
            print("Choix invalide, veuillez reessayer.")

if __name__ == "__main__":
    main()
