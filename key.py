def cryptage (caractere,cle):
    resultat =(ord(caractere) + ord(cle))%127
    return resultat
key_phrase = input("Veullez entrer une clé : ")
with open(r"C:\Users\amine\OneDrive\Documents\entrainement\u.txt",'r',encoding="utf-8") as fichier :
    contenu = fichier.read()

contenu_crypte = ""
for i in range(len(contenu)):
    caractere = contenu[i]
    cle = key_phrase[i % len(key_phrase)]
    Resultat = cryptage(caractere,cle)
    contenu_crypte += chr(Resultat)

Nouveau_fichier = input("Le fichier est crypte! Renommez-le : ")
with open(Nouveau_fichier,'w',encoding="utf-8") as fichier_crypte :
    fichier_crypte.write(contenu_crypte)

def decryptage (caractere,cle):
    resultat =(ord(caractere) - ord(cle)+127)%127
    return resultat

with open(Nouveau_fichier,'r',encoding="utf-8") as fichier_crypte :
    contenu = fichier_crypte.read()

contenu_decrypte = ""
for i in range(len(contenu)):
    caractere = contenu[i]
    cle = key_phrase[i % len(key_phrase)]
    Resultat = decryptage(caractere,cle)
    contenu_decrypte += chr(Resultat)

NNouveau_fichier = input("Le fichier est decrypte! Renommez-le : ")
with open(NNouveau_fichier,'w',encoding="utf-8") as fichier_decrypte :
    fichier_decrypte.write(contenu_decrypte)








 
     




    




    


   