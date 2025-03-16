from PyPDF2 import PdfMerger
import os

def fusionner_pdfs(fichiers, sortie, taille_max=400 * 1024 * 1024):
    merger = PdfMerger()
    
    for fichier in fichiers:
        merger.append(fichier)
    
    merger.write(sortie)
    merger.close()
    
    if os.path.getsize(sortie) > taille_max:
        print("Le fichier final dépasse la limite de 500 Mo. Essayez de réduire la taille des fichiers source.")
    else:
        print("Fusion terminée avec succès !")

# Exemple d'utilisation
fichiers_a_fusionner = ["as1.pdf", "as2.pdf"]
nom_fichier_sortie = "as.pdf"

fusionner_pdfs(fichiers_a_fusionner, nom_fichier_sortie)




