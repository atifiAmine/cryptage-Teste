from distutils import command
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x250') #taille fenetre
root.title("Logiciel de cryptage et de decryptage")
root.resizable(width=False, height=False) #Pas de pleine écran



def cle(frame_key):
    frame_key = Frame(root)
    frame_key.pack(pady=10)

    label_key = Label(frame_key, text="Entrez la clé :")
    label_key.grid(row=0, column=0, padx=5, sticky="w")

    entry_key = Entry(frame_key, width=40)
    entry_key.grid(row=0, column=1, padx=5)
    
frame_key = Frame(root)
frame_key.pack(pady=10)

label_key = Label(frame_key, text="Entrez la clé :")
label_key.grid(row=0, column=0, padx=5, sticky="w")

entry_key = Entry(frame_key, width=40, command=cle)
entry_key.grid(row=0, column=1, padx=5)  



root.mainloop()