def cryptage_caractere (caractere):
    resultat = ord(caractere) + 65 
    if caractere.isupper():
        resultat += 32

    return resultat

caracteres = input("Veuillez entrer des caracteres : ")
contenu_crypte = ""
for i in range(len(caracteres)):
    caractere_crypte = caracteres[i]
    Resultat = cryptage_caractere(caractere_crypte)
    contenu_crypte += chr(Resultat)
print (contenu_crypte)

'''
-fonction decryptage_caracteres() est une fonction pour décrypter les caracteres cryptes dans fonction cryptage_caracteres
-(contenu_crypte) > variable contenant  les caracteres cryptes auparavant
-focntion decryptage_caracteres est  la valeur de contenu_crypte en ascii et soustrait 65 pour trouver valeur d'origine
return resultat > on retourne ce résultat dans "resultat"

'''
def  decryptage_caracteres(contenu_crypte):
    resultat = ord(contenu_crypte)- 65
    return resultat

'''
contenu_decrypte> on initialise "contenu-decrype" à un espace vide
boucle > on rapelle la fonction pour tous le contenu de contenu_crypte, soit pour tous les caracteres cryptes pour qu'ils soient décryptes 
'''
contenu_decrypte = ""
for i in range(len(contenu_crypte)):
    caractere_decrypte = contenu_crypte[i]
    Resultat = decryptage_caracteres(caractere_decrypte)
    contenu_decrypte += chr(Resultat)
print (contenu_decrypte)


