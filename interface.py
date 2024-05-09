from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)

def parcourir():
    filepath = filedialog.askopenfilename()
    entry_filename.delete(0, END)
    entry_filename.insert(0, filepath)

def cryptage(key_phrase,caractere):
    ascii_value = ord(caractere) +65
    resultat = ascii_value
    return resultat

key_phrase = input("Veuillez entrer une clé : ")
with open( parcourir ,'r') as fichier :
    contenu = fichier.read()

contenu_crypte =""
for caractere in contenu : 
    resultat2 = cryptage(key_phrase,caractere)
    contenu_crypte = contenu_crypte + chr(resultat2)

nouveau_fichier = input("Le fichier est désormais crypté! Veuillez le renommer :")
with open(nouveau_fichier,'w') as fichier_crypte:
    fichier_crypte.write(contenu_crypte)

    pass

def decrypter():
    # Code
    pass

root = Tk()
root.geometry('400x300')
root.title("Cryptage / Décryptage de fichier")

# taile img
crypter_photo = resize_image("cryptage-des-donnees (1).png", 100, 100)
decrypter_photo = resize_image("decryptage.png", 100, 100)

# Cadre pour bouton
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

# Bouton Crypter
btn_crypter = Button(frame_buttons, image=crypter_photo, command=crypter)
btn_crypter.pack(side=LEFT, padx=10)

# Bouton Décrypter
btn_decrypter = Button(frame_buttons, image=decrypter_photo, command=decrypter)
btn_decrypter.pack(side=RIGHT, padx=10)

# Cadre pour le parcourir
frame_file = Frame(root)
frame_file.pack(pady=10)

label_filename = Label(frame_file, text="Nom du fichier:")
label_filename.grid(row=0, column=0, padx=5, sticky="w")

entry_filename = Entry(frame_file, width=40)
entry_filename.grid(row=0, column=1, padx=5)

btn_parcourir = Button(frame_file, text="Parcourir", command=parcourir)
btn_parcourir.grid(row=0, column=2, padx=5)

# Cadre pour la clé de cryptage
frame_key = Frame(root)
frame_key.pack(pady=10)

label_key = Label(frame_key, text="Clé de cryptage:")
label_key.grid(row=0, column=0, padx=5, sticky="w")

entry_key = Entry(frame_key, width=40)
entry_key.grid(row=0, column=1, padx=5)

# Bouton Quitter
btn_quitter = Button(root, text="Quitter", command=root.destroy)
btn_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()
