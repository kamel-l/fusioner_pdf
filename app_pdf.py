import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def selectionner_fichiers():
    fichiers = filedialog.askopenfilenames(filetypes=[("Fichiers PDF", "*.pdf")])
    liste_fichiers.delete(0, tk.END)
    for fichier in fichiers:
        liste_fichiers.insert(tk.END, fichier)

def fusionner_pdfs():
    fichiers = liste_fichiers.get(0, tk.END)
    if not fichiers:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné")
        return
    
    fichier_sortie = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Fichiers PDF", "*.pdf")])
    if not fichier_sortie:
        return
    
    merger = PdfMerger()
    for fichier in fichiers:
        merger.append(fichier)
    
    merger.write(fichier_sortie)
    merger.close()
    messagebox.showinfo("Succès", "Fusion terminée avec succès !")

def supprimer_selection():
    selection = liste_fichiers.curselection()
    for index in reversed(selection):
        liste_fichiers.delete(index)

def vider_liste():
    liste_fichiers.delete(0, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Fusionneur de PDF")
root.geometry("500x400")

# Boutons et liste
frame = tk.Frame(root)
frame.pack(pady=10)

liste_fichiers = tk.Listbox(frame, width=60, height=10)
liste_fichiers.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame, orient="vertical", command=liste_fichiers.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
liste_fichiers.config(yscrollcommand=scrollbar.set)

btn_selectionner = tk.Button(root, text="Sélectionner fichiers", command=selectionner_fichiers)
btn_selectionner.pack(pady=5)

btn_fusionner = tk.Button(root, text="Fusionner PDFs", command=fusionner_pdfs)
btn_fusionner.pack(pady=5)

btn_supprimer = tk.Button(root, text="Supprimer sélection", command=supprimer_selection)
btn_supprimer.pack(pady=5)

btn_vider = tk.Button(root, text="Vider la liste", command=vider_liste)
btn_vider.pack(pady=5)

root.mainloop()
