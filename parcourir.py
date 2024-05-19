'''
-parcourir() > fonction pour sélectionner le fichier 
- fichier_selectionne > argument corrspondant au fichier sélectionné 
-with open > on ouvre ce fichier
-contenu = fichier.read > on met ce fichier en mode lecture
'''
from tkinter import *
from tkinter import filedialog
def parcourir():
    chemin_fichier = filedialog.askopenfilename()
    with open(chemin_fichier, 'r', encoding="utf-8", errors="ignore") as fichier:
        contenu = fichier.read()
        print(contenu)
'''
-on rapelle la fonction "parcourir" et on stcoke dans résultat
-print resultat > on retourne "resultat", soit le contenu du fichier sélectionné 
'''
resultat= parcourir()
print (resultat)