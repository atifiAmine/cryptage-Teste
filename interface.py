from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def taille_image(image_path, width, height):
    original_image = Image.open(image_path)
    redimension_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(redimension_image)

def parcourir():
    chemin_fichier = filedialog.askopenfilename()
    entre_nomfichier.delete(0, END)
    entre_nomfichier.insert(0, chemin_fichier)
    with open(chemin_fichier, 'r', encoding="utf-8", errors="ignore") as fichier:
        contenu = fichier.read()
        return contenu

def cryptage_caractere(contenu, cle_phrase):
    contenu_crypte = ""
    cle_length = len(cle_phrase)

    for i in range(len(contenu)):
        caractere = contenu[i]
        cle_caractere = cle_phrase[i % cle_length]
        ascii_value = (ord(caractere) + ord(cle_caractere))+ 3 
        contenu_crypte += chr(ascii_value)

    return contenu_crypte

def decryptage_caractere(contenu, cle_phrase):
    contenu_crypte = ""
    cle_length = len(cle_phrase)

    for i in range(len(contenu)):
        caractere = contenu[i]
        cle_caractere = cle_phrase[i % cle_length]
        ascii_value = (ord(caractere) - ord(cle_caractere))- 3 
        contenu_crypte += chr(ascii_value)

    return contenu_crypte

def renommer_decryptfichier():
    chemin_fichier = entre_nomfichier.get()
    cle_phrase = entre_cle.get()

    # Lire le contenu du fichier
    with open(chemin_fichier, 'r', encoding="utf-8", errors='ignore') as fichier:
        contenu = fichier.read()

    contenu_crypte = decryptage_caractere(contenu, cle_phrase)

    # Écrire le contenu crypté dans le même fichier
    with open(chemin_fichier, 'w', encoding="utf-8", errors='ignore') as fichier_crypte:
        fichier_crypte.write(contenu_crypte)

    # Renommer le fichier après l'avoir fermé
    nouveau_nom = filedialog.asksaveasfilename(defaultextension=".txt")
    if nouveau_nom:
        os.rename(chemin_fichier, nouveau_nom)

def renommer_cryptfichier():
    chemin_fichier = entre_nomfichier.get()
    cle_phrase = entre_cle.get()

    # Lire le contenu du fichier
    with open(chemin_fichier, 'r', encoding="utf-8", errors='ignore') as fichier:
        contenu = fichier.read()

    contenu_crypte = cryptage_caractere(contenu, cle_phrase)

    # Écrire le contenu crypté dans le même fichier
    with open(chemin_fichier, 'w', encoding="utf-8", errors='ignore') as fichier_crypte:
        fichier_crypte.write(contenu_crypte)

    # Renommer le fichier après l'avoir fermé
    nouveau_nom = filedialog.asksaveasfilename(defaultextension=".txt")
    if nouveau_nom:
        os.rename(chemin_fichier, nouveau_nom)

root = Tk()
root.geometry('500x250') # taille fenetre
root.title("Logiciel de cryptage et de decryptage")
root.resizable(width=False, height=False) # Pas de pleine écran

# taille img
crypter_photo = taille_image("cryptage-des-donnees (1).png", 100, 100)
decrypter_photo = taille_image("decryptage.png", 100, 100)

# Cadre pour bouton
cadre_buttons = Frame(root)
cadre_buttons.pack(pady=10)

# Btn Crypter
btn_crypter = Button(cadre_buttons, image=crypter_photo, command=renommer_cryptfichier)
btn_crypter.pack(side=LEFT, padx=10)

# Bouton Décrypter
btn_decrypter = Button(cadre_buttons, image=decrypter_photo, command=renommer_decryptfichier)
btn_decrypter.pack(side=RIGHT, padx=10)

# Cadre pour le parcourir
cadre_fichier = Frame(root)
cadre_fichier.pack(pady=10)

etiquette_nomfichier = Label(cadre_fichier, text="Sélectionnez le fichier :")
etiquette_nomfichier.grid(row=0, column=0, padx=5, sticky="w")

entre_nomfichier = Entry(cadre_fichier, width=40)
entre_nomfichier.grid(row=0, column=1, padx=5)

btn_parcourir = Button(cadre_fichier, text="Parcourir", command=parcourir)
btn_parcourir.grid(row=0, column=2, padx=5)

# Cadre pour la clé de cryptage
cadre_cle = Frame(root)
cadre_cle.pack(pady=10)

label_key = Label(cadre_cle, text="Entrez la clé :")
label_key.grid(row=0, column=0, padx=5, sticky="w")

entre_cle = Entry(cadre_cle, width=40)
entre_cle.grid(row=0, column=1, padx=5)

# Bouton Quitter
btn_quitter = Button(root, text="Quitter", command=root.destroy)
btn_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()