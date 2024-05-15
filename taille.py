from tkinter import *
from PIL import Image, ImageTk


'''
Cette fonction ce charge de regler la hateur, la largeur et la position d'une image 
'''

def taille_image(chemin, largeur, hauteur):
    image = Image.open(chemin)
    redimension_image = image.resize((largeur, hauteur))
    return ImageTk.PhotoImage(redimension_image)

root = Tk()
root.geometry('500x250')  # taille fenetre
root.title("Logiciel de cryptage et de decryptage")
root.resizable(width=False, height=False)  # Pas de plein écran

crypter_photo = taille_image("C:\\Users\\Utilisateur\\cryptage-Teste\\cryptage-des-donnees (1).png", 100, 100)
decrypter_photo = taille_image("C:\\Users\\Utilisateur\\cryptage-Teste\\decryptage.png", 100, 100)

# Bouton Crypter
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)
btn_crypter = Button(frame_buttons, image=crypter_photo)
btn_crypter.pack(side=LEFT, padx=10)

# Bouton Décrypter
btn_decrypter = Button(frame_buttons, image=decrypter_photo)
btn_decrypter.pack(side=RIGHT, padx=10)
root.mainloop()
