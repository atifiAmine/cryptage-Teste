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
    contenu = fichier.read()

contenu_crypte =""
for caractere in contenu : 
    resultat2 = cryptage(key_phrase,caractere)
    contenu_crypte = contenu_crypte + chr(resultat2)

nouveau_fichier = input("Le fichier est désormais crypté! Veuillez le renommer :")
with open(nouveau_fichier,'w') as fichier_crypte:
    fichier_crypte.write(contenu_crypte)


 
     




    




    


   