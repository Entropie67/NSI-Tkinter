from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Coucou !")
label.pack()

bouton = Button(fenetre, text="Quit", command=fenetre.quit)
bouton.pack()


variable = StringVar()
variable.set("Tapez votre texte")
entre = Entry(fenetre, textvariable=variable, width=50)
entre.pack()



fenetre.mainloop()

