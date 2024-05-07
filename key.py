import os
def cryptage():
    key_phrase = input("Veuillez entrer la clé : ")
    for i in range(len(key_phrase)):
        ascii_value = ord(key_phrase[i]) + 65 
        print(ascii_value)
with open("text.txt","r") as fichier :
    contenu = fichier.read()
    for caractere in contenu :
        cryptage()


        

    




    


   