def cryptage_caractere (caractere):
    resultat =(ord(caractere) + 65 )%127
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




