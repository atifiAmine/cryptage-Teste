<<<<<<< HEAD
def cryptage(key_phrase,caractere):
    ascii_value = ord(caractere) 
    if 'A' <= caractere <= 'Z':
        # Convertir le caractère de la clé en valeur ASCII et normaliser sa valeur entre 0 et 25
        key_value = (ord(key_phrase.upper()) - ord('A')) % 26
        # Calculer la nouvelle valeur ASCII en ajoutant le décalage défini par la clé
        nouvelle_ascii_value = (ascii_value - ord('A') + key_value) % 26 + ord('A')
        # Retourner le caractère correspondant à la nouvelle valeur ASCII
        return chr(nouvelle_ascii_value)
    else:
        # Ne pas crypter les caractères qui ne sont pas des lettres majuscules
        return caractere


key_phrase = input("Veuillez entrer une clé : ")
with open(r"C:\Users\atifi_a\Documents\capteurSR04\projet\fichier.txt",'r') as fichier :
=======
def cryptage (caractere,cle):
    resultat =(ord(caractere) + ord(cle))%127
    return resultat
key_phrase = input("Veullez entrer une clé : ")
with open(r"C:\Users\amine\OneDrive\Documents\entrainement\u.txt",'r',encoding="utf-8") as fichier :
>>>>>>> 7caf71a45ba8702c72b72d82b3138bef3dca59fe
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








 
     




    




    


   