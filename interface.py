from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


root = Tk()
root.geometry('300x250')
root.title("Cryptage / Décryptage de fichier")

def parcourir():
    filepath = filedialog.askopenfilename()
    entry_filename.delete(0, END)
    entry_filename.insert(0, filepath)

def crypter():
    #code
    pass

def decrypter():
    #code
    pass

crypter_img = Image.open("cryptage-des-donnees (1).png")
decrypter_img = Image.open("decryptage.png")


crypter_photo = ImageTk.PhotoImage(crypter_img)
decrypter_photo = ImageTk.PhotoImage(decrypter_img)

btn_crypter = Button(root, image=crypter_photo, command=crypter)
btn_crypter.pack(side=LEFT, padx=10)

btn_decrypter = Button(root, image=decrypter_photo, command=decrypter)
btn_decrypter.pack(side=RIGHT, padx=10)


btn_parcourir = Button(root, text="Parcourir", command=parcourir)
btn_parcourir.pack()


label_filename = Label(root, text="Nom du fichier:")
label_filename.pack()

entry_filename = Entry(root, width=50)
entry_filename.pack()


label_key = Label(root, text="Clé de cryptage:")
label_key.pack()

entry_key = Entry(root, width=50)
entry_key.pack()


btn_quitter = Button(root, text="Quitter", command=root.destroy)
btn_quitter.pack(side=BOTTOM)

root.mainloop()
