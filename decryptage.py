def cryptage_caractere(caracteres, cle_phrase):
    contenu_crypte = ""
    for i in range(len(caracteres)):
        caractere = caracteres[i]
        cle_caractere = cle_phrase[i % len(cle_phrase)]
        ascii_value = (ord(caractere) + ord(cle_caractere) + 3) 
        contenu_crypte += chr(ascii_value)
    return contenu_crypte

def decryptage_caractere(contenu_crypte, cle_phrase):
    contenu_decrypte = ""
    for i in range(len(contenu_crypte)):
        caractere2 = contenu_crypte[i]
        cle_caractere2 = cle_phrase[i % len(cle_phrase)]
        ascii_value = (ord(caractere2) - ord(cle_caractere2) - 3)
        contenu_decrypte += chr(ascii_value)
    return contenu_decrypte

# Entrée des caractères et de la clé pour le cryptage
caracteres = input("Veuillez entrer des caractères : ")
cle_phrase = input("Veuillez entrer une clé : ")

# Appel de la fonction de cryptage et affichage du résultat
resultat_crypte = cryptage_caractere(caracteres, cle_phrase)
print("Le texte crypté est :", resultat_crypte)

# Entrée du texte crypté et de la clé pour le décryptage
cle_phrase2 = input("Veuillez entrer la même clé de cryptage : ")

# Appel de la fonction de décryptage et affichage du résultat
resultat_decrypte = decryptage_caractere(resultat_crypte, cle_phrase2)
print("Le texte décrypté est :", resultat_decrypte)


