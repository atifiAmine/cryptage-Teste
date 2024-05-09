def cryptage(key_phrase,caractere):
    ascii_value = ord(caractere) +65
    resultat = ascii_value
    return resultat

key_phrase = input("Veuillez entrer une clé : ")
with open("ancien.txt",'r') as fichier :
    contenu = fichier.read()

contenu_crypte =""
for caractere in contenu : 
    resultat2 = cryptage(key_phrase,caractere)
    contenu_crypte = contenu_crypte + chr(resultat2)

nouveau_fichier = input("Le fichier est désormais crypté! Veuillez le renommer :")
with open(nouveau_fichier,'w') as fichier_crypte:
    fichier_crypte.write(contenu_crypte)

 
     




    




    


   