from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from hashlib import sha256

root = Tk()
root.geometry('300x250')
root.title("Cryptage / Décryptage de fichier")

def parcourir():
    filepath = filedialog.askopenfilename()
    entry_filename.delete(0, END)
    entry_filename.insert(0, filepath)

def crypter():
    entree = entry_filename.get()  # Récupère le nom du fichier à chiffrer depuis l'entrée
    sortie = "fichier_chiffre.txt"  # Nom du fichier de sortie chiffré
    key = entry_key.get()  # Clé de chiffrement récupérée depuis l'entrée
    keys = sha256(key.encode('utf-8')).digest()

    with open(entree, 'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i = 0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i % len(keys)
                b = bytes([c ^ keys[j]])
                f_sortie.write(b)
                i = i + 1

def decrypter():
    entree = entry_filename.get()  # Récupère le nom du fichier à déchiffrer depuis l'entrée
    sortie = "fichier_dechiffre.txt"  # Nom du fichier de sortie déchiffré
    key = entry_key.get()  # Clé de déchiffrement récupérée depuis l'entrée
    keys = sha256(key.encode('utf-8')).digest()

    with open(entree, 'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i = 0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i % len(keys)
                b = bytes([c ^ keys[j]])
                f_sortie.write(b)
                i = i + 1

# Charger les images
crypter_img = Image.open("cryptage-des-donnees (1).png")
decrypter_img = Image.open("decryptage.png")

# Convertir les images pour Tkinter
crypter_photo = ImageTk.PhotoImage(crypter_img)
decrypter_photo = ImageTk.PhotoImage(decrypter_img)

# Créer les boutons avec les images
btn_crypter = Button(root, image=crypter_photo, command=crypter)
btn_crypter.pack(side=LEFT, padx=10)

btn_decrypter = Button(root, image=decrypter_photo, command=decrypter)
btn_decrypter.pack(side=RIGHT, padx=10)

# Parcourir le bouton
btn_parcourir = Button(root, text="Parcourir", command=parcourir)
btn_parcourir.pack()

# Champ de texte pour le nom du fichier
label_filename = Label(root, text="Nom du fichier:")
label_filename.pack()

entry_filename = Entry(root, width=50)
entry_filename.pack()

# Champ de texte pour la clé de cryptage
label_key = Label(root, text="Clé de cryptage:")
label_key.pack()

entry_key = Entry(root, width=50)
entry_key.pack()

# Bouton quitter
btn_quitter = Button(root, text="Quitter", command=root.destroy)
btn_quitter.pack(side=BOTTOM)

root.mainloop()
