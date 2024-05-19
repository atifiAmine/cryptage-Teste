'''
-cryptage_caractere() > fonction pour crypter les caracteres
-(caracteres) > 1er argument de la fonction correspodnant aux données entrés par utilisateur
-(cle_phrase) > 2eme argument correspodnant a la clé entrée par l'utilisateur
-for i in range(len(caracteres)): > on applique la fonction sur tous les caracteres inscris par l'utilisateur
- caractere = caracteres[i] > un caractere correspind au premier caractere de la phrase entrée par l'utilisateur
- ascii_value = (ord(caractere) + ord(cle_caractere) + 3) % 256 > 
'''
def cryptage_caractere(caracteres, cle_phrase):
    contenu_crypte = ""
    for i in range(len(caracteres)):
        caractere = caracteres[i]
        cle_caractere = cle_phrase[i % len(cle_phrase)]
        ascii_value = (ord(caractere) + ord(cle_caractere) + 3) 
        contenu_crypte += chr(ascii_value)
    return contenu_crypte

caracteres = input("Veuillez entrer des caractères : ")
cle_phrase = input("Veuillez entrer une clé : ")


resultat_crypte = cryptage_caractere(caracteres, cle_phrase)
print("Le texte crypté est :", resultat_crypte)




    
    




