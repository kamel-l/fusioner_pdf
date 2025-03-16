from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def fusionner_pdfs(fichiers, sortie, taille_max=500 * 1024 * 1024):
    merger = PdfMerger()
    
    for fichier in fichiers:
        merger.append(fichier)
    
    merger.write(sortie)
    merger.close()
    
    if os.path.getsize(sortie) > taille_max:
        print("Le fichier final dépasse la limite de 500 Mo. Essayez de réduire la taille des fichiers source.")
    else:
        print("Fusion terminée avec succès !")

def compresser_pdf(entree, sortie):
    reader = PdfReader(entree)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)
    
    with open(sortie, "wb") as fichier_sortie:
        writer.write(fichier_sortie)
    
    print("Compression terminée avec succès !")

# Exemple d'utilisation
fichiers_a_fusionner = ["fm1.pdf", "fm2.pdf", "fmn1.pdf", "fmn2.pdf"]
nom_fichier_sortie = "fusionne.pdf"
nom_fichier_compresse = "fusionne_compresse.pdf"

fusionner_pdfs(fichiers_a_fusionner, nom_fichier_sortie)
compresser_pdf(nom_fichier_sortie, nom_fichier_compresse)
