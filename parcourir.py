def parcourir(fichier_selectionne):
    with open(fichier_selectionne,'r',encoding="utf-8") as fichier :
        contenu = fichier.read()
        return contenu 
  
nom_fichier = r"C:\Users\atifi_a\Documents\capteurSR04\projet\fichier.txt"
contenu_fichier = parcourir(nom_fichier)
print(contenu_fichier)