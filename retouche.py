from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Coucou !")
label.pack()

bouton = Button(fenetre, text="Quit", command=fenetre.quit)
bouton.pack()


fenetre.mainloop()

