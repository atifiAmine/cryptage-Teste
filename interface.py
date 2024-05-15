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

def crypter_contenu(contenu, key_phrase):
    contenu_crypte = ""
    for caractere in contenu:
        ascii_value = ord(caractere) + 65
        resultat = ascii_value
        contenu_crypte += chr(resultat)
    return contenu_crypte

def crypter_fichier():
    filepath = entry_filename.get()
    key_phrase = entry_key.get()

    with open(filepath, 'r', encoding="utf-8", errors='ignore') as fichier:
        contenu = fichier.read()

    contenu_crypte = crypter_contenu(contenu, key_phrase)

    nouveau_fichier = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(nouveau_fichier, 'w', encoding="utf-8", errors='ignore') as fichier_crypte:
        fichier_crypte.write(contenu_crypte)
#https://www.journaldunet.fr/developpeur/developpement/1441055-corriger-l-erreur-unicodedecodeerror-utf-8-codec-can-t-decode-byte-0xff-in-position-0-invalid-start-byte/
root = Tk()
root.geometry('500x250') #taille fenetre
root.title("Logiciel de cryptage et de decryptage")
root.resizable(width=False, height=False) #Pas de pleine écran

# taile img
crypter_photo = resize_image("cryptage-des-donnees (1).png", 100, 100)
decrypter_photo = resize_image("decryptage.png", 100, 100)

# Cadre pour bouton
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

# Bouton Crypter
btn_crypter = Button(frame_buttons, image=crypter_photo, command=crypter_fichier)
btn_crypter.pack(side=LEFT, padx=10)

# Bouton Décrypter
btn_decrypter = Button(frame_buttons, image=decrypter_photo, command=decrypter_photo)
btn_decrypter.pack(side=RIGHT, padx=10)


root.mainloop()
