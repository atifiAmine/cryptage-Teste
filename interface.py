from tkinter import *

root = Tk()

root.geometry('100x100')

btn = Button(root, text='Quitter', command=root.destroy)

btn.pack(side='bottom')

root.mainloop()
